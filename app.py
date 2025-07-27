import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("Interior Quotation Software")

# Initialize session state
if "quotation" not in st.session_state:
    st.session_state.quotation = []

# Input form
with st.form("add_item_form"):
    item_name = st.text_input("Item Name")
    sqft = st.number_input("Sqft", min_value=0.0, format="%.2f")
    rate = st.number_input("Sqft Rate", min_value=0.0, format="%.2f")
    amount = sqft * rate
    st.write(f"**Amount:** ₹ {amount:.2f}")
    submitted = st.form_submit_button("Add Item")
    if submitted:
        st.session_state.quotation.append({
            "Sl No": len(st.session_state.quotation) + 1,
            "Item Name": item_name,
            "Sqft": sqft,
            "Sqft Rate": rate,
            "Amount": round(amount, 2)
        })

# Display table
if st.session_state.quotation:
    df = pd.DataFrame(st.session_state.quotation)
    st.table(df)

# Save to Excel
if st.button("Submit Quotation"):
    if not st.session_state.quotation:
        st.warning("Add at least one item before submitting.")
    else:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Quotation_{now}.xlsx"
        df = pd.DataFrame(st.session_state.quotation)
        df.to_excel(filename, index=False)
        st.success(f"Quotation saved as `{filename}`")
        st.session_state.quotation.clear()
