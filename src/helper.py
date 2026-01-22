# ---------------- PDF Loader ---------------- #
from langchain_community.document_loaders import PyPDFLoader
from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Extract data from the PDF file
def load_pdf_file(path: str) -> List[Document]:
    """
    Load PDF and return list of Document objects
    """
    loader = PyPDFLoader(path)
    documents = loader.load()
    return documents


# Filter to minimal docs (only source + content)
def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects
    containing only 'source' in metadata and the original page_content.
    """
    minimal_docs: List[Document] = []

    for doc in docs:
        src = doc.metadata.get("source", None)
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs


# Split the Data into Text Chunks
def text_split(minimal_docs: List[Document]) -> List[Document]:
    """
    Split documents into smaller chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks = text_splitter.split_documents(minimal_docs)
    return text_chunks


# Download the embeddings from HuggingFace
def download_hugging_face_embeddings() -> HuggingFaceEmbeddings:
    """
    Download and return Hugging Face embedding model
    """
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embedding


# Load embeddings
embeddings = download_hugging_face_embeddings()
print("Embeddings loaded successfully ✅")
