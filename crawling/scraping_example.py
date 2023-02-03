import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup


async def coroutine_fetcher(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        # cont_thumb = soup.select('div.cont_thumb')
        cont_thumb_2 = soup.find_all('div','cont_thumb')
        for cont in cont_thumb_2:
            title = cont.find('p', 'txt_thumb')
            if title is not None:
                print(title.text,'\n')


async def coroutine_main():
    base_url = 'https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C'
    urls = [f'{base_url}?page={i}' for i in range(1, 11)]
    async with aiohttp.ClientSession() as session:  # 객체생성, get, close까지의 로직
        await asyncio.gather(
            *[coroutine_fetcher(session, url) for url in urls]
        )


if __name__ == '__main__':
    start = time.time()
    asyncio.run(coroutine_main())
    end = time.time()
    print('coroutine_main: ', end - start)  # 2초
