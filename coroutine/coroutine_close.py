"""
    보통 co-routine은 실행 상태를 유지하기 위해 while True:를 사용해서 끝나지 않는 infinite loop로 동작합니다.
    만약 co-routine을 강제로 종료하고 싶다면 close method를 사용합니다.
    close는 코루틴의 종료 시점을 알아야 할 때 사용하면 편리합니다.

    object_of_coroutine.close()
"""
def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')

co = number_coroutine()
next(co) # co.send(None)

for i in range(20):
    co.send(i)

co.close() # 코루틴 종료
