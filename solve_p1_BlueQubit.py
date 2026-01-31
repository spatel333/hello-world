from qiskit import QuantumCircuit

# Load the cleaned .qasm file
qc = QuantumCircuit.from_qasm_file('P1_little_peak.qasm')

# Visualize it in the terminal to confirm it works
print(qc)