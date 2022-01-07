# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:04:57 2022

@author: tejan
"""

from pydantic import BaseModel

class arima_api(BaseModel):
    arrival_date: str
    modal_price: float
    