"""
    co-routine 안에 Exception을 발생 시킬 때는 throw method를 사용합니다. throw는 말그대로 던지다라는 뜻인데
    Exception을 co-routine 안으로 던집니다. 이때 throw method에 지정한 error message는 except as의 variable에 들어갑니다.
"""
def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total # 코루틴 바깥으로 값 전달

co = sum_coroutine()
next(co) # co.send(None)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기')) # 190, 코루틴의 except에서 yield로 전달받은 값
