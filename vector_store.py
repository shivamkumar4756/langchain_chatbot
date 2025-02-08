import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings 
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INDEX_PATH = "faiss_index"

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_db = FAISS.from_documents(docs, embeddings)
    vector_db.save_local(INDEX_PATH)
    return vector_db


