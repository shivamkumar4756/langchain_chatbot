import os
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INDEX_PATH = "faiss_index"

def initialize_chatbot():
    vector_db = FAISS.load_local(INDEX_PATH, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))
    return ConversationalRetrievalChain.from_llm(OpenAI(), vector_db.as_retriever())
