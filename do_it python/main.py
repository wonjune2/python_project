# 데코레이터 함수 정의
def my_decorator(func):
    def wrapper():
        print("데코레이터 전처리")
        func()
        print("데코레이터 후처리\n")
    return wrapper

# 데코레이터를 사용하여 함수 수정
@my_decorator
def say_hello():
    print("hello!")

@my_decorator
def say_world():
    print("world!")

# 함수 호출
say_hello()
say_world()