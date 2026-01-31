from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Load the .qasm file
qc = QuantumCircuit.from_qasm_file('P2_small_bump.qasm')

# Visualize it in the terminal to confirm it works
print(qc)

# Measure to see the output 
qc.measure_all()

# Aer local simulator 
simulator = AerSimulator()
circuit_compiled = transpile(qc, simulator)

#Running on QASM simulator
p2_sim = simulator.run(circuit_compiled, shots=1024)
result = p2_sim.result()

# Get the counts (how many times each result was measured)
counts = result.get_counts()

# Find peak bitstring 
max_count_bitstring = max(counts, key=counts.get)
print(f"Most frequent bitstring is:, {max_count_bitstring}")