# ingest/run_ingest.py
import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import glob

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chroma_client.get_or_create_collection(name="company_docs")

def ingest_documents():
    base_path = "data/"
    doc_id = 0

    access_mapping = {
        "finance": {"department": "finance"},
        "marketing": {"department": "marketing"},
        "hr": {"department": "hr"},
        "engineering": {"department": "engineering"},
        "general": {"access_level": "general"}
    }

    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            for file in glob.glob(f"{folder_path}/*.md"):
                with open(file, "r", encoding="utf-8") as f:
                    text = f.read()

                embedding = embedding_model.encode(text).tolist()
                metadata = access_mapping.get(folder, {})
                metadata["source"] = os.path.basename(file)

                collection.add(
                    documents=[text],
                    embeddings=[embedding],
                    metadatas=[metadata],
                    ids=[f"doc_{doc_id}"]
                )
                doc_id += 1

    print(f"✅ Ingested {doc_id} documents")

if __name__ == "__main__":
    ingest_documents()
