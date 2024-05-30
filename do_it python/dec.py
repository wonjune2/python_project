import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        resutl = original_func()
        end = time.time()
        print(f"함수 수행시간: {end - start}")
        return resutl
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc()