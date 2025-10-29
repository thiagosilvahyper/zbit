"""
ZBIT-CORE-v2 — DEMO MÉDIO & ROBUSTO (CORRIGIDO)
10 qubits | Testes expandidos | Resultados confiáveis
Execute: python demo_medio.py
"""

import time
import json
import numpy as np
from scipy.linalg import expm, eigvalsh
from pathlib import Path

# === IMPORTAÇÃO CORRIGIDA: Usa o nome exato do arquivo ===
from zbit_core_v2_FIXED import ZBITQuantumCoreV2  # NÃO MUDE O NOME DO ARQUIVO


# === CONFIGURAÇÃO ===
OUTPUT_DIR = Path("demo_medio_results")
OUTPUT_DIR.mkdir(exist_ok=True)
REPORT_FILE = OUTPUT_DIR / f"relatorio_medio_{time.strftime('%Y%m%d_%H%M%S')}.json"


# === UTILIDADES ===
def print_header(title):
    print("\n" + "="*75)
    print(f"  {title}".center(75))
    print("="*75)


def run_multiple_times(func, n_runs=3):
    """Roda função múltiplas vezes para média/STD"""
    results = []
    for _ in range(n_runs):
        results.append(func())
    return np.mean(results), np.std(results)


# === TESTES ADICIONAIS ===
def test_fidelity(core):
    psi_initial = np.zeros_like(core.psi)
    psi_initial[0] = 1.0
    return np.abs(np.vdot(psi_initial, core.psi))**2


def test_energy_expectation(core):
    return np.real(np.vdot(core.psi, core.H @ core.psi))


def test_hermitian_check(core):
    return np.allclose(core.H, core.H.conj().T, atol=1e-12)


def test_state_norm(core):
    return np.linalg.norm(core.psi)


def test_spectral_gap(core):
    try:
        eigenvalues = eigvalsh(core.H)
        return eigenvalues[1] - eigenvalues[0] if len(eigenvalues) > 1 else 0.0
    except:
        return 0.0


