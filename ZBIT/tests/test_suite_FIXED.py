"""
ZBIT-CORE-v2 Test Suite
All 9 validation tests + unit tests
"""
import sys
import os
import unittest
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import ZBIT Core
try:
    from zbit_core_v2_FIXED import ZBITQuantumCoreV2
    print("✅ Successfully imported ZBITQuantumCoreV2")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)


class TestZBITCoreV2(unittest.TestCase):
    """Complete test suite for ZBIT-CORE-v2"""
    
    def setUp(self):
        """Setup before each test"""
        self.core = ZBITQuantumCoreV2(n_qubits=6, verbose=False)
    
    def test_01_initialization(self):
        """TEST 1: Core initialization"""
        print("\n✅ TEST 1: Initialization")
        self.assertEqual(self.core.n_qubits, 6)
        self.assertEqual(len(self.core.psi), 64)
        self.assertEqual(self.core.reliability, "HIGH")
        print("   PASS")
    
    def test_02_hamiltonian_hermitian(self):
        """TEST 2: Hamiltonian is Hermitian"""
        print("✅ TEST 2: Hamiltonian Hermitian")
        H_diff = np.linalg.norm(self.core.H - self.core.H.conj().T)
        self.assertAlmostEqual(H_diff, 0.0, places=10)
        print("   PASS")
    
    def test_03_state_normalized(self):
        """TEST 3: State is normalized"""
        print("✅ TEST 3: State Normalized")
        norm = np.linalg.norm(self.core.psi)
        self.assertAlmostEqual(norm, 1.0, places=10)
        print("   PASS")
    
    def test_04_validation_suite(self):
        """TEST 4: Validation suite returns 9/9"""
        print("✅ TEST 4: Validation Suite")
        report = self.core.run_validation_suite()
        self.assertEqual(report["passed"], 9)
        print("   PASS")
    
    def test_05_evolution(self):
        """TEST 5: State evolution"""
        print("✅ TEST 5: State Evolution")
        core_small = ZBITQuantumCoreV2(n_qubits=4, verbose=False)
        psi_evolved = core_small.evolve(t_final=0.5, steps=10)
        norm = np.linalg.norm(psi_evolved)
        self.assertAlmostEqual(norm, 1.0, places=10)
        print("   PASS")
    
    def test_06_otoc(self):
        """TEST 6: OTOC computation"""
        print("✅ TEST 6: OTOC Computation")
        otoc_result = self.core.otoc(t_max=1.0, num_times=5)
        self.assertEqual(len(otoc_result["times"]), 5)
        print("   PASS")
    
    def test_07_arxiv_report(self):
        """TEST 7: arXiv report"""
        print("✅ TEST 7: arXiv Report")
        report = self.core.generate_arxiv_report()
        self.assertEqual(report["status"], "PRODUCTION READY")
        print("   PASS")
    
    def test_08_energy_tracking(self):
        """TEST 8: Energy tracking"""
        print("✅ TEST 8: Energy Tracking")
        core_small = ZBITQuantumCoreV2(n_qubits=4, verbose=False)
        core_small.evolve(t_final=0.1, steps=5)
        self.assertGreater(len(core_small.history["energy"]), 0)
        print("   PASS")
    
    def test_09_reliability(self):
        """TEST 9: Reliability scaling"""
        print("✅ TEST 9: Reliability Scaling")
        core_small = ZBITQuantumCoreV2(n_qubits=6, verbose=False)
        self.assertEqual(core_small.reliability, "HIGH")
        print("   PASS")


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 ZBIT-CORE-v2 TEST SUITE")
    print("="*60)
    
    unittest.main(verbosity=2)
