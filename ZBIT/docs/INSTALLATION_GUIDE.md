# 🔧 GUIA DE INSTALAÇÃO - ZBIT Framework

## ⚠️ Problema Encontrado e Solução

### O Erro
```
tomllib.TOMLDecodeError: Cannot overwrite a value (at line 132, column 22)
```

**Causa:** O arquivo `pyproject.toml` original tinha uma **seção duplicada** `[build-system]` definida duas vezes.

### ✅ Solução

#### Passo 1: Substituir pyproject.toml
Remova o arquivo `pyproject.toml` antigo e use a versão corrigida [32]:

1. Baixe [32] - pyproject-fixed.toml
2. Renomeie para `pyproject.toml`
3. Coloque na raiz do projeto

#### Passo 2: Adicionar setup.py
Baixe [33] - setup.py e coloque na raiz do projeto.

#### Passo 3: Instalar (Windows)
```bash
# Limpar cache pip
pip cache purge

# Instalar dependencies
pip install --upgrade pip setuptools wheel

# Instalar em modo desenvolvimento
cd C:\Users\PC\Desktop\protocolo SAO\ZBIT
pip install -e ".[dev]"
```

---

## 📁 Estrutura Esperada

```
ZBIT/
├── pyproject.toml          ✅ CORRIGIDO [32]
├── setup.py                ✅ NOVO [33]
├── requirements.txt        ✅ [15]
├── zbit/
│   ├── __init__.py         ✅ [28]
│   └── core/
│       ├── __init__.py     ✅ [27]
│       ├── types.py        ✅ [22]
│       ├── encoder.py      ✅ [23]
│       ├── processor.py    ✅ [24]
│       ├── anomaly.py      ✅ [25]
│       ├── engine.py       ✅ [26]
│       └── exceptions.py   ✅ [17]
├── tests/
│   ├── conftest.py         ✅ [29]
│   └── test_core.py        ✅ [30]
└── docs/
    └── ARCHITECTURE.md     ✅ [16]
```

---

## 🚀 Instalação Passo-a-Passo (Windows)

### 1. Preparar Ambiente
```bash
# Abrir PowerShell ou CMD como Administrador
cd C:\Users\PC\Desktop\protocolo SAO\ZBIT

# Limpar pip cache
pip cache purge

# Verificar versão Python
python --version  # Deve ser 3.9+
```

### 2. Instalar Dependências Base
```bash
# Atualizar ferramentas base
pip install --user --upgrade pip setuptools wheel

# Instalar build essentials
pip install --user build
```

### 3. Instalar ZBIT em Modo Desenvolvimento
```bash
# Navegar para o diretório ZBIT
cd C:\Users\PC\Desktop\protocolo SAO\ZBIT

# Instalar com dependencies de desenvolvimento
pip install --user -e ".[dev]"
```

### 4. Validar Instalação
```bash
# Teste 1: Importar módulo
python -c "from zbit import ZBITEngine; print('✅ ZBIT importado com sucesso!')"

# Teste 2: Criar engine
python -c "from zbit import ZBITEngine; e = ZBITEngine(); print('✅ Engine criado!')"

# Teste 3: Rodar teste rápido
python -c "
from zbit import ZBITEngine
engine = ZBITEngine()
record = engine.encode_byte(170)
print(f'✅ Byte codificado: {record.to_binary()}')
"
```

---

## 🧪 Rodando Testes

### Teste Rápido (5 minutos)
```bash
# Instalar pytest se não tiver
pip install --user pytest pytest-cov

# Rodar apenas testes unitários rápidos
cd C:\Users\PC\Desktop\protocolo SAO\ZBIT
pytest tests/test_core.py -v --tb=short
```

### Teste Completo com Cobertura (10 minutos)
```bash
# Rodar testes com cobertura
pytest tests/test_core.py -v --cov=zbit --cov-report=html

# Abrir relatório
start htmlcov/index.html
```

