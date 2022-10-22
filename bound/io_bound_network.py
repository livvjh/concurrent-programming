import requests


def io_bound_func():
    return requests.get("https://google.com")


if __name__ == "__main__":
    for _ in range(10):
        # 요청한 시간의 누적으로 인해 bound 발생
        result = io_bound_func()
    print(result)
