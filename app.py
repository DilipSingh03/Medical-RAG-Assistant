import streamlit as st
from connect_memory_llm import get_answer

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_answer(prompt)
            st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )