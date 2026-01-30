import asyncio
from PriceWb import wbPrice

price = asyncio.run(wbPrice(550070901))
print(price)

#fastapi dev Server.py