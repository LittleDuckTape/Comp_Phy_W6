import threading
import random

lower_num = 1
upper_num = 10000
buffer_size = 100
max_count = 10000

buffer = []
lock = threading.Lock()
condition = threading.Condition(lock)

producer_done = False
produced_total = 0
consumed_total = 0

all_file = open("all.txt", "w")
even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")

def producer():
    global produced_total, producer_done

    for _ in range(max_count):
        num = random.randint(lower_num, upper_num)

        with condition:
            while len(buffer) >= buffer_size:
                condition.wait()

            buffer.append(num)
            all_file.write(f"{num}\n")
            produced_total += 1

            condition.notify_all()
    
    with condition:
        producer_done = True
        condition.notify_all()

def consumer(want_even, out_file):
    global consumed_total

    while True:
        with condition:
            while True:
                if consumed_total >= max_count:
                    condition.notify_all()
                    return
                
                if len(buffer) == 0:
                    if producer_done:
                        condition.notify_all()
                        return
                    condition.wait()
                    continue

                top = buffer[-1]

                if (top % 2 == 0) == want_even:
                    num = buffer.pop()
                    consumed_total += 1
                    out_file.write(f"{num}\n")
                    condition.notify_all()
                    break

                else:
                    condition.wait()

producer_thread = threading.Thread(target = producer)
even_thread = threading.Thread(target = consumer, args = (True, even_file))
odd_thread = threading.Thread(target = consumer, args = (False, odd_file))

producer_thread.start()
even_thread.start()
odd_thread.start()

producer_thread.join()
even_thread.join()
odd_thread.join()

all_file.close()
even_file.close()
odd_file.close()

print("Program done :)")