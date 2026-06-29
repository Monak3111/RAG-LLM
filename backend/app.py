import streamlit as st

from rag import ask_ai


st.set_page_config(
    page_title="Ollama RAG Chatbot"
)


st.title("🤖 Ollama RAG Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages=[]



for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])



question = st.chat_input(
    "Ask something..."
)


if question:


    st.session_state.messages.append(
        {
        "role":"user",
        "content":question
        }
    )


    with st.chat_message("user"):
        st.write(question)



    answer = ask_ai(question)


    st.session_state.messages.append(
        {
        "role":"assistant",
        "content":answer
        }
    )


    with st.chat_message("assistant"):
        st.write(answer)