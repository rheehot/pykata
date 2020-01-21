"""
    co-routine에서 값을 바깥으로 보낼 경우에는 아래의 형태로 코드를 작성한다.
    next와 send의 차이를 살펴보면 next는 co-routine의 코드를 실행하지만 값을 보내지 않을 때 사용하고,
    send는 값을 보내면서 co-routine의 코드를 실행할 때 사용한다.
    yield를 사용하여 co-routine 바깥으로 값을 전달하면 next와 send의 반환값으로 받는다는 점만 기억하면 됩니다.

    variable_1 = (yield variable_2) # inside of co-routine, out variable_2
"""
def sum_coroutine():
    total = 0
    while True:
        x = (yield total)  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x


co = sum_coroutine()
print(next(co))  # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력

print(co.send(1))  # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))  # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))  # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력
