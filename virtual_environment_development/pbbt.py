# Automating basic tasks 
import random

# Shuffel list 
def shuffel(l):
    l = len(l)
    pic = random.randint(0,l-1)
    return l[pic]

def random_generator(data_type, size = 50): # varry range - categorical / numerical/ boolean
    d = []
    if data_type == 1:
        for booleans in range(size):
            e = random.randint(0,1)
            d.append(e)  # making boolean dataset
        return d 
    elif data_type == 2:
        for cat in range(size):
            e = random.randint(0,5)
            d.append(e)
        return d
    elif data_type == 3:
        for nums in range(size):
            e = random.randint(-50, 50)
            d.append(e)
        return d
    else:
        return None 