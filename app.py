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
    s = np.clip(s, 0, 1)  # Limit s between 0 and 1 (0% to 100% of GDP)
    return s

# Page 1: Optimal Risk Mitigation using Monte Carlo simulation
def optimal_risk_mitigation():
    st.title("Optimal Risk Mitigation")
    st.write("""
    This page estimates the optimal share of GDP to spend on mitigating existential risk from AI.
    The Monte Carlo simulation draws samples from key parameter distributions and computes an 
    approximate optimal spending share.
    """)
    
    num_simulations = st.number_input("Number of Simulations", min_value=1000, max_value=1000000,
                                      value=10000, step=1000)
    s_values = monte_carlo_simulation(num_simulations)
    
    st.subheader("Simulation Results")
    fig, ax = plt.subplots()
    ax.hist(s_values, bins=50, edgecolor='k')
    ax.set_xlabel("Optimal Mitigation Spending Share (s)")
    ax.set_ylabel("Frequency")
    ax.set_title("Monte Carlo Simulation of Optimal Spending")
    st.pyplot(fig)
    
    st.write("Mean Optimal Spending Share:", np.mean(s_values))
    st.write("Fraction of simulations with s > 0:", np.mean(s_values > 0))

# Page 2: AI vs Growth – Expected Payoff
def ai_vs_growth():
    st.title("AI vs Growth")
    st.write("""
    This page explores the trade-off between AI-induced growth and existential risk.
    Here we assume per-capita income yₜ = 1, so that consumption is c = 1 − x, and we model 
    the expected payoff as the sum of utility and a discounted benefit from risk reduction.
    """)
    # Baseline parameters for the payoff model
    delta0 = 0.01    # Baseline extinction risk
    phi    = 0.5     # Fraction of risk that can be mitigated
    xi     = 0.5     # Mitigation effectiveness
    T      = 10      # Period length (years)
    beta   = 0.99 ** T  # Discount factor
    V      = 180     # Value of life (relative to annual consumption)
    alpha  = xi * T  # Effectiveness parameter (baseline: 5)
    
    # Define range for mitigation spending share x (we avoid the endpoints to prevent log issues)
    x = np.linspace(0.001, 0.99, 1000)
    c = 1 - x  # Consumption, given yₜ = 1
    
    # Extinction risk function: δ(x) = (1 − φ)*δ₀ + φ*δ₀*exp(−α*x)
    delta_x = (1 - phi) * delta0 + phi * delta0 * np.exp(-alpha * x)
    
    # Utility function: u(c) = ln(c)
    u_c = np.log(c)
    
    # Expected payoff: current utility plus discounted benefit from risk reduction
    payoff = u_c + (1 - delta_x) * beta * V
    
    fig, ax = plt.subplots()
    ax.plot(x, payoff, linewidth=2)
    ax.set_xlabel("Mitigation Spending Share, x")
    ax.set_ylabel("Expected Payoff")
    ax.set_title("Expected Payoff vs. Mitigation Spending Share")
    st.pyplot(fig)
    
    st.write("This plot shows the trade-off between consumption (1−x) and the discounted benefit of reducing risk.")

# Main app with navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Optimal Risk Mitigation", "AI vs Growth"))
    
    if page == "Optimal Risk Mitigation":
        optimal_risk_mitigation()
    elif page == "AI vs Growth":
        ai_vs_growth()

if __name__ == "__main__":
    main()

