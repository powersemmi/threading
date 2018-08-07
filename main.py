from threading import Thread
from time import sleep

total = 4


def creates_item():
    global total
    for i in range(10):
        sleep(0.1)
        print('iteration_1 {}'.format(i))
        total += 1
        print('iterations_1 done')


def creates_item_2():
    global total
    for i in range(7):
        sleep(0.5)
        print('iteration_2 {}'.format(i))
        total += 1
        print('iterations_2 done')


def limits_item():
    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('subtracted by 3')
        else:
            sleep(1)
            print('waiting')


if __name__ == '__main__':
    creates1 = Thread(target=creates_item)
    creates2 = Thread(target=creates_item_2)
    limiter = Thread(target=limits_item, daemon=True)

    creates1.start()
    creates2.start()
    limiter.start()

    creates1.join()
    creates2.join()
    # limiter.join()
