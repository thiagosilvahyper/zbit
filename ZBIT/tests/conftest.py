import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# tests/conftest.py
"""
Configuração global de testes pytest para ZBIT Framework.

Define fixtures reutilizáveis, configuração de logging e helpers.
"""

import pytest
import logging
from typing import List
from zbit import ZBITEngine, ZBITEncoder, ZBITProcessor, AnomalySimulator
from zbit.core.types import AnomalousRecord, ZBITConfig


# ========== CONFIGURAÇÃO DE LOGGING ==========

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configura logging para os testes."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    logger = logging.getLogger("zbit")
    logger.setLevel(logging.DEBUG)


# ========== FIXTURES DE COMPONENTES ==========

@pytest.fixture
def clean_engine():
    """Fornece um ZBITEngine limpo para cada teste."""
    return ZBITEngine()


@pytest.fixture
def verbose_engine():
    """Fornece um ZBITEngine com verbose=True."""
    config = ZBITConfig(verbose=True)
    return ZBITEngine(config=config)


@pytest.fixture
def encoder():
    """Fornece um ZBITEncoder."""
    return ZBITEncoder()


@pytest.fixture
def processor():
    """Fornece um ZBITProcessor."""
    return ZBITProcessor()


@pytest.fixture
def anomaly_simulator():
    """Fornece um AnomalySimulator padrão."""
    return AnomalySimulator()


@pytest.fixture
def custom_anomaly_simulator():
    """Fornece um AnomalySimulator com configurações customizadas."""
    return AnomalySimulator(
        p1_critical_iteration=100,
        p2_complexity_threshold=150,
        p3_enabled=True,
        metavacuum_energy=3000.0,
        boost_rate=0.9
    )


# ========== FIXTURES DE DADOS ==========

@pytest.fixture
def sample_byte():
    """Byte de teste padrão (170 = 10101010)."""
    return 170


@pytest.fixture
def sample_bytes():
    """Array de bytes de teste."""
    return [0, 1, 127, 128, 255, 170, 85, 240]


@pytest.fixture
def sample_message():
    """Mensagem de teste padrão."""
    return b"ZBIT Framework Test Message"


@pytest.fixture
def large_dataset():
    """Dataset grande para stress tests (1MB)."""
    return bytes([i % 256 for i in range(1_000_000)])


@pytest.fixture
def sample_record(encoder, sample_byte):
    """Registro Anômalo de teste."""
    return encoder.encode_byte(sample_byte)


@pytest.fixture
def corrupted_record(sample_record):
    """Registro Anômalo corrompido no bit 3."""
    corrupted = AnomalousRecord(
        BA=sample_record.BA.copy(),
        BG=sample_record.BG,
        BP=sample_record.BP,
        BAL=sample_record.BAL.copy()
    )
    corrupted.BA[3] = 1 - corrupted.BA[3]  # Corrompe bit 3
    return corrupted, 3  # (record, error_index)


@pytest.fixture
def sample_records(encoder, sample_bytes):
    """Lista de Registros Anômalos."""
    return [encoder.encode_byte(b) for b in sample_bytes]


# ========== FIXTURES DE CONFIGURAÇÃO ==========

@pytest.fixture
def default_config():
    """Configuração ZBIT padrão."""
    return ZBITConfig()


@pytest.fixture
def custom_config():
    """Configuração ZBIT customizada."""
    return ZBITConfig(
        verbose=True,
        track_metrics=True,
        p1_critical_iteration=100,
        p2_complexity_threshold=150,
        metavacuum_energy_per_jump=3000.0,
        energy_boost_rate=0.9
    )


# ========== HELPERS ==========

@pytest.fixture
def introduce_error():
    """Helper para introduzir erro em Registro Anômalo."""
    def _introduce_error(record: AnomalousRecord, bit_index: int = 0) -> AnomalousRecord:
        """Corrompe um bit específico."""
        corrupted = AnomalousRecord(
            BA=record.BA.copy(),
            BG=record.BG,
            BP=record.BP,
            BAL=record.BAL.copy()
        )
        if 0 <= bit_index < 8:
            corrupted.BA[bit_index] = 1 - corrupted.BA[bit_index]
        return corrupted
    
    return _introduce_error


@pytest.fixture
def create_records():
    """Helper para criar múltiplos registros."""
    def _create_records(values: List[int]) -> List[AnomalousRecord]:
        encoder = ZBITEncoder()
        return [encoder.encode_byte(v) for v in values]
    
    return _create_records


# ========== MARKERS ==========

def pytest_configure(config):
    """Registra markers customizados."""
    config.addinivalue_line(
        "markers", "unit: marca testes unitários"
    )
    config.addinivalue_line(
        "markers", "integration: marca testes de integração"
    )
    config.addinivalue_line(
        "markers", "slow: marca testes lentos (>1s)"
    )
    config.addinivalue_line(
        "markers", "benchmark: marca benchmarks de performance"
    )
    config.addinivalue_line(
        "markers", "anomaly: marca testes de anomalias"
    )


# ========== HOOKS ==========

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para adicionar informações extras aos relatórios de teste."""
    outcome = yield
    rep = outcome.get_result()
    
    # Adiciona informação de duração longa
    if rep.when == "call" and rep.duration > 1.0:
        rep.sections.append(("Slow Test", f"Duração: {rep.duration:.2f}s"))


# ========== FIXTURES DE VALIDAÇÃO ==========

@pytest.fixture
def assert_valid_record():
    """Helper para validar Registro Anômalo."""
    def _assert_valid(record: AnomalousRecord):
        assert len(record.BA) == 8, f"BA deve ter 8 bits, tem {len(record.BA)}"
        assert record.BG in [0, 1], f"BG deve ser 0 ou 1, é {record.BG}"
        assert record.BP in [0, 1], f"BP deve ser 0 ou 1, é {record.BP}"
        assert len(record.BAL) == 2, f"BAL deve ter 2 bits, tem {len(record.BAL)}"
        assert all(b in [0, 1] for b in record.BA), "BA contém valores inválidos"
        assert all(b in [0, 1] for b in record.BAL), "BAL contém valores inválidos"
    
    return _assert_valid


@pytest.fixture
def assert_metrics_updated():
    """Helper para validar atualização de métricas."""
    def _assert_updated(metrics_before, metrics_after, expected_increments):
        for metric, increment in expected_increments.items():
            before = getattr(metrics_before, metric)
            after = getattr(metrics_after, metric)
            assert after == before + increment, (
                f"Métrica '{metric}' esperava {before + increment}, obteve {after}"
            )
    
    return _assert_updated
