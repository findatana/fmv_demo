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
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Year {year}")
    with col2:
        st.write(f"${principal:.2f}")
    with col3:
        if principal < 1000000:
            st.write("You are not a millionair")
        else:
            st.write("You become a dollar millionair")