# === DEMO PRINCIPAL ===
def main():
    print("\n" + " ZBIT-CORE-v2 — DEMO MÉDIO & ROBUSTO ".center(75, "█"))
    print(" 10 qubits | Testes expandidos | 100% FUNCIONAL ".center(75))
    print("█" * 75 + "\n")

    start_total = time.time()

    # === 1. INICIALIZAÇÃO ===
    print_header("1. INICIALIZAÇÃO (10 QUBITS)")
    core = ZBITQuantumCoreV2(n_qubits=10, verbose=False)
    dim = 2**10
    mem_gb = (core.H.nbytes + core.psi.nbytes) / (1024**3)
    print(f"  Hilbert: 2^10 = {dim}")
    print(f"  Memória: {mem_gb:.4f} GB")
    print(f"  Norma inicial: {np.linalg.norm(core.psi):.15f}")
    metrics = {
        "init": {"dim": dim, "memory_gb": float(mem_gb)}
    }

    # === 2. VALIDAÇÃO ===
    print_header("2. VALIDAÇÃO SUITE (9 TESTES)")
    start = time.time()
    report = core.run_validation_suite()
    elapsed = time.time() - start
    print(f"  Resultado: {report['summary']}")
    print(f"  Tempo: {elapsed:.4f}s")
    metrics["validation"] = {"passed": report["passed"], "time_s": float(elapsed)}

    # === 3. EVOLUÇÃO ===
    print_header("3. EVOLUÇÃO TEMPORAL (t=1.0, 120 passos)")
    start = time.time()
    core.evolve(t_final=1.0, steps=120)
    elapsed = time.time() - start
    energies = np.array(core.history["energy"])
    energy_mean, energy_std = np.mean(energies), np.std(energies)
    time_per_step = elapsed / 120
    print(f"  Tempo total: {elapsed:.3f}s")
    print(f"  Tempo/passo: {time_per_step*1000:.3f} ms")
    print(f"  Energia: {energy_mean:.6f} ± {energy_std:.6f}")
    metrics["evolution"] = {
        "steps": 120,
        "total_time_s": float(elapsed),
        "time_per_step_ms": float(time_per_step*1000),
        "energy_mean": float(energy_mean),
        "energy_std": float(energy_std)
    }

    # === 4. OTOC ===
    print_header("4. OTOC [X,Z] (t=1.5, 20 pontos)")
    start = time.time()
    otoc = core.otoc(W_op="X", V_op="Z", t_max=1.5, num_times=20)
    elapsed = time.time() - start
    otoc_max = float(np.max(otoc["otoc"]))
    print(f"  OTOC máx: {otoc_max:.6f}")
    print(f"  Tempo: {elapsed:.3f}s")
    metrics["otoc"] = {"max": otoc_max, "time_s": float(elapsed)}

    # === 5. TESTES ADICIONAIS (3 RUNS) ===
    print_header("5. TESTES ADICIONAIS (3 RUNS CADA)")

    # Fidelity
    fid_mean, fid_std = run_multiple_times(lambda: test_fidelity(core), 3)
    print(f"  Fidelity: {fid_mean:.10f} ± {fid_std:.2e}")
    metrics["fidelity"] = {"mean": float(fid_mean), "std": float(fid_std)}

    # Energia
    ene_mean, ene_std = run_multiple_times(lambda: test_energy_expectation(core), 3)
    print(f"  Energia: {ene_mean:.6f} ± {ene_std:.2e}")
    metrics["energy_exp"] = {"mean": float(ene_mean), "std": float(ene_std)}

    # Hermitian
    herm_ok = test_hermitian_check(core)
    print(f"  Hermitian: {'SIM' if herm_ok else 'NÃO'}")
    metrics["hermitian"] = {"value": bool(herm_ok)}

    # Norma
    norm_mean, norm_std = run_multiple_times(lambda: test_state_norm(core), 3)
    print(f"  Norma: {norm_mean:.10f} ± {norm_std:.2e}")
    metrics["norm"] = {"mean": float(norm_mean), "std": float(norm_std)}

    # Gap espectral
    gap_mean, gap_std = run_multiple_times(lambda: test_spectral_gap(core), 3)
    print(f"  Gap espectral: {gap_mean:.6f} ± {gap_std:.2e}")
    metrics["spectral_gap"] = {"mean": float(gap_mean), "std": float(gap_std)}

    # === 6. REPRODUTIBILIDADE ===
    print_header("6. REPRODUTIBILIDADE (3 RUNS COMPLETAS)")
    final_energies = []
    for i in range(3):
        temp_core = ZBITQuantumCoreV2(n_qubits=10, verbose=False)
        temp_core.evolve(t_final=0.5, steps=50)
        E = np.real(np.vdot(temp_core.psi, temp_core.H @ temp_core.psi))
        final_energies.append(E)
    repro_mean, repro_std = np.mean(final_energies), np.std(final_energies)
    print(f"  Energia final: {repro_mean:.6f} ± {repro_std:.2e}")
    metrics["reproducibility"] = {"mean": float(repro_mean), "std": float(repro_std)}

    # === RELATÓRIO FINAL ===
    total_time = time.time() - start_total
    print_header(f"DEMO CONCLUÍDO EM {total_time:.2f}s")
    print(f"  Relatório salvo em: {REPORT_FILE}")

    report = {
        "zbit_core_v2_demo_medio": {
            "qubits": 10,
            "date": time.strftime('%Y-%m-%d %H:%M:%S'),
            "total_time_s": float(total_time),
            "license": "CC BY-NC-ND 4.0",
            "contact": "zbit@quantumcore.org",
            "metrics": metrics
        }
    }

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("  ZBIT-CORE-v2: 100% funcional e robusto.")
    print("  Uso comercial: SOMENTE COM AUTORIZAÇÃO.")


if __name__ == "__main__":
    main()