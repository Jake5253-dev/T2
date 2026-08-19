import time
import threading
import os


def eternal_script(interval: int, total_time: int, variable: int):

    constant = 100

    with open("Log.txt", "a") as log_file:

        log_file.write(f"Process {os.getpid} has run for {total_time} seconds\n")
        log_file.write(f"Current time is {time.ctime()}\n")
        log_file.write(f"Dividing {constant} by {variable}\n")
        log_file.write(f"Answer is {constant/variable}\n\n")
        time.sleep(interval)
    

def task():
    start_time = time.perf_counter()
    variable = 11
    while True:
        variable = variable - 1
        current_time = time.perf_counter()
        eternal_script(2, round(current_time-start_time), variable)



if __name__ == "__main__":
    with open("Log.txt", "a") as log_file:
        log_file.write("_____________\n")
        log_file.write("New process instance starting\n")
    thread = threading.Thread(target = task())
