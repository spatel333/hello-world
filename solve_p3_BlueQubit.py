from qiskit import QuantumCircuit, transpile
import bluequbit
from qiskit_aer import AerSimulator
import numpy as np
import os

os.environ['BLUEQUBIT_EXECUTION_MODE']= 'cloud'
# Bluequbit client setup
bq = bluequbit.init("Xo3SG0t3Jy1vY4mWBloqXzKSgyqqecMR") #Utilize API key in the parantheses

# Load the .qasm file
qc = QuantumCircuit.from_qasm_file('P3_tiny_ripple.qasm')

# Transpile the circuit to BlueQubit 
result = bq.run(qc, job_name = "Tiny Ripple Challenge")

# Obtain statevector 
statevector = result.get_statevector()

# Find the highest probability outcome
probabilities = np.abs(statevector)**2
max_index = np.argmax(probabilities)

# Convert index to binary string
highest_prob_bitstring = format(max_index,"030b") # We want a 30-bit string output

print(f"Highest probability bitstring: {highest_prob_bitstring}")