from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.answer_analyzer import analyze_text_with_gpt, generate_follow_up, clean_text

router = APIRouter()

class AnswerRequest(BaseModel):
    question: str
    answer: str

class FollowUpRequest(BaseModel):
    question: str
    answer: str

@router.post("/answers/{answerId}/feedback")
async def analyze_answer(request: AnswerRequest):
    job_role = '개발자'
    try:
        cleaned_answer = clean_text(request.answer)
        analysis_result = analyze_text_with_gpt(cleaned_answer, request.question, job_role)

        final_result = {
            "original_answer": request.answer,
            "analysis_result": analysis_result,
        }

        return final_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.post("/answers/{answerId}/feedback")
# async def analyze_answer_api(answerId: int, request: AnswerRequest):
#     job_role = '개발자'
#     try:
#         result = analyze_text_with_gpt(request.question, request.answer, job_role)
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/questions/{questionid}/follow-up")
async def generate_follow_up_api(questionid: int, request: FollowUpRequest):
    job_role = '개발자'
    try:
        result = generate_follow_up(request.answer, request.question, job_role)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
