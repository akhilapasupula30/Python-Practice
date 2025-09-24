import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Personal Finance Tracker", page_icon="💰", layout="centered")

st.title("💰 Personal Finance Tracker")

# Initialize session state
if "transactions" not in st.session_state:
    st.session_state["transactions"] = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

# Input form
st.subheader("Add New Transaction")
with st.form("transaction_form"):
    date = st.date_input("Date", datetime.date.today())
    category = st.selectbox("Category", ["Income", "Food", "Transport", "Bills", "Entertainment", "Other"])
    description = st.text_input("Description")
    amount = st.number_input("Amount", step=0.01, format="%.2f")
    submitted = st.form_submit_button("Add Transaction")
    
    if submitted:
        new_transaction = {"Date": date, "Category": category, "Description": description, "Amount": amount}
        st.session_state["transactions"] = pd.concat(
            [st.session_state["transactions"], pd.DataFrame([new_transaction])],
            ignore_index=True
        )
        st.success("Transaction added!")

# Display transactions
st.subheader("Transaction History")
if not st.session_state["transactions"].empty:
    st.dataframe(st.session_state["transactions"], use_container_width=True)
    
    # Summary
    st.subheader("Summary")
    total_income = st.session_state["transactions"].loc[st.session_state["transactions"]["Category"]=="Income", "Amount"].sum()
    total_expense = st.session_state["transactions"].loc[st.session_state["transactions"]["Category"]!="Income", "Amount"].sum()
    balance = total_income - total_expense
    
    st.metric("Total Income", f"₹{total_income:.2f}")
    st.metric("Total Expense", f"₹{total_expense:.2f}")
    st.metric("Balance", f"₹{balance:.2f}")
    
    # Category-wise chart
    st.subheader("Expenses by Category")
    expense_data = st.session_state["transactions"][st.session_state["transactions"]["Category"]!="Income"]
    if not expense_data.empty:
        st.bar_chart(expense_data.groupby("Category")["Amount"].sum())
else:
    st.info("No transactions added yet.")
