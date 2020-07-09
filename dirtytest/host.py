import time
from random import randint

gtcs_path = 'GTCS.txt'
gtot_path = 'GTOT.txt'
gt_path = 'GT.txt'
r_path = 'R.txt'

rand_thres = 7
a = 1 #delay in seconds for scheduled roll

def store(path, value):
    file = open(path, 'w')
    file.write(str(value))
    file.close()


def rolldice():
    return randint(0,20)

if __name__=="__main__":

    GTCS = time.time() #current time in seconds since EPOCH
    store(gtcs_path,GTCS)

    while True:
        time.sleep(1)
        GTOT = time.time() #current time in seconds since EPOCH
        store(gtot_path,GTOT)

        if randint(0,10) > rand_thres:
            r = rolldice()
            GT = GTOT + a
            store(gt_path,GT)
            store(r_path,r)
