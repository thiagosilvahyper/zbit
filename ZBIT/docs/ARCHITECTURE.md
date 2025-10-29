# 🏗️ ZBIT Framework - Arquitetura Profissional

## Visão Geral

O ZBIT Framework é estruturado em módulos independentes mas interconectados, permitindo desenvolvimento paralelo, testes isolados e fácil manutenção.

---

## Estrutura de Diretórios

```
zbit-framework/
├── zbit/                           # Package principal
│   ├── __init__.py                 # Exports públicos
│   ├── version.py                  # Versionamento
│   │
│   ├── core/                       # 🔷 Motor Central ZBIT
│   │   ├── __init__.py
│   │   ├── engine.py               # ⭐ ZBITEngine (classe centralizada)
│   │   ├── encoder.py              # Codificação para Registro Anômalo
│   │   ├── processor.py            # Processamento e correção
│   │   ├── anomaly.py              # Simulação de anomalias
│   │   ├── exceptions.py           # Exceções customizadas
│   │   └── types.py                # Type hints reutilizáveis
│   │
│   ├── physics/                    # 🌌 Simulação Física Quântica
│   │   ├── __init__.py
│   │   ├── principles.py           # 3 Princípios ASAQ
│   │   ├── metavacuum.py           # Simulação do Vácuo Quântico
│   │   ├── retrocausality.py       # Lógica Retrocausal
│   │   └── constants.py            # Constantes físicas simuladas
│   │
│   ├── api/                        # 🌐 Interface REST (FastAPI)
│   │   ├── __init__.py
│   │   ├── main.py                 # Aplicação FastAPI
│   │   ├── models.py               # Schemas Pydantic
│   │   ├── routes.py               # Rotas dos endpoints
│   │   └── middleware.py           # Middlewares customizados
│   │
│   └── cli/                        # 💻 Interface de Linha de Comando
│       ├── __init__.py
│       ├── commands.py             # Comandos principais
│       └── utils.py                # Utilitários CLI
│
├── tests/                          # 🧪 Suite de Testes
│   ├── __init__.py
│   ├── test_core.py                # Testes do core engine
│   ├── test_physics.py             # Testes da física
│   ├── test_integration.py         # Testes de integração
│   ├── test_benchmarks.py          # Benchmarks de performance
│   ├── test_api.py                 # Testes da API
│   ├── conftest.py                 # Configuração pytest
│   └── fixtures.py                 # Dados de teste
│
├── docs/                           # 📚 Documentação
│   ├── README.md                   # Guia de início rápido
│   ├── ARCHITECTURE.md             # Este arquivo
│   ├── API.md                      # Referência completa da API
│   ├── PHYSICS.md                  # Explicação dos princípios
│   ├── EXAMPLES.md                 # Exemplos práticos
│   ├── CONTRIBUTING.md             # Guia de contribuições
│   ├── INSTALLATION.md             # Guia de instalação
│   └── images/                     # Imagens e diagramas
│
├── .github/                        # ⚙️ Automação GitHub
│   └── workflows/
│       ├── ci.yml                  # CI/CD Pipeline
│       ├── publish.yml             # Publicação PyPI
│       └── docs.yml                # Build da documentação
│
├── pyproject.toml                  # Configuração do projeto (PEP 518)
├── setup.py                        # Setup legacy (compatibilidade)
├── requirements.txt                # Dependências congeladas
├── requirements-dev.txt            # Dependências de desenvolvimento
├── .gitignore                      # Gitignore
├── LICENSE                         # MIT License
├── Dockerfile                      # Containerização
└── .dockerignore                   # Docker ignore
```

---

## Módulos Core

### 1. `zbit/core/engine.py` - ZBITEngine (Centralizado)

```python
class ZBITEngine:
    """Motor principal que integra os 3 princípios ASAQ"""
    
    # Atributos
    - energy_boost_rate: Taxa de coleta de energia
    - metavacuum_state: Estado do vácuo quântico
    - statistics: Métricas de execução
    
    # Métodos Públicos
    - encode_byte(data: int) -> AnomalousRecord
    - decode_and_correct(record: AnomalousRecord) -> Tuple[int, bool]
    - encode_bulk(data: bytes) -> List[AnomalousRecord]
    - simulate_processing_flow(data: bytes) -> Dict
```

**Responsabilidade:** Orquestrar os 3 princípios (Trajetória Refletida, Ecos, Energia)

### 2. `zbit/core/encoder.py` - Codificação

- Converte bytes → Registros Anômalos (RA) de 12 bits
- B0-B7: Dado Causal (BA)
- B8: Bit Gêmeo (BG) - Trajetória Refletida
- B9: Bit Prenúncio (BP) - Ecos do Futuro
- B10-B11: Bits Alinhamento (BAL) - Energia Sem Origem

### 3. `zbit/core/processor.py` - Processamento

- Detecção de erros via Bit Gêmeo
- Correção de um único erro
- Validação de integridade

### 4. `zbit/physics/principles.py` - 3 Princípios

