import os
import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor #

def fetcher(params):
    session = params[0]
    url = params[1]
    print(f'{os.getpid()} process | {threading.get_ident()} | url : {url}')
    with session.get(url) as response:
        return response.text


def normal_main():
    urls = ['https://naver.com', 'https://daum.net'] * 30
    executor = ThreadPoolExecutor(max_workers=1) # worker의 갯수로 인해 효율성이 달라짐 (너무 많으면 메모리 효율 달라짐)
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)


if __name__ == "__main__":
    start = time.time()
    normal_main()
    end = time.time()
    print('normal_main: ', end - start)  # 10초
