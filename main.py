import time
import threading
import os


def eternal_script(interval: int, total_time: int):

    constant = 100
    variable = 10

    # with open("Log.txt", "a") as log_file:
    #     log_file.write(f"Process 'This Process' has run for {total_time} seconds\n")
    #     log_file.write(f"Dividing {constant} by {variable}")
    #     log_file.write(f"Answer is {constant/variable}")
    #     time.sleep(interval)

    print(f"Process 'This Process' has run for {total_time} seconds\n")
    print(f"Dividing {constant} by {variable}")
    print(f"Answer is {constant/variable}"))
    time.sleep(interval)

def task():
    start_time = time.perf_counter()

    while True:
        current_time = time.perf_counter()
        eternal_script(2, round(current_time-start_time))



if __name__ == "__main__":
    with open("Log.txt", "a") as log_file:
        log_file.write("_____________\n")
        log_file.write("New process instance starting\n")
    thread = threading.Thread(target = task())
