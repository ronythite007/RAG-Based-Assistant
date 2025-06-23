# app/api.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.auth import authenticate_user, create_token, get_current_user
from app.models import Query, Response, User
from app.rag import run_rag_pipeline

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    user = authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_token(user)
    return {"access_token": token}

@router.post("/query", response_model=Response)
async def query_rag(query: Query, current_user: User = Depends(get_current_user)):
    try:
        print("\n🔍 Incoming Query:", query.text)
        print("👤 Role:", current_user.role.value)
        print("🏢 Department:", current_user.department)

        result = run_rag_pipeline(query.text, current_user.role.value, current_user.department)

        if not result or not result.answer.strip():
            print("⚠️ Empty or missing result from run_rag_pipeline")
            return Response(
                answer="No content found for your query or access level.",
                sources=[],
                role=current_user.role.value
            )

        print("✅ Result Answer:", result.answer)
        print("📁 Sources:", result.sources)
        return result

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("❌ Internal Server Error:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error. Please check logs.")
