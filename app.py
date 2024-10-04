import streamlit as st

st.write("This is a demo for calculating the time value of money")

fine = st.checkbox("Please ensure that you have realized this, click the button to confirm!")

if fine:
    st.write("Great!")

# Assumptions:

principal = st.number_input("Enter the principal amount")
st.write("The principal amount is ", principal)

rate = st.number_input("Enter the discount rate")
st.write("The discount rate is ", rate)

time = st.number_input("Enter the numbers of investment years")
st.write("The investment period (years) is ", time)

freq = st.number_input("Enter the number of compounding periods per year")
st.write("Number of compounding periods per year is ", freq)


# Print the earned amounts at the endings of each year
t = int(time)
for year in range(1, t + 1):
    principal = principal * (1 + rate / freq) ** freq
    st.write(f"Year {year}: ${principal:.2f}")