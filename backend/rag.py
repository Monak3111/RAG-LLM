from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import Chroma


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


db = Chroma(
    persist_directory="database",
    embedding_function=embeddings
)


retriever = db.as_retriever(
    search_kwargs={
        "k":3
    }
)


from langchain_ollama import ChatOllama
import os


llm = ChatOllama(
 model="llama3.1",
 temperature=0,
 base_url=os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
 )
)


def ask_ai(question):

    docs = retriever.invoke(question)


    context = "\n\n".join(
        d.page_content for d in docs
    )


    prompt = f"""

You are a helpful AI assistant.

Answer only using the context.

Context:

{context}


Question:

{question}

"""


    response = llm.invoke(prompt)

    return response.content