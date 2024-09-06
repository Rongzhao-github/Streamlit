import streamlit as st

def fare(d):
    book = 2.0  # Booking fee
    start = 3.0  # Starting fee
    cost = 1.0  # Cost per distance unit
    fare = book + start + d * cost
    return fare

# Streamlit application
st.title("Fare Calculator")

# Input for distance
d = st.number_input("What is the distance (in units)?", min_value=0.0, step=0.1)

# Calculate and display fare
if st.button("Calculate Fare"):
    calculated_fare = fare(d)
    st.success(f"The calculated fare is: ${calculated_fare:.2f}")
