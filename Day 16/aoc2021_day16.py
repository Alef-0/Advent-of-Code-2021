from math import prod
from os.path import join, isfile
from time import time_ns as time

TEST = 'test16.txt'
INPUT = 'input16.txt'
LOCAL = 'Day 16'
CHOICE = INPUT
start = time()
if not isfile(CHOICE): CHOICE = join(LOCAL, CHOICE)

with open(CHOICE) as file:
    data = file.read().strip()
    # Eliminate the 0b prefix and fills with zeroes
    data = str(bin(int(data, 16)))[2:].zfill(len(data) * 4) 

# print(data) # Comment
pointer = 0

def read_packet(pointer, data):
    packet_version = int(data[pointer : (pointer := pointer + 3)],2)
    # For Part 1
    global sum_of_packet_versions
    sum_of_packet_versions += packet_version
    #
    packet_type_id = int(data[pointer : (pointer := pointer + 3)],2)
    # print(f'{packet_version=}, {packet_type_id=}') # Comment
    if packet_type_id == 4:
        # Literal Value
        string_bits = ''
        while data[pointer] == '1':
            pointer += 1
            string_bits += data[pointer : (pointer := pointer + 4)]
        # Last iteration
        pointer += 1
        string_bits += data[pointer:(pointer := pointer + 4)]
        literal_value = int(string_bits,2)
        # print(f'{literal_value=}') # Comment
    else:
        # Operator
        length_type_ID = int(data[pointer: (pointer := pointer + 1)],2)
        values = []
        if length_type_ID == 0:
            # Total length in bits of subpackets
            total_length = int(data[pointer:(pointer := pointer + 15)],2)
            original_pointer = pointer
            while pointer != original_pointer + total_length:
                # print("Entered in another packet") # Comment
                pointer, new_values = read_packet(pointer, data)
                values.append(new_values)
                # Maybe do something with the new values
        else:
            # Amount of subpackets
            amount_subpackets = int(data[pointer:(pointer := pointer + 11)],2)
            for _ in range(amount_subpackets):
                # print("Entering in another packet") # Comment
                pointer, new_values = read_packet(pointer, data)
                values.append(new_values)
                # Maybe do something with the new values
        # Now realize the operations on the values
        match packet_type_id:
            case 0: literal_value = sum(values)
            case 1: literal_value = prod(values)
            case 2: literal_value = min(values)
            case 3: literal_value = max(values)
            case 5: literal_value = 1 if values[0] > values[1] else 0
            case 6: literal_value = 1 if values[0] < values[1] else 0
            case 7: literal_value = 1 if values[0] == values[1] else 0
            case _: pass
    return pointer, literal_value

sum_of_packet_versions = 0
pointer, result = read_packet(pointer, data)

# print() # To separate the versions
# PART 1 = 879 | PART 2 = 539051801941
print("Part 1: ", sum_of_packet_versions)
print("Part 2: ", result)
print('Time elapsed in ns: ', time() - start)