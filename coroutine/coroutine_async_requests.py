import asyncio
import time

import aiohttp


async def coroutine_fetcher(session, url):
    async with session.get(url) as response:
        return await response.text() # 실행의 결과값을 기다리지 않고 응답을 한꺼번에 받는다


async def coroutine_main():
    urls = ['https://naver.com', 'https://google.com', 'https://livvjh.com'] * 30
    async with aiohttp.ClientSession() as session:  # 객체생성, get, close까지의 로직
        result = await asyncio.gather(
            *[coroutine_fetcher(session, url) for url in urls]
        )
        # result = await coroutine_fetcher(session, urls[0])
        print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(coroutine_main())
    end = time.time()
    print('coroutine_main: ', end - start) # 2초
