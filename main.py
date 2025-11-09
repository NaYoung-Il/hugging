from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# FastAPI 객체 생성
app = FastAPI(title='질의응답 챗봇')

# 'question-answering' 파이프라인 로드
qa_pipeline = pipeline(
    "question-answering",
    model="ainize/klue-bert-base-mrc"
)

# QA 입력을 위한 Pydantic 모델 정의
class QAInput(BaseModel):
    question: str  # 질문
    context: str   # 지문 (본문)

@app.post('/ask')
def ask(data: QAInput):
    print("받은 질문 : ", data.question)
    print("받은 지문 : ", data.context)

    # QA 파이프라인 실행
    # question과 context를 명시적으로 전달
    result = qa_pipeline(question=data.question, context=data.context)
    
    print(result)
    # QA 결과 예시: {'score': 0.998, 'start': 10, 'end': 15, 'answer': '어떤 답변'}

    # 사용자가 원하는 형식으로 응답 구성
    response = {
        "input_question": data.question,
        "context": data.context,
        "answer": result['answer'],
        "score": round(result['score'], 4) # 답변의 신뢰도 점수
    }
    return response