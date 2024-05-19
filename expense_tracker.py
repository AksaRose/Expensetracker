import streamlit as st
import pandas as pd

st.title("Expense Tracker")
st.write("where tracking your expenses made easy")

expense_desc = st.text_input("Description")
expense_amount = st.number_input("Amount",min_value=0.0,format = "%.2f")
expense_cat = st.selectbox("Category",["Food","Transport","Mess fee","groccery","LBS society","miscellaneous"])
expense_date = st.date_input("Date")

if st.button("Add Expense"):
    if expense_amount and expense_desc:
        new_expense = {
            "Description" : expense_desc,
            "Amount": expense_amount,
            "Category" : expense_cat,
            "Date": expense_date
            }
        if "expenses" not in st.session_state:
            st.session_state.expenses =[]
        st.session_state.expenses.append(new_expense)
        st.success("Expense added succesfully!")
    else:
        st.error("Pleae enter valid description and amount.")    
    

st.header("Expenses")
if "expenses" in st.session_state and st.session_state.expenses:
    expense_df = pd.DataFrame(st.session_state.expenses)
    st.table(expense_df)

    total_expense = expense_df["Amount"].sum()
    st.write(f"**Total Expense:** {total_expense:.2f}")

    expense_by_cat = expense_df.groupby("Category")["Amount"].sum().reset_index()
    st.bar_chart(expense_by_cat.set_index("Category"))

else:
    st.write("No expenses yet.")

    