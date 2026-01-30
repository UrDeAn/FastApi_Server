import asyncio
from PriceWb import wbPrice
f = [655919326, 550070961, 505535663]
b = [1073, 9277, 1568]
a = []
for i in f:
    price = asyncio.run(wbPrice(i))
    a.append(price)
print(b)
print(a)
#fastapi dev Server.py