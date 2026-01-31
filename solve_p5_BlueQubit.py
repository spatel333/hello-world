from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import matplotlib.pyplot as plt 

print(">>> Problem 5 script started")

# Load circuit
qc = QuantumCircuit.from_qasm_file("P5_soft_rise.qasm")
print(f"Loaded circuit with {qc.num_qubits} qubits")

# Add measurements
qc.measure_all()

# Create MPS simulator
sim = AerSimulator(method="matrix_product_state")

#data = []

#for i in range(32,64,1):

sim.set_options(matrix_product_state_max_bond_dimension=32)

# Transpile (important for MPS)
qc_t = transpile(qc, sim, optimization_level=1)

print("Running MPS simulation...")
result = sim.run(qc_t, shots=512).result()

counts = result.get_counts()
peak = max(counts, key=counts.get)

#data.append(result)

print("=== RESULTS ===")
print("Peak bitstring:", peak)
print("Counts:", counts[peak])


