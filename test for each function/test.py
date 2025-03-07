import numpy as np

def energy(state, J):
    """
    Calculate the energy of the Ising model given a state and coupling constant J.
    """
    energy = 0
    for i in range(len(state)):
        for j in range(len(state)):
            energy += -J * state[i] * state[j]
    return energy

def ising_ground_state(N, J):
    """
    Find the ground state of the Ising model with N spins and coupling constant J.
    """
    # Generate all possible spin configurations
    configs = np.array(np.meshgrid(*[[1, -1]] * N)).T.reshape(-1, N)

    min_energy = float('inf')
    ground_state = None

    # Iterate over all configurations to find the one with minimum energy
    for config in configs:
        config_energy = energy(config, J)
        if config_energy < min_energy:
            min_energy = config_energy
            ground_state = config

    return ground_state, min_energy

# Example usage
N = 32  # Number of spins
J = 1  # Coupling constant
ground_state, min_energy = ising_ground_state(N, J)
print("Ground state:", ground_state)
print("Minimum energy:", min_energy)
