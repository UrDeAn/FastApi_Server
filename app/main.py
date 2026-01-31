#import asyncio
#from price_wb import wb_price
#import subprocess
from fastapi import FastAPI
import os
#articles = [655919326, 550070961, 505535663, 499118925, 608718068]
#TruePrice = [1073, 9277, 1568, 2948, 3704]
#AppPrice = []

#try:
#    subprocess.run(['playwright', 'install'], check=True)
#    print("Браузеры успешно установлены.")
#except subprocess.CalledProcessError:
#    print("Ошибка при установке браузеров.")

#for articl in articles:
#    price = asyncio.run(wb_price(articl))
#    AppPrice.append(price)

#print(TruePrice)
#print(AppPrice)
#print(AppPrice == TruePrice) # За 1 день 4 цены уже сменились

app = FastAPI()
port = int(os.environ.get("PORT", 8000))  # 8000 — значение по умолчанию

@app.get("/item")
def read_root():
    return {"message": "Hello World"}

@app.get("/item/1")
def read_root():
    return {"message": "Hello World1"}
#fastapi dev main.py
#С ВБ кошельком скидка около 2% (от 2% до 8%)
# На занятии сделать парсинг артикула с ссылки (веб и из приложения)
#№###