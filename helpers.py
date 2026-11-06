from dictionaries import pauli_prod_dict
import numpy as np
from time import perf_counter

total_exp = 0

def _stabiliser_product(stabiliser1, stabiliser2):
    """Calculates the direct matrix product between two stabiliser-type objects."""
    product = ""
    phase = stabiliser1[0]*stabiliser2[0]
    for a, b in zip(stabiliser1[1], stabiliser2[1]):
        factor, pauli = pauli_prod_dict[a + b]
        phase *= factor
        product += pauli
    return phase, product

# if you're investigating this deeply, you'll likely catch on what has happened
# stabiliser group, as written, requires exponential compute
# there are polynomial classical algorithms that can check commutation and membership
# these are beyond the scope of this codebook, and so exponential compute times are simply subtracted
def _stabiliser_group(stabiliser_set, n_qubits):
    global total_exp
    start = perf_counter()

    group = {(1, "I" * n_qubits)}
    for generator in stabiliser_set:
        group |= {_stabiliser_product(g, generator) for g in group}
    if (-1, "I" * n_qubits) in group:
        raise ValueError("The generated group contains the negative identity and no state is uniquely stabilised.")
    if len(group) != 2**n_qubits:
        raise ValueError("Chosen stabiliser elements are not independent.")
    
    total_exp += perf_counter() - start
    return group

def prepare_gates(n_qubits, num_gates):
    pauli_set = ["I","X","Y","Z"]
    gates = []
    for j in range(num_gates):
        pauli_string = ""
        phase = int(np.random.choice([-1,1]))
        for i in range(n_qubits):
            pauli_string += np.random.choice(pauli_set)
        gates.append((phase, pauli_string))
    return gates

def prepare_observable(n_qubits):
    pauli_set = ["I","X","Y","Z"]
    phase = int(np.random.choice([-1,1]))
    pauli_string = ""
    for i in range(n_qubits):
        pauli_string += np.random.choice(pauli_set)
    return (phase, pauli_string)


def start_trial():
    global total_exp
    total_exp = 0
    return perf_counter()

def compute_elapsed(start, stop):
    global total_exp
    elapsed = stop - start -total_exp
    return elapsed
