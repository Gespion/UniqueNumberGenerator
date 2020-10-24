import random
from time import sleep

def UniqueNumberGenerator(start,end,size):
    
    final_list = []
    
    while len(final_list) < size:
        number = random.randint(start,end)
        if number not in final_list:
            final_list.append(number)
            print("- %d -" % number)
            sleep(0.5)
        else:
            pass
    print("Unique random numbers from your list: " , final_list)

    random.choice()

print("How many random numbers to generate: ")
random_size = int(input())
print("Start from:")
random_start = int(input())
print("End at:")
random_end = int(input())
print("Starting nummber(s) generation...")
UniqueNumberGenerator(random_start,random_end,random_size)