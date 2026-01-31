import asyncio
from PriceWb import wbPrice
articles = [655919326, 550070961, 505535663, 499118925, 608718068]
TruePrice = [1073, 9277, 1568, 2948, 3704]
AppPrice = []

for articl in articles:
    price = asyncio.run(wbPrice(articl))
    AppPrice.append(price)

print(TruePrice)
print(AppPrice)
print(AppPrice == TruePrice)
#fastapi dev main.py
#С ВБ кошельком скидка около 2% (от 2% до 8%)
# На занятии сделать парсинг артикула с ссылки (веб и из приложения)
#№#