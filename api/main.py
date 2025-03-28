from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load, dump
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from preprocessing import dropna_and_combine_text, text_preprocessing_function, vectorization_function
from typing import List

pipeline = load("pipeline.joblib")


app = FastAPI()


class NewsItem(BaseModel):
    Titulo: str
    Descripcion: str
    Fecha: str


class RetrainData(BaseModel):
    ID: int
    Titulo: str
    Descripcion: str
    Fecha: str
    Label: int

@app.post("/predict/")
def predict(news: NewsItem):
    df = pd.DataFrame([news.dict()])
    prediction = pipeline.predict(df)[0]
    probabilidades = pipeline.predict_proba(df)[0]
    return {"prediction": int(prediction), "probabilidades": int(probabilidades)}

@app.post("/predictMany")
def predict(news_list: List[NewsItem]):
    df = pd.DataFrame([news.dict() for news in news_list])
    predictions = pipeline.predict(df)  
    probabilidades = pipeline.predict_proba(df)
    return {"predictions": predictions.tolist(), "probabilidades": probabilidades.tolist()}

@app.post("/retrain/")
def retrain(data: list[RetrainData]):
    df = pd.DataFrame([item.dict() for item in data])
    X = df.drop(columns=["ID", "Label"])
    y = df["Label"]
    X_processed = pipeline[:-1].transform(X)
    new_model = GradientBoostingClassifier(n_estimators=500, max_depth=5, criterion="friedman_mse")
    new_model.fit(X_processed, y)


    y_pred = new_model.predict(X_processed)
    

    precision = precision_score(y, y_pred, average="weighted")
    recall = recall_score(y, y_pred, average="weighted")
    f1 = f1_score(y, y_pred, average="weighted")


    pipeline.steps[-1] = ("classification", new_model)
    dump(pipeline, "pipelineRetrain.joblib")

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
