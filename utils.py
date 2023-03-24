from pythonosc import udp_client
import random
import time

# using pythonosc (udp) send messages to max
IP = "127.0.0.1"
PORT_TO_MAX = 1001
client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)


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

    pattern_length = 14

    pattern_original = [0] * pattern_length
    pattern_grouped = [[0,0,0,0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0]]
    pattern_with_octaves = [[0,0,0,0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0]]
    octave_chance = 20

    first_unit = [0, 0, 0, 0]
    unit1 = [0, 0, 0]
    unit2 = [0, 0, 0]
    unit3 = [0, 0, 0]
    last_note = [0]


    one_array = [-1, 1]



    def generate_unit(self):
        # choose tonic, third or fifth
        chosen_index = random.randint(0, len(self.maj_pattern1_imp) - 1)
        chosen_degree = self.maj_pattern1_imp[chosen_index]
        # add neighbors
        neighbor1_index = (chosen_degree + random.choice(self.one_array)) % len(self.maj_pattern1)
        neighbor2_index = (neighbor1_index + random.choice(self.one_array)) % len(self.maj_pattern1)
        neighbor3_index = (neighbor2_index + random.choice(self.one_array)) % len(self.maj_pattern1)
        print("neighbor1_index: " + str(neighbor1_index))
        print("neighbor2_index: " + str(neighbor2_index))
        return [neighbor1_index, neighbor2_index, neighbor3_index]
    
    def generate_unit_four(self):
        # choose tonic
        chosen_degree = 0
        # add neighbors
        neighbor1_index = (chosen_degree + random.choice(self.one_array)) % len(self.maj_pattern1)
        neighbor2_index = neighbor1_index + 1
        neighbor3_index = neighbor2_index + 1
        neighbor4_index = (neighbor3_index + random.choice(self.one_array)) % len(self.maj_pattern1)
        print("neighbor1_index: " + str(neighbor1_index))
        print("neighbor2_index: " + str(neighbor2_index))
        print("neighbor3_index: " + str(neighbor3_index))
        print("neighbor4_index: " + str(neighbor4_index))
        return [neighbor1_index, neighbor2_index, neighbor3_index, neighbor4_index]
        
    
    def generate_pattern(self):
        self.unit1 = self.generate_unit()
        self.unit2 = self.generate_unit()
        self.unit3 = self.generate_unit()
        self.first_unit = self.generate_unit_four()
        self.last_note = [(self.unit1[0] + random.choice(self.one_array)) % len(self.maj_pattern1)]
        self.pattern_original = self.first_unit + self.unit1 + self.unit2 + self.unit3 + self.last_note
        self.pattern_grouped = [self.first_unit, self.unit1, self.unit2, self.unit3, self.last_note]
        return
    
    def randomize_pattern(self):
        units = [self.first_unit, self.unit1, self.unit2, self.unit3]
        new_pattern = []
        indeces = [0, 1, 2, 3]
        random.shuffle(indeces)
        i = 0
        for index in indeces:
            new_pattern.append(units[index])
            i = i + 1
        new_pattern.append(self.last_note)
        self.pattern_grouped = new_pattern
        print(new_pattern)
            
    
    def add_octaves(self):
        i = 0
        for unit in self.pattern_grouped:
            j = 0
            for degree in unit:
                num = random.randint(1, 100)
                print("rand num: " + str(num))
                if num > self.octave_chance:
                    self.pattern_with_octaves[i][j] = degree + 12
                    print("changed! " + str(degree + 12))
                j = j + 1

            i = i + 1

    def play_octaves(self):
        i = 0
        for unit in self.pattern_with_octaves:
            client.send_message("playing", 1)
            j = 0
            for degree in unit:
                client.send_message("playing", 1)
                print(self.pattern_with_octaves[i][j])
                client.send_message("midi", self.pattern_with_octaves[i][j])
                time.sleep(.2)
                j = j + 1
                client.send_message("playing", 0)
                #print(str(i) + " " + str(j))
            i = i + 1
            time.sleep(.1)
            client.send_message("playing", 0)
        client.send_message("playing", 0)
        return

    def play_pattern(self):
        i = 0
        for degree in self.pattern:
            client.send_message("playing", 1)
            client.send_message("midi", self.pattern_original[i])
            print(self.pattern[i])
            i = i + 1
            time.sleep(.5)
        client.send_message("playing", 0)

    def play_pattern_groups_of_3(self):
        i = 0
        for unit in self.pattern_grouped:
            client.send_message("playing", 1)
            j = 0
            for degree in unit:
                client.send_message("playing", 1)
                print(self.pattern_grouped[i][j])
                client.send_message("midi", self.pattern_grouped[i][j])
                time.sleep(.2)
                j = j + 1
                client.send_message("playing", 0)
            i = i + 1
            time.sleep(.1)
            client.send_message("playing", 0)
        client.send_message("playing", 0)
        return