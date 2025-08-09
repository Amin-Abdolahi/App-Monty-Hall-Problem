import streamlit as st
from monty_hall import monty_hall_gui


st.title("Monty Hall Problem Simulation")

st.write("Welcome to the Monty Hall Problem simulation!")

st.sidebar.header("User Input")
change_door = st.sidebar.checkbox("Change Door", value=True)
num_simulations = st.sidebar.number_input("Number of Simulations", min_value=1, value=1000)

if st.button("Run Simulation"):
    results = monty_hall_gui(num_simulations, change_door)
    st.write("Simulation Results:")
    st.write(f"Win Rate: {results[0] / (results[0] + results[1]) * 100:.2f}%")
    st.write(f"Loss Rate: {results[1] / (results[0] + results[1]) * 100:.2f}%")
