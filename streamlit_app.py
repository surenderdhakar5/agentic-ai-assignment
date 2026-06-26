import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support Agent")

st.write("Ask any question about your order or products.")

question = st.text_input("Your Question")

if st.button("Submit"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        answer = run_agent(question)

        st.success(answer)