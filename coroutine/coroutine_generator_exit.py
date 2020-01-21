"""
    co-routine object에서 close method를 call하면 co-routine이 종료될 때 GeneratorExit Exception이 발생합니다.
    따라서 이 Exception을 처리하면 co-routine의 종료 시점을 알 수 있습니다.
"""
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit: # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')

co = number_coroutine()
next(co) # co.send(None)

for i in range(20):
    co.send(i)

co.close()