import streamlit as st

st.set_page_config(page_title="TDS Calculator", page_icon="💰", layout="centered")

st.title("💰 TDS Calculator")
st.write("Calculate Tax Deducted at Source (TDS) based on income and TDS rate.")

income = st.number_input("Enter Income Amount (₹)", min_value=0.0, step=100.0)
tds_rate = st.number_input("Enter TDS Rate (%)", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Calculate TDS"):
    if income > 0 and tds_rate > 0:
        tds_amount = (income * tds_rate) / 100
        net_income = income - tds_amount

        st.success(f"TDS Amount: ₹ {tds_amount:,.2f}")
        st.info(f"Net Income after TDS: ₹ {net_income:,.2f}")
    else:
        st.warning("Please enter valid income and TDS rate.")
