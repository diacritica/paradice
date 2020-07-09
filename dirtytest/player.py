import time
from random import randint
from uuid import uuid4

pcs_path = 'GTCS.txt'
gtot_path = 'GTOT.txt'
gt_path = 'GT.txt'
r_path = 'R.txt'

def read(path):
    file = open(path, 'r')
    value = float(file.read())
    file.close()
    return value

if __name__=="__main__":

    id = uuid4().int
    print("Player ID",id)
    PCS = time.time() #current time in seconds since EPOCH
    print("original PCS",PCS)
    offset = randint(-10,10)
    PCS = PCS + offset
    GTOT = read(gtot_path)
    delta = PCS - GTOT # time delta between PCS and GTOT


    print("new PCS",PCS)
    print("offset",offset)
    print("delta",delta)

    OLDGT = 0
    while True:
        time.sleep(0.1)
        PT = time.time() + offset # current time in seconds since EPOCH
        GT = read(gt_path) # scheduled game time

        if OLDGT != GT: # simple hack to avoid dup reading within 1sec timeframe
            if GT > (PT - delta):
                r = int(read(r_path))
                while int(GT) != int(PT - delta):
                    PT = time.time() + offset
                    time.sleep(0.2)
                print("DICE:",r)
        OLDGT = GT
