dimport streamlit as st

def fare(d):
    book = 3.30  # Booking fee
    start = 4.6  # Starting fee
    cost = 0.29  # Cost per distance unit
    fare = book + start + d * cost
    return fare

# Streamlit application
st.title("Fare Calculator")

# Input for distance
d = st.number_input("What is the distance (in units)?", min_value=0.0, step=0.1)

# Calculate and display fare
if st.button("Calculate Fare"):
    calculated_fare = fare(d)
    st.success(f"Based on the assumption that booking fee is $3.30 and the starting fare of $4.60, the estimated calculated fare is: ${calculated_fare:.2f}")
