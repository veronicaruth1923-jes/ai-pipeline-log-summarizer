import streamlit as st

st.title("AI Pipeline Log Summarizer")

log_input = st.text_area("Paste Pipeline Logs")

if st.button("Summarize"):
    st.subheader("AI Summary")
    
    st.write("""
    Pipeline execution failed due to a schema mismatch 
    in the customer_orders table.

    Recommended Action:
    Validate source schema and update ingestion mappings.

    Severity: Medium
    """)
