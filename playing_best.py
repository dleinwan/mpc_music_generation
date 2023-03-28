import time
from pythonosc import udp_client
import csv
import sys
import signal

def handle_close(signum, frame): 
        client_.send_message("playing", 0)
        print(" ")
        print("Closing")
        sys.exit(0)

signal.signal(signal.SIGINT, handle_close)

IP = "127.0.0.1"
PORT_TO_MAX = 1001
client_ = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)

with open('best_output.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        #self.pattern_original = row
        print("row: " + str(row))
        client_.send_message("playing", 1)
        for i in range(len(row)):
            # self.client.send_message("playing", 1)
            client_.send_message("midi", int(row[i]))
            print(row[i])
            #i = i + 1
            time.sleep(.5)
            # self.client.send_message("playing", 0)
        client_.send_message("playing", 0)
        time.sleep(1)
        print("next")
        
    file.close()

