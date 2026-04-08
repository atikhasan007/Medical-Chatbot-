# Medical Chatbot Using RAG (Flask + LangChain + Pinecone)

A **Retrieval-Augmented Generation (RAG) chatbot** that answers medical queries using vector embeddings, Pinecone, and OpenAI GPT-4. Built with **Flask** for a web interface and **LangChain** for RAG pipelines.

---

## Project Overview
This chatbot retrieves relevant medical information from a document database and generates **context-aware responses** using GPT-4. It demonstrates the use of **vector databases**, **LLMs**, and RAG pipelines in a real-world application.

---

## Business Objectives
- Provide **accurate medical responses** to user queries.  
- Demonstrate **RAG pipeline capabilities** for domain-specific chatbots.  
- Offer a **scalable and interactive web-based solution**.

---

## Data Sources
- Medical PDFs, articles, and curated text documents.  
- **Hugging Face embeddings** to convert text chunks into vector representations.  
- **Pinecone vector database** to store and retrieve embeddings efficiently.

---

## Exploratory Data Analysis (EDA)
- Documents were **cleaned** and **chunked** for embedding.  
- Checked for **duplicates** and irrelevant data.  
- Verified **embedding similarity** to ensure relevant retrieval.

---

## Models Used
- **Hugging Face embeddings** – for vectorizing text.  
- **PineconeVectorStore** – for vector storage and similarity search.  
- **GPT-4o (via LangChain)** – generates context-aware answers.  
- **RAG Chain** – integrates retrieval with generation for accurate responses.

---

## Evaluation Metrics
- **Response relevance** – qualitative assessment of correctness.  
- **Retrieval accuracy** – top-k nearest neighbors (`k=3`) for relevance.  
- **User feedback** – to improve chatbot quality over time.

---

## End-to-End Application
1. User inputs a query via Flask web interface.  
2. RAG pipeline retrieves relevant document embeddings from Pinecone.  
3. GPT-4o generates the response using the retrieved context.  
4. Response is displayed to the user in real-time.

---



# How to run ?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/atikhasan007/Medical-Chatbot-.git

```

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n medi python=3.10 -y
```

```bash
conda activate medi
```

### Step 02 - install the requirements
```bash
pip install -r requirements.txt

```

