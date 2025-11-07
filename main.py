from fastapi import FastAPI
# fastapi 가상환경 설정
# (Ctrl + Shift + P -> Python: Select Interpreter -> 가상환경 선택)
from pydantic import BaseModel
from transformers import pipeline

#fastapi 객체 생성
app = FastAPI(title='감정 분석')

# 멀티 언어 감성 분석 BERT 모델 불러오기
sentimental=pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

class ReviewSentimental(BaseModel):
    text: str

# 요청 본문을 ReviewSentimental 모델로 받음
@app.post('/predict')
def predict(review: ReviewSentimental):
    print("받은 문장 : ", review.text)
    # review.text를 BERT 모델에 전달하여 결과를 받아옴.
    result=sentimental(review.text)[0]
    print(result)

    label = result['label']
    score = result['score']

    if label in ["4 stars", "5 stars"]:
        sentiment = "positive"
    
    elif label in ["1 star", "2 stars"]:
        sentiment = "negative"

    else:
        sentiment = "neutral"
    
    response={"input": review.text, "label": sentiment, "score": round(score, 2)}
    return response