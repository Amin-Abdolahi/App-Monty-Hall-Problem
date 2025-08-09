from __future__ import annotations
import streamlit as st
import time
from monty_hall import monty_hall_gui


st.title("Monty Hall Problem Simulation")

st.write("Welcome to the Monty Hall Problem simulation!")

st.sidebar.header("User Input", divider=True)

change_door = st.sidebar.checkbox("Change Door", value=True)
num_simulations = st.sidebar.number_input("Number of Simulations", min_value=1, value=100, step=100)

st.sidebar.header("About", divider=True)
st.sidebar.info("This simulation demonstrates the Monty Hall problem, a probability puzzle based on a game show scenario.")

chart = st.line_chart(x=None, y=None, width=700, height=400,x_label="Number of Simulations", y_label="Win Rate (%)")

if st.button("Run Simulation"):
    Win_Rate = 0
    st.write(f"Change Door: {"on" if change_door else "off"}")

    for i in range(num_simulations):
        results = monty_hall_gui(i+1, change_door)
        Win_Rate += results[0] / (results[0] + results[1]) * 100
        chart.add_rows([Win_Rate/(i+1)])
        time.sleep(0.08)
    st.write(f"Final Win Rate: {Win_Rate / num_simulations : .2f} %")

    

