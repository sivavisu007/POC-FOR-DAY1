from time import *
from threading import *
def siva():
    print("hello")
    sleep(1)
    print("love")

def hari():
    print("siva")
    sleep(1)
    print("is god")

th1 = Thread(target=siva)
th2 = Thread(target=hari)

th1.start()
sleep(0.2)
th2.start()


th1.join()
th2.join()

print("bye")
