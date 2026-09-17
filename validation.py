from itertools import combinations

def _commutation_1qubit(pauli1, pauli2):
    comm_string = pauli1+pauli2
    if "I" in comm_string:
        return 1
    elif pauli1 == pauli2:
        return 1
    else:
        return -1

def _commutation(stab1, stab2):
    parity = 1
    for i in range(len(stab1[1])):
        parity = parity * _commutation_1qubit(stab1[1][i], stab2[1][i])
    return parity

def _validate_stabiliser_set(n_qubits, stabiliser_set):
    """e.g. [(1,"IXIIX"),(1j,"IXZZX")]"""
    # make sure all strings only contain pauli operators
    pauli_set = set(["I","X","Y","Z"])
    phase_set = set([1,-1])

    for stab in stabiliser_set:
        if stab[0] not in phase_set:
            raise ValueError("Stabiliser phases contain non-valid elements. Phases must contain 1 or -1.")
        for pauli in stab[1]:   
            if pauli not in pauli_set:
                raise ValueError("Stabililiser operators contain non-valid elements. Requires Pauli strings containing 'I', 'X', 'Y' or 'Z'.")
            
    # make sure strings are the right length
    for stab in stabiliser_set:
        if len(stab[1])!=n_qubits:
            raise ValueError("The stabiliser set for an n-qubit state should contain n stabiliser generators.")

    # validate that all strings commute
    pairs = combinations(stabiliser_set, 2)
    for pair in pairs:
        if _commutation(*pair) == -1:
            raise ValueError("Elements of the stabiliser group do not mutually commute.")

    # validate "I" does not appear in the multiplicative set
    # requires gaussian elimination, n^3
    return True

def _validate_operator(n_qubits, operator):
    phase_set = set([1,-1,1j,-1j])
    operator_set = set(["I","X","Y","Z","H","S"])

    # check for valid phase
    if operator[0] not in phase_set:
        raise ValueError("Stabiliser phases contain non-valid elements. Phases must contain 1, -1, 1j, -1j.")

    # if operator is cnot type operator
    if operator[1].startswith("CNOT"):
        format_op = operator[1].removeprefix("CNOT_")
        control = format_op.find("C")
        target = format_op.find("T")
        # validate length without prefix
        if len(format_op)!=n_qubits:
            raise ValueError(f"Operator must act on the same number of qubits as the register, {n_qubits}.")

        # if control or target cannot be found raise error
        if control == -1:
            raise ValueError("Unable to identify control qubit in CNOT operator")
        elif target == -1:
            raise ValueError("Unable to identify target qubit in CNOT operator")

        # build the remaining string, without the control or target entries. This should be purely identities.
        remainder = ""
        expected = "I"*(n_qubits-2)
        for i in range(n_qubits):
            if i != control and i != target:
                remainder += format_op[i]
        if remainder != expected:
            raise ValueError("CNOT operators should be composed only of a control, 'C' and a target 'T'. The operation on all other qubits should be 'I'.")

    # if not cnot type, check length directly, and validate string entries
    else: 
        if len(operator[1])!=n_qubits:
            raise ValueError(f"Operator must act on the same number of qubits as the register, {n_qubits}.")
        
        for i in operator[1]:
            if i not in operator_set:
                raise ValueError(["Operators must be Cliffords, with strings containing 'I','X','Y','Z','H' or 'S' only."])


def _validate_basis(basis):
    pass
