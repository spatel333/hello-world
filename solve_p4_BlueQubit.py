from qiskit import QuantumCircuit, transpile
import bluequbit
from qiskit_aer import AerSimulator
import numpy as np

#import os
#os.environ['BLUEQUBIT_EXECUTION_MODE']= 'cloud'

# Bluequbit client setup
bq = bluequbit.init("Xo3SG0t3Jy1vY4mWBloqXzKSgyqqecMR") #Utilize API key in the parantheses

# Load the .qasm file
qc = QuantumCircuit.from_qasm_file('P4_gentle_mound.qasm')

# Transpile the circuit to BlueQubit 
result = bq.run(qc, job_name = "Gentle Mound Challenge",device = 'mps.cpu')

# Use MPS (Matrix Product State)
simulator = AerSimulator(method='matrix_product_state')
qc = transpile(qc, simulator)   

# Obtain the MPS States and store them somewhere
p4_sim = simulator.run(qc,shots = 1024)
result = p4_sim.result()

# Find the highest probability outcome
probabilities = np.abs(result)**2
max_index = np.argmax(probabilities)

# Convert index to binary string
highest_prob_bitstring = format(max_index,"040b") # We want a 30-bit string output