### Teste Específico
```bash
# Testar apenas Encoder
pytest tests/test_core.py::TestZBITEncoder -v

# Testar apenas um teste
pytest tests/test_core.py::TestZBITEncoder::test_encode_byte_valid -v
```

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'zbit'"

**Solução:**
```bash
# Reinstalar em modo editable
pip install --user --force-reinstall -e .

# Ou com verbose
pip install --user -e . -vvv
```

### Problema: "ERROR: Could not find a version"

**Solução:**
```bash
# Certifique-se de estar no diretório correto
cd C:\Users\PC\Desktop\protocolo SAO\ZBIT
dir pyproject.toml  # Deve existir

# Limpar cache
pip cache purge

# Instalar novamente
pip install --user -e ".[dev]"
```

### Problema: "Cannot overwrite a value"

**Solução:**
```bash
# Verificar pyproject.toml duplicações
# Use o arquivo corrigido [32]
# Copiar conteúdo de pyproject-fixed.toml → pyproject.toml

# Validar TOML
python -c "import tomllib; print(tomllib.loads(open('pyproject.toml').read()))"
```

### Problema: "site-packages is not writeable"

**Solução 1 (Recomendado):**
```bash
# Usar --user flag (já está nos comandos acima)
pip install --user -e ".[dev]"
```

**Solução 2 (Ambiente Virtual):**
```bash
# Criar venv
python -m venv venv

# Ativar venv
venv\Scripts\activate

# Instalar sem --user
pip install -e ".[dev]"
```

---

## ✅ Verificação Final

Após instalação bem-sucedida, deve funcionar:

```python
# test_installation.py
from zbit import ZBITEngine, AnomalousRecord
from zbit.core import ZBITConfig

# 1. Criar engine
engine = ZBITEngine()
print("✅ Engine criado")

# 2. Codificar
record = engine.encode_byte(170)
print(f"✅ Codificado: {record.to_binary()}")

# 3. Decodificar
result = engine.decode_and_correct(record)
print(f"✅ Decodificado: {result.original_value}")

# 4. Métricas
metrics = engine.get_metrics()
print(f"✅ Bytes processados: {metrics.bytes_encoded}")

print("\n🎉 ZBIT Framework instalado com sucesso!")
```

Salve como `test_installation.py` e rode:
```bash
python test_installation.py
```

---

## 📦 Ficheiros Necessários

Para instalação local completa, baixe em ordem:

| # | Arquivo | Essencial |
|---|---------|-----------|
| 32 | pyproject-fixed.toml | ✅ CRÍTICO |
| 33 | setup.py | ✅ IMPORTANTE |
| 28 | zbit/__init__.py | ✅ CRÍTICO |
| 27 | zbit/core/__init__.py | ✅ CRÍTICO |
| 22 | zbit/core/types.py | ✅ CRÍTICO |
| 23 | zbit/core/encoder.py | ✅ CRÍTICO |
| 24 | zbit/core/processor.py | ✅ CRÍTICO |
| 25 | zbit/core/anomaly.py | ✅ CRÍTICO |
| 26 | zbit/core/engine.py | ✅ CRÍTICO |
| 17 | zbit/core/exceptions.py | ✅ CRÍTICO |
| 29 | tests/conftest.py | ⚠️ Para testes |
| 30 | tests/test_core.py | ⚠️ Para testes |
| 15 | requirements.txt | ℹ️ Referência |

---

## 🎓 Próximos Passos

Após instalação bem-sucedida:

1. **Rodar testes**: `pytest tests/ -v`
2. **Verificar cobertura**: `pytest --cov=zbit`
3. **Explorar API**: Abrir Python e testar `from zbit import ZBITEngine`
4. **Ler docs**: Ver [16] ARCHITECTURE.md
5. **Começar desenvolvimento**: Week 3 - Physics Module

---

**Status:** ✅ Guia de instalação completo  
**Data:** 25 de Outubro de 2025, 23:50 BST  
**Versão:** ZBIT 1.0.0-alpha.1

🚀 **Sucesso na instalação!**
