import asyncio
from playwright.async_api import async_playwright

async def wbPrice(TARGET_NM) -> None:
    stop_event = asyncio.Event()
    price = None  # локальная переменная

    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            locale="ru-RU"
        )
        page = await context.new_page()

        async def handle_response(response):
            nonlocal price  # используем nonlocal для изменения переменной из внешней функции
            if "u-card/cards/v4/detail" in response.url:
                try:
                    data = await response.json()
                    print("JSON ПОЛУЧЕН ✅")
                    price = int(int(data["products"][0]["sizes"][0]["price"]["product"]) / 100)
                    stop_event.set()
                except Exception as e:
                    print("ERROR", e)

        page.on("response", handle_response)

        await page.goto(
            f"https://www.wildberries.ru/catalog/{TARGET_NM}/detail.aspx",
            wait_until="networkidle"
        )

        # ждём либо 15 секунд, либо пока придёт JSON
        try:
            await asyncio.wait_for(stop_event.wait(), timeout=15)
        except asyncio.TimeoutError:
            print("JSON не был получен за 15 секунд")

        await browser.close()

    return price  # возвращаем результат
