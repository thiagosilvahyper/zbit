# 🧪 ZBIT Framework - Plano de Testes Completo

## Visão Geral

Suite de testes estratificada em 4 níveis: unitários, integração, benchmarks e segurança.
**Target:** >95% de cobertura total de código

---

## 1. Testes Unitários (60+ testes)

### 1.1 Core Engine Tests (`test_core.py`)

#### Princípio 1: Trajetória Refletida
```python
test_encode_byte_valid()                 # Codifica byte válido
test_encode_byte_zero()                  # Edge case: 0
test_encode_byte_max()                   # Edge case: 255
test_encode_byte_invalid()               # Rejeita >255
test_detect_error_clean_record()         # Sem erro
test_detect_error_corrupted()            # Detecta erro
test_correct_single_error()              # Corrige 1 erro
test_correct_error_invalid_index()       # Index fora do range
```

#### Princípio 2: Ecos do Futuro
```python
test_calculate_premonition_low()         # BP=0 para simples
test_calculate_premonition_high()        # BP=1 para complexo
test_quantum_jump_with_bp()              # Salta com BP=1
test_quantum_jump_without_bp()           # Não salta com BP=0
test_jump_iterations_calculation()       # Calcula corretamente
```

#### Princípio 3: Energia Sem Origem
```python
test_check_alignment_all_true()          # Alinhamento ativado
test_check_alignment_p1_false()          # P1 falso → sem anomalia
test_check_alignment_p2_false()          # P2 falso → sem anomalia
test_check_alignment_p3_false()          # P3 falso → sem anomalia
test_collect_metavacuum_energy()         # Coleta energia
test_metavacuum_state_updated()          # Estado atualizado
```

#### Codificação/Decodificação
```python
test_encode_bulk_multiple_bytes()        # Lote de 10 bytes
test_encode_bulk_empty()                 # Lista vazia
test_decode_and_correct_valid()          # Decodifica válido
test_decode_and_correct_with_error()     # Decodifica e corrige
```

### 1.2 Physics Tests (`test_physics.py`)

#### Princípios
```python
test_principle1_twin_bit_logic()         # Lógica do BG
test_principle2_premonition_logic()      # Lógica do BP
test_principle3_alignment_logic()        # Lógica de alinhamento
test_all_principles_independent()        # Independência dos princípios
```

#### Metavácuo
```python
test_metavacuum_initial_state()          # Estado inicial
test_metavacuum_energy_collection()      # Coleta energia
test_metavacuum_state_persistence()      # Estado persiste
test_metavacuum_overflow_handling()      # Manejo de overflow
```

#### Retrocausalidade
```python
test_retrocausal_prediction()            # Previsão correta
test_retrocausal_history_tracking()      # Histórico correto
```

---

## 2. Testes de Integração (20+ testes)

### 2.1 End-to-End Flows

```python
test_encode_corrupt_decode()             # Ciclo completo
test_multiple_messages()                 # Múltiplas mensagens
test_anomaly_activation_full_flow()      # Com ativação de anomalia
test_high_error_rate_recovery()          # Taxa alta de erros
test_bulk_processing()                   # Processamento em lote (1MB+)
```

### 2.2 Interação entre Módulos

```python
test_core_physics_integration()          # Core + Physics
test_core_api_integration()              # Core + API
test_physics_metavacuum_sync()           # Physics + Metavácuo sincronizado
```

### 2.3 Stress Tests

```python
test_large_dataset_encoding()            # Dataset de 1MB
test_rapid_fire_operations()             # 10.000 ops/sec
test_memory_efficiency()                 # Sem memory leaks
test_concurrent_encoding()               # Múltiplas threads
```

---

## 3. Benchmarks (10+ benchmarks)

### 3.1 Performance vs Hamming Code

```python
bench_zbit_encode_vs_hamming()
bench_zbit_decode_vs_hamming()
bench_zbit_error_correction_vs_hamming()
bench_zbit_throughput_vs_hamming()
```

**Esperado:** ZBIT comparable ou melhor em 9 bits vs Hamming 12-15 bits

### 3.2 Performance Absoluta

```python
bench_encode_byte()                      # Operação atômica
bench_encode_1kb()                       # 1 KB
bench_encode_1mb()                       # 1 MB
bench_full_pipeline()                    # Encode + Anomaly + Decode
```

**Target:**
- Encode/Decode: <1µs por byte
- Anomaly: <100ms para 10.000 bytes

### 3.3 Escalabilidade

