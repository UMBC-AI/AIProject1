#generate random graphs for testing
import random

ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#Edit these parameters accordingly. The current configuration will generate at most 200 nodes, with 1500 edges between them
NUM_OF_CONNECTIONS=1500
NUM_OF_NODES=200
MIN_WEIGHT=0
MAX_WEIGHT=20

def main():
    f = open("input.txt","a")
    for i in range(0,NUM_OF_CONNECTIONS):
        L1 = random.randint(1,NUM_OF_NODES)#randLetter()
        L2 = random.randint(1,NUM_OF_NODES)#randLetter()
        LE = random.randint(MIN_WEIGHT,MAX_WEIGHT)
        f.write(str(L1)+" "+str(L2)+" "+str(LE)+"\n")
        

def randLetter():
    return ALPHA[random.randint(0,len(ALPHA)-1)]

main()
