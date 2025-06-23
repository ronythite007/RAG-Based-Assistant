import os
from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq
from dotenv import load_dotenv
from .roles import get_access_filter
from .models import Response

load_dotenv()

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chroma_client.get_or_create_collection(name="company_docs")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_rag_pipeline(query: str, role: str, department: str = None) -> Response:
    try:
        query_embedding = embedding_model.encode(query).tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
            where=get_access_filter(role)
        )

        documents = results.get('documents', [[]])[0]
        metadatas = results.get('metadatas', [[]])[0]

        if not documents:
            print("⚠️ No accessible documents found.")
            return Response(answer="No accessible information found.", sources=[], role=role)

        # Combine and truncate to safe token size (~3000 tokens = ~12000 characters)
        MAX_CONTEXT_CHARS = 12000
        context = "\n\n".join(documents)
        if len(context) > MAX_CONTEXT_CHARS:
            print("✂️ Truncating context to stay under token limit.")
            context = context[:MAX_CONTEXT_CHARS]

        sources = [md.get("source", "unknown") for md in metadatas]

        prompt = (
            f"You are a helpful assistant for {department or 'the company'}.\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{query}\n\n"
            "Guidelines:\n"
            "1. Answer concisely and professionally.\n"
            "2. Use only the provided context.\n"
            "3. If unsure, say \"I don't have enough information to answer that.\"\n"
            "4. For financial data, include relevant numbers when available.\n"
            "5. For HR questions, be particularly careful with sensitive information."
        )

        llm_response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": f"You are a {role} department assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return Response(
            answer=llm_response.choices[0].message.content,
            sources=sources,
            role=role
        )

    except Exception as e:
        print("❌ run_rag_pipeline error:", str(e))
        return Response(
            answer="An internal error occurred while processing your query.",
            sources=[],
            role=role
        )
