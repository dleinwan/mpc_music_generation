from pythonosc import udp_client
import random
import time
from utils import *
import signal
import time

signal.signal(signal.SIGINT, handle_close)

print("main running")

my_generation = StartGeneration()

my_generation.generate_pattern()

print("original: " + str(my_generation.pattern_original))
print("grouped: " + str(my_generation.pattern_grouped))
print(" ")

my_generation.generate_and_load_to_file()

print("BEFORE RANDOMIZATION")
print("original: " + str(my_generation.pattern_original))
print("grouped: " + str(my_generation.pattern_grouped))
#my_generation.play_pattern()
print("")

time.sleep(1)

my_generation.randomize_pattern()

my_generation.reload_original()
print("AFTER RANDOMIZATION")
print("original: " + str(my_generation.pattern_original))
print("grouped: " + str(my_generation.pattern_grouped))
print("")


#my_generation.play_best_output()