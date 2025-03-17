import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Section Functions ---

def show_abstract():
    st.header("Abstract")
    st.write("""
    **How Much Should We Spend to Reduce A.I.'s Existential Risk?**

    *(Insert the paper’s abstract here.)*
    """)

def show_introduction():
    st.header("Introduction")
    st.write("""
    *(Insert the introduction text here, outlining the motivation behind mitigating A.I. risk, the Covid-19 analogy, etc.)*
    """)

def show_model():
    st.header("The Model")
    st.write("""
    This section outlines the representative agent’s decision problem and the key equations.
    
    **Key Components:**
    - The utility from consumption, *u(c)*.
    - Mitigation spending *x* versus consumption tradeoffs.
    - The extinction risk function *δ(x)*.
    
    *(Insert more detailed explanation as needed.)*
    """)
    
    st.subheader("Placeholder for Equations")
    eq1 = st.text_area("Equation 1 (e.g., First Order Condition)", value="u'(c) = -δ'(x) β V")
    st.write("You entered:")
    st.latex(eq1)  # This will render LaTeX if you input proper LaTeX syntax

def show_calibration():
    st.header("Calibration")
    st.write("""
    Here we calibrate the model parameters.
    
    **Parameters include:**
    - Baseline extinction risk, δ₀
    - Fraction of risk that can be mitigated, φ
    - Mitigation effectiveness, ξ
    - Value of life (VSL) and other economic variables
    
    *(Provide explanation and context for each parameter.)*
    """)
    
    st.subheader("Input Calibration Parameters")
    delta0 = st.number_input("Extinction Risk, δ₀ (%)", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
    phi = st.number_input("Fraction Mitigated, φ", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
    xi = st.number_input("Mitigation Effectiveness, ξ", min_value=0.0, max_value=0.99, value=0.5, step=0.05)
    
    st.write("Selected Parameters:")
    st.write(f"δ₀: {delta0}%, φ: {phi}, ξ: {xi}")

def show_results():
    st.header("Numerical Results")
    st.write("""
    This section presents numerical solutions and graphs based on the model.
    
    *(Insert explanations for the numerical results and any graphs you generate.)*
    """)
    
    # Example interactive plot (placeholder)
    if st.checkbox("Show Example Plot"):
        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title("Example Plot")
        st.pyplot(fig)

def show_montecarlo():
    st.header("Monte Carlo Simulations")
    st.write("""
    This section illustrates Monte Carlo simulations to assess the robustness of optimal spending.
    
    **Simulation Setup:**
    - Number of simulations
    - Distributions for δ₀, φ, ξ, and the value of life
    
    *(Provide detailed explanation and interactive inputs as needed.)*
    """)
    
    num_simulations = st.number_input("Number of Simulations", min_value=1000, max_value=1000000, value=10000, step=1000)
    st.write("Number of simulations selected:", num_simulations)
    
    if st.button("Run Simulation (Placeholder)"):
        st.write("Simulation running... (this is a placeholder)")
        # You can later add code to run the simulation and display the results.

def show_conclusion():
    st.header("Conclusion")
    st.write("""
    *(Insert the conclusion text here, summarizing the key insights regarding optimal mitigation spending.)*
    """)

def show_about():
    st.header("About")
    st.write("""
    **Reducing A.I.'s Existential Risk: Streamlit App**

    This app is based on the paper *"How Much Should We Spend to Reduce A.I.'s Existential Risk?"* by Charles I. Jones.
    
    The purpose is to explore the model and conduct simulations. You can adjust parameters, 
    input equations, and visualize numerical results interactively.
    """)

# --- Main App Navigation ---

def main():
    st.title("Reducing A.I.'s Existential Risk")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", 
        ("Abstract", "Introduction", "Model", "Calibration", "Results", "Monte Carlo", "Conclusion", "About"))
    
    if page == "Abstract":
        show_abstract()
    elif page == "Introduction":
        show_introduction()
    elif page == "Model":
        show_model()
    elif page == "Calibration":
        show_calibration()
    elif page == "Results":
        show_results()
    elif page == "Monte Carlo":
        show_montecarlo()
    elif page == "Conclusion":
        show_conclusion()
    elif page == "About":
        show_about()

if __name__ == "__main__":
    main()
