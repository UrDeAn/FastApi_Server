from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from bs4 import BeautifulSoup
import asyncio
import requests

app = FastAPI()

# Модель данных, которая приходит от Kotlin
class Item(BaseModel):
    url: str
    id: int
    name: str
    price: int

#@app.post("/items/")
#async def create_item(item: Item):
    #headers = {'User-Agent': 'Mozilla/5.0'}
    #async with httpx.AsyncClient() as client:
        #response = await client.get(item.url, headers=headers)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #price_tag = soup.find('ins', class_='priceBlockFinalPrice--iToZR')
    #if price_tag:
        #price = price_tag.text.strip()
    #else:
        #price = "Цена не найдена"
    #print(price)
    #return {"message": "Item received", "item": item}

#asyncio.run(create_item(Item(url='https://www.wildberries.ru/catalog/489449111/detail.aspx?targetUrl=EX', id=1, name='111', price=1111)))