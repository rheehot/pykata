"""
    co-routine은 cooperative routine을 의미하며, 서로 협력하는 routine이라는 뜻이다. main-routine과 sub-routine처럼 종속된
    관계가아니라 서로 대등한 관계이며 특정 시점에 상대방의 코드를 실행한다.
    co-routine은 generator의 specific case로 generator는 yield로 값을 발생시켰지만, co-routine은 yield로 값을 받아온다.
    co-routine은 yield에서 function의 중간에 대기한 다음에 main routine을 실행하다가 다시 co-routine을 실행한다.

    co-routine에 값을 보낼 경우에는 아래의 형태로 코드를 작성한다.

    object_of_coroutine.send(value)
    variable = (yield) # inside of co-routine
"""
def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)

co = number_coroutine()
next(co) # co.send(None)


co.send(1)
co.send(2)
co.send(3)
