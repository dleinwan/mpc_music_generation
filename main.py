from pythonosc import udp_client
import random
import time

print("main running")

# using pythonosc (udp) send messages to max
IP = "127.0.0.1"
PORT_TO_MAX = 1001
client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)


#client.send_message("max", 1)
#client.send_message("max2", 2)

class StartGeneration:
    tonic = 0 # index at which the tonic resides
    second = 1
    third = 2
    fourth = 3
    fifth = 4
    sixth = 5
    seventh = 6
    octave = 7

    maj_pattern1 = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16]
    maj_pattern1_imp = [0, 4, 7, 12]
    maj_pattern1_num_important = len(maj_pattern1_imp)

    min_pattern1 = [0, 2, 3, 5, 7, 9, 11, 12, 14, 15]
    min_pattern1_imp = [0, 3, 7, 12]
    min_pattern1_num_important = len(min_pattern1_imp)

    pattern = [0] * len(maj_pattern1)



    def generate_unit(self):
        # choose tonic, third or fifth
        chosen_index = random.randint(0, len(self.maj_pattern1_imp) - 1)
        chosen_degree = self.maj_pattern1_imp[chosen_index]
        one_array = [-1, 1]
        # add neighbors
        neighbor1_index = (chosen_degree + 1*random.choice(one_array)) % len(self.maj_pattern1)
        neighbor2_index = (neighbor1_index + 1*random.choice(one_array)) % len(self.maj_pattern1)
        neighbor3_index = (neighbor2_index + 1*random.choice(one_array)) % len(self.maj_pattern1)
        print("neighbor1_index: " + str(neighbor1_index))
        print("neighbor2_index: " + str(neighbor2_index))
        return [neighbor1_index, neighbor2_index, neighbor3_index]
    
    def generate_pattern(self):
        unit1 = self.generate_unit()
        unit2 = self.generate_unit()
        unit3 = self.generate_unit()
        self.pattern = unit1 + unit2 + unit3
        return unit1 + unit2 + unit3

    def play_pattern(self):
        i = 0
        for degree in self.pattern:
            playing = 1
            client.send_message("playing", playing)
            client.send_message("midi", pattern[i])
            print(pattern[i])
            i = i + 1
            time.sleep(.5)
        playing = 0
        client.send_message("playing", playing)




my_generation = StartGeneration()

pattern = my_generation.generate_pattern()

print(pattern)

my_generation.play_pattern()

