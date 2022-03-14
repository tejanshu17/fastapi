import uvicorn
from fastapi import FastAPI,BackgroundTasks
from pydantic import BaseModel
from datetime import date
import pickle
import numpy as np
import pandas as pd
app = FastAPI()

li=[]
Dict={}

class arima(BaseModel):
    Arrival_Date: str
    modal_price: float


def predict_price(data:arima):
    # data=data.dict()
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    index_future_dates=pd.date_range(start='2021-05-30', end='2021-06-02')
    prediction=loaded_model.predict(start=75,end=78)
    prediction.index=index_future_dates
    output=prediction.to_string()
    li.append(output)
    Dict['price']=output
    print(Dict)
    # return {
    #    'prediction': output, 
    # }

@app.get('/')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(predict_price,arima)
    return Dict
    

@app.get('/predictedValue')
async def displayValue():
    return Dict