import streamlit as st

st.title("Pharmacy Manager 💊")

# 1. Ask the user for the drug name
name = st.text_input("Enter Drug Name:")

# 2. Ask the user for the quantity
count = st.number_input("Enter Current Stock:", step=1)

# 3. Create a button to run the check
if st.button("Run Safety Check"):
    if count < 10:
        st.warning(f"Alert: {name} is low on stock!")
    else:
        st.success(f"{name} stock level is healthy.")