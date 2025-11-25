import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import DensityMatrix, entropy, partial_trace
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

class ETGEngine:
    """
    Core simulation engine for the Entanglement Tabletop Gravity (ETG) project.
    Handles quantum circuit generation, state simulation, and entropy calculation.
    """

    def __init__(self, use_noise=False, noise_prob=0.05):
        """
        Initialize the engine.
        
        Args:
            use_noise (bool): If True, applies a noise model to the simulation.
            noise_prob (float): Probability of depolarizing error if noise is enabled.
        """
        self.use_noise = use_noise
        self.noise_prob = noise_prob
        self.simulator = AerSimulator()
        self.noise_model = None
        
        if self.use_noise:
            self._setup_noise_model()

    def _setup_noise_model(self):
        """Configures a basic depolarizing noise model."""
        self.noise_model = NoiseModel()
        # Add depolarizing error to all 1-qubit gates
        error_1 = depolarizing_error(self.noise_prob, 1)
        self.noise_model.add_all_qubit_quantum_error(error_1, ['ry', 'u1', 'u2', 'u3'])
        # Add depolarizing error to CNOT
        error_2 = depolarizing_error(self.noise_prob, 2)
        self.noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

    def create_circuit(self, theta):
        """
        Creates a 2-qubit circuit representing the Alice-Bob system.
        
        Args:
            theta (float): Parameter controlling the degree of entanglement.
                           0 = Separable state |00>
                           pi/2 = Maximally entangled Bell state (|00> + |11>)/sqrt(2)
        
        Returns:
            QuantumCircuit: The prepared quantum circuit.
        """
        qc = QuantumCircuit(2)
        
        # Apply rotation on Qubit 0 (Alice)
        qc.ry(theta, 0)
        
        # Apply CNOT to entangle Qubit 0 with Qubit 1 (Bob)
        qc.cx(0, 1)
        
        return qc

    def simulate_state(self, theta):
        """
        Simulates the circuit and returns the density matrix of the system.
        
        Args:
            theta (float): Entanglement parameter.
            
        Returns:
            DensityMatrix: The density matrix of the final state.
        """
        qc = self.create_circuit(theta)
        qc.save_density_matrix()
        
        # Run simulation
        if self.use_noise:
            result = self.simulator.run(qc, noise_model=self.noise_model).result()
        else:
            result = self.simulator.run(qc).result()
            
        rho = result.data(0)['density_matrix']
        return rho

    def calculate_entropy(self, theta):
        """
        Calculates the Von Neumann Entropy for Subsystem A (Alice).
        S = -Tr(rho_A * ln(rho_A))
        
        Args:
            theta (float): Entanglement parameter.
            
        Returns:
            float: The calculated entropy value.
        """
        # Get the full system density matrix
        rho_AB = self.simulate_state(theta)
        
        # Trace out Bob (qubit 1) to get Alice's reduced density matrix (qubit 0)
        # qiskit.quantum_info.partial_trace takes list of qubits to TRACE OUT
        rho_A = partial_trace(rho_AB, [1])
        
        # Calculate Von Neumann entropy (base e by default, can be base 2)
        # Using base 2 for bits
        S = entropy(rho_A, base=2)
        
        return S

if __name__ == "__main__":
    # Quick test
    engine = ETGEngine(use_noise=False)
    print("Testing ETG Engine...")
    
    test_thetas = [0, np.pi/4, np.pi/2]
    for t in test_thetas:
        s = engine.calculate_entropy(t)
        print(f"Theta: {t:.2f}, Entropy: {s:.4f}")