```python
bench_scaling_vs_data_size()             # O(n)?
bench_memory_usage()                     # Memória usada
bench_energy_efficiency()                # Energia "coletada"
```

---

## 4. Testes de API (20+ testes)

### 4.1 REST Endpoints

```python
test_post_encode_valid()                 # POST /encode
test_post_encode_invalid()               # POST /encode (erro)
test_post_decode_valid()                 # POST /decode
test_post_simulate_valid()               # POST /simulate
test_get_metrics()                       # GET /metrics
test_get_physics_state()                 # GET /physics/state
test_get_health()                        # GET /health
```

### 4.2 Error Handling

```python
test_api_invalid_input()                 # Validação Pydantic
test_api_timeout()                       # Timeout em operação longa
test_api_rate_limiting()                 # Rate limit
test_api_authentication()                # Autenticação (se aplicável)
```

---

## 5. Testes de Segurança

### 5.1 Input Validation

```python
test_no_sql_injection()                  # N/A para este projeto
test_no_command_injection()              # N/A
test_large_input_handling()              # Limita tamanho input
test_malformed_data()                    # Rejeita dados ruim
```

### 5.2 Dependency Check

- Usar `safety check` para CVEs
- Usar `bandit` para code security issues

---

## 6. Configuração de Testes (conftest.py)

### Fixtures

```python
@pytest.fixture
def clean_engine():
    """Fornece engine limpo para cada teste"""
    return ZBITEngine()

@pytest.fixture
def sample_data():
    """Dados de teste padrão"""
    return bytes([170, 200, 255, 100])

@pytest.fixture
def large_dataset():
    """Dataset grande para stress tests"""
    return bytes([i % 256 for i in range(1000000)])
```

### Markers

```python
@pytest.mark.unit              # Testes unitários
@pytest.mark.integration       # Testes de integração
@pytest.mark.slow              # Testes lentos (skip com -m "not slow")
@pytest.mark.benchmark         # Benchmarks
@pytest.mark.security          # Testes de segurança
```

---

## 7. Cobertura Alvo por Módulo

| Módulo | Target | Método |
|--------|--------|--------|
| `core/engine.py` | 100% | Direto (crítico) |
| `core/encoder.py` | 100% | Direto (crítico) |
| `core/processor.py` | 100% | Direto (crítico) |
| `core/exceptions.py` | 90% | Via testes |
| `physics/principles.py` | 95% | Cobertura |
| `physics/metavacuum.py` | 95% | Cobertura |
| `api/routes.py` | 90% | API tests |
| `cli/commands.py` | 85% | CLI tests |
| **TOTAL** | **>95%** | Agregado |

---

## 8. Estratégia de Execução

### Desenvolvimento (Local)

```bash
# Testes rápidos apenas
pytest tests/ -m "not slow"

# Com cobertura
pytest tests/ --cov=zbit --cov-report=html

# Teste específico
pytest tests/test_core.py::test_encode_byte_valid -v
```

### CI/CD (GitHub Actions)

```bash
# Todos os testes
pytest tests/ \
  --cov=zbit \
  --cov-report=xml \
  --cov-report=term-missing \
  -v

# Apenas se passar
# Então: black, pylint, mypy
# Então: build distribution
```

### Pre-Commit (Local)

```bash
# Automático antes de commit
pytest tests/ -m "not slow" -x  # Stop on first failure
```

---

## 9. Metas de Qualidade

### Semana 1-2 (Atual)
- [ ] Setup pytest + fixtures
- [ ] Primeiros 20 testes unitários
- [ ] Cobertura inicial ~30%

### Semana 3-4
- [ ] 60+ testes unitários
- [ ] 20+ testes integração
- [ ] Cobertura ~70%

### Semana 5-6
- [ ] Benchmarks + stress tests
- [ ] API tests
- [ ] Cobertura ~90%

### Semana 7-8
- [ ] 100+ testes total
- [ ] Cobertura >95%
- [ ] Security checks passando

---

## 10. Ferramentas

- **pytest** - Framework principal
- **pytest-cov** - Cobertura
- **pytest-xdist** - Testes paralelos
- **pytest-benchmark** - Benchmarks
- **hypothesis** - Property-based testing (opcional)
- **black** - Formatação
- **mypy** - Type checking
- **bandit** - Security check
- **safety** - Dependency check

---

**Status:** ✅ Plano finalizado Week 1  
**Próximo:** Implementar testes durante Week 2-3
