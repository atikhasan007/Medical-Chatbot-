from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore


load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# -------- Load & Process PDF --------
extracted_data = load_pdf_file("data/Medical_book.pdf")
minimal_docs = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(minimal_docs)


# -------- Embeddings --------
embeddings = download_hugging_face_embeddings()


# -------- Pinecone --------
index_name = "medi-bot"

pc = Pinecone(api_key=PINECONE_API_KEY)

if index_name not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)


# -------- Store in Pinecone --------
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print("Data stored in Pinecone successfully ✅")
