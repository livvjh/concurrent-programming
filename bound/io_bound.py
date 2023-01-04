def io_bound_func():
    print("값을 입력해주세요.")
    # 사용자가 입력을 안하는 경우 I/O 바운드 발생
    # 이때 사용자가 아니고 서버끼리 통신시에도 발생 (서버에서 응답이 안오면 그걸 기다리는 상태로 병목)
    input_value = input()
    return int(input_value) + 100


if __name__ == "__main__":
    result = io_bound_func()
    print(result)