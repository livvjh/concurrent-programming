import os
import threading
import time
import requests


def fetcher(session, url):
    # with session.Session() as session: # 객체생성, get, close까지의 로직
    #     session.get(url)
    with session.get(url) as response:
        return response.text


def normal_main():
    urls = ['https://naver.com', 'https://google.com', 'https://livvjh.com'] * 30
    # session = requests.Session()
    # session.get(url)
    # session.close()
    with requests.Session() as session:  # 객체생성, get, close까지의 로직
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == '__main__':
    start = time.time()
    normal_main()
    end = time.time()
    print('normal_main: ', end - start)  # 10초