```python
class Principle1_ReflectedTrajectory:
    """Trajetória Refletida - Detecta/corrige erros"""
    
class Principle2_EchoesFromFuture:
    """Ecos do Futuro - Prediz complexidade"""
    
class Principle3_EnergyWithoutOrigin:
    """Energia Sem Origem - Coleta energia do Metavácuo"""
```

---

## Fluxo de Dados

```
┌─────────────────────────────────────────────────┐
│  INPUT: dados brutos (bytes)                     │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  core/encoder.py     │
        │  Codifica em RA      │ (12 bits)
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ physics/principles.py│
        │ Aplicar 3 princípios │
        └──────────┬───────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
    [Sem anomalia]    [Com anomalia]
          │            (alinhamento)
          │                  │
          │          ┌───────▼────────┐
          │          │ Metavácuo      │
          │          │ Coleta energia │
          │          └────────────────┘
          │
          ▼
    ┌──────────────────────┐
    │ core/processor.py    │
    │ Detecta/corrige erros│
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │ OUTPUT: dados correctos
    └──────────────────────┘
```

---

## Interface API (FastAPI)

### Endpoints Primários

```
POST   /api/v1/encode          # Codificar dados
POST   /api/v1/decode          # Decodificar e corrigir
POST   /api/v1/simulate        # Simular com anomalias
GET    /api/v1/metrics         # Métricas em tempo real
GET    /api/v1/physics/state   # Estado do Metavácuo
GET    /api/v1/health          # Health check
```

---

## Padrões de Código

### Conventions

- **Naming:** snake_case para funções, PascalCase para classes
- **Docstrings:** Google-style com type hints
- **Type Hints:** Obrigatórios em todas as funções públicas
- **Testing:** Mínimo 95% cobertura
- **Logging:** Usar `logging` module (não print)

### Exemplo de Função

```python
def encode_byte(data_causal: int) -> AnomalousRecord:
    """
    Codifica um byte em Registro Anômalo ZBIT.
    
    Args:
        data_causal: Valor inteiro (0-255) do byte a codificar
        
    Returns:
        AnomalousRecord com 12 bits codificados
        
    Raises:
        ValueError: Se data_causal não está em [0, 255]
        
    Example:
        >>> record = encode_byte(170)
        >>> print(record.BA)  # [0, 1, 0, 1, 0, 1, 0, 1]
    """
```

---

## Testes

### Estrutura de Testes

```
tests/
├── test_core.py          # ~30 testes unitários
├── test_physics.py       # ~20 testes unitários
├── test_integration.py   # ~15 testes de integração
├── test_benchmarks.py    # ~10 benchmarks
├── test_api.py           # ~20 testes de API
└── conftest.py           # Configuração global
```

### Cobertura Alvo

- Core Engine: 100%
- Physics: 95%
- API: 90%
- CLI: 85%
- **Total: >95%**

---

## CI/CD Pipeline (GitHub Actions)

### `.github/workflows/ci.yml`

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -e ".[dev]"
      - run: pytest --cov
      - run: black --check .
      - run: pylint zbit/
```

### `.github/workflows/publish.yml`

```yaml
name: Publish to PyPI
on:
  release:
    types: [created]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install build
      - run: python -m build
      - run: twine upload dist/*
```

---

## Dependências

### Runtime
- **pydantic>=2.0** - Validação de dados
- **numpy>=1.20** - Cálculos numéricos

### Development
- **pytest>=7.0** - Testes
- **black>=23.0** - Formatação
- **pylint>=2.15** - Linting
- **mypy>=1.0** - Type checking

### API (Opcional)
- **fastapi>=0.95** - Framework web
- **uvicorn[standard]>=0.20** - Servidor ASGI

---

## Roadmap de Implementação

### Semana 1 (ATUAL): Arquitetura
- ✅ Estrutura de diretórios
- ✅ pyproject.toml e configuração
- ✅ GitHub Actions setup
- ⏳ Documentação de arquitetura

### Semana 2: Core Engine
- Refatorar pyzbit_library.py → engine.py
- Consolidar encoder.py e processor.py
- Primeiros 30 testes

### Semana 3-4: Physics Complete
- Implementar 3 princípios completos
- Metavácuo dinâmico
- 50+ testes

### Semana 5-6: API e CLI
- REST API com FastAPI
- CLI com typer/click
- 30+ testes de integração

### Semana 7-8: Testes e Benchmarks
- 100+ testes total
- Benchmarks vs Hamming
- >95% cobertura

### Semana 9: Documentação e Lançamento
- Documentação completa
- Upload PyPI
- GitHub release

---

## Convenções de Versioning

Seguir **Semantic Versioning** (SemVer):

- **1.0.0-alpha.1** (v1.0.0 prévia)
- **1.0.0-beta.1** (v1.0.0 testada)
- **1.0.0** (Release público)
- **1.1.0** (Nova feature - minor bump)
- **2.0.0** (Breaking change - major bump)

---

## Contato e Comunidade

- **GitHub:** github.com/zbit-research/zbit-framework
- **Discussions:** GitHub Discussions
- **Email:** info@zbit-framework.dev
- **Docs:** zbit-framework.readthedocs.io

---

**Status:** ✅ Arquitetura finalizada Week 1  
**Próximo:** Implementação do Core Engine (Week 2)
