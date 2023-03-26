from pythonosc import udp_client
import random
import time
from utils import *
import signal

signal.signal(signal.SIGINT, handle_close)

print("main running")

my_generation = StartGeneration()

my_generation.generate_pattern()

print("original: " + str(my_generation.pattern_original))
print("grouped: " + str(my_generation.pattern_grouped))
print(" ")
# print(my_generation.pattern_with_octaves)

#my_generation.play_pattern()

###my_generation.play_pattern_groups_of_3()

# time.sleep(.5)
# my_generation.add_octaves()
# my_generation.play_octaves()


# print("original: " + str(my_generation.pattern_original))
# print("grouped: " + str(my_generation.pattern_grouped))
# print("with octaves: " + str(my_generation.pattern_with_octaves))


print("BEFORE RANDOMIZATION")
print("original: " + str(my_generation.pattern_original))
print("grouped: " + str(my_generation.pattern_grouped))
my_generation.play_pattern()
print("")

my_generation.randomize_pattern()

my_generation.reload_original()
print("AFTER RANDOMIZATION")
print("original: " + str(my_generation.pattern_original))
print("grouped: " + str(my_generation.pattern_grouped))
my_generation.play_pattern()
print("")
