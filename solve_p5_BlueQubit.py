from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
# import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram
from collections import Counter

print(">>> Problem 5 script started")

# Load circuit
qc = QuantumCircuit.from_qasm_file("P5_soft_rise.qasm")
print(f"Loaded circuit with {qc.num_qubits} qubits")

# Add measurements
qc.measure_all()

# Create MPS simulator
sim = AerSimulator(method="matrix_product_state")




### Testing Iterations

data = []
total_counts = Counter()

for i in range(32,64,1):                            # BOND DIMENSIONS  

    ### --- we in the loop! --- ###
    
    # Set the bond dimension
    sim.set_options(matrix_product_state_max_bond_dimension=i)
    # Transpile (important for MPS)
    qc_t = transpile(qc, sim, optimization_level=1)

    for o in range(10):                             # 10 TRIALS       
        ### --- we in the inner loop! --- ###
        print("Running MPS simulation...")
        print("\tBond Dim:\t{i}")
        print("\tTrial:\t{o}")
        
        result = sim.run(qc_t, shots=512).result()
        counts = result.get_counts()
        data.append(counts)


        # peak = max(counts, key=counts.get)

        # print("=== RESULTS ===")
        # print("Peak bitstring:", peak)
        # print("Counts:", counts[peak])

for trial_counts in data:
    total_counts.update(trial_counts)

# Plotting the last result
filtered_counts = {k: v for k, v in total_counts.items() if v > 100}
plot_histogram(total_counts, title="MPS Simulation Bitstring Distribution", bar_labels=False)

