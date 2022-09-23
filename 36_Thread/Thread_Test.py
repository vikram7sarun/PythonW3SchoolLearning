import threading
import time



def update_db():
    print("Updating db...")
    time.sleep(5)
    print("Updated db")

def display_number(num):
    for i in range(1,num+1):
        print(i)

def print_evenNumber():
    for i in range(100):
        print("Hello")

# update_db()

thread_db = threading.Thread(target=update_db)
thread_db.start()
display_number(100)
thread_printEvenNumber = threading.Thread(target=print_evenNumber)
thread_printEvenNumber.start()

print(threading.activeCount()) # only one main thread is running
print(threading.enumerate())
thread_db.join()               # To print END at the end of the operation
print("*************END Operation*************")