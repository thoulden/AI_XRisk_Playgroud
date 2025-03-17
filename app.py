import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo simulation function based on Table 1 parameters
def monte_carlo_simulation(num_simulations=10000):
    # Parameter samples
    delta0 = np.random.uniform(0, 0.02, num_simulations)  # Extinction risk, δ₀
    phi    = np.random.uniform(0, 1, num_simulations)       # Fraction of risk that can be mitigated, φ
    xi     = np.random.uniform(0, 0.99, num_simulations)    # Mitigation effectiveness, ξ
    V      = np.random.uniform(90, 270, num_simulations)     # Value of life, V = Vt+1/u'(1)
    T      = np.random.uniform(5, 20, num_simulations)       # Period length, T
    
    beta = 0.99 ** T  # Discount factor
    # Approximate optimal spending share (s) using a simplified relation:
    s = phi * delta0 * beta * V - 1 / (xi * T)
    s = np.clip(s, 0, 1)  # Limit s between 0 and 1 (0% and 100% of GDP)
    return s

def main():
    st.title("Optimal Mitigation Spending Simulation")
    st.write("""
    This simple app estimates the optimal share of GDP to spend on mitigating existential risk from AI.
    The Monte Carlo simulation draws samples from key parameter distributions and computes an approximate optimal spending share.
    """)

    num_simulations = st.number_input("Number of Simulations", min_value=1000, max_value=1000000, value=10000, step=1000)
    s_values = monte_carlo_simulation(num_simulations)

    st.subheader("Simulation Results")
    # Plot histogram of the optimal spending share
    fig, ax = plt.subplots()
    ax.hist(s_values, bins=50, edgecolor='k')
    ax.set_xlabel("Optimal Mitigation Spending Share (s)")
    ax.set_ylabel("Frequency")
    ax.set_title("Monte Carlo Simulation of Optimal Spending")
    st.pyplot(fig)

    # Display summary statistics
    st.write("Mean Optimal Spending Share:", np.mean(s_values))
    st.write("Fraction of simulations with s > 0:", np.mean(s_values > 0))

if __name__ == "__main__":
    main()
