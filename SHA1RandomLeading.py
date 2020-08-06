import hashlib
import random
import matplotlib.pyplot as plt
import os
import sys

def search(space,leading):
    for i in range(space): 

        hashvalue = hashlib.sha1(random.getrandbits(128).to_bytes(16, 'big')).digest()
        zeroes = 160 - int.from_bytes(hashvalue, 'big').bit_length()
        
        leading[zeroes] = leading[zeroes] +1
        
        if i % 10000000 == 0:
            print (".",end ='',flush=True)
            
    for item in leading: 
        print(item, end =',')
        

def searchAndPrint(numberOfTrials,leadingZero):
    for i in range(numberOfTrials): 
        rndValue = random.getrandbits(128).to_bytes(16, 'big')
        hashvalue = hashlib.sha1(rndValue).digest()
        
        if leadingZero == (160 - int.from_bytes(hashvalue, 'big').bit_length()):
            print(bin(int.from_bytes(rndValue, byteorder='big'))[2:].zfill(128), " ", bin(int.from_bytes(hashvalue, byteorder='big'))[2:].zfill(160))
        

def preResult(): #With a numberOfTrials = 10000000000
    return [4999899716,2500040694,1250025163,625012247,312519435,156242195,78129201,39070485,19532263,9766270,4882962,2438565,1220675,610279,305021,152313,75950,38232,19141,9601,4800,2403,1200,610,305,127,75,32,16,15,4,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    

def expectedGraphData(space,div2):    
    for idx,item in enumerate(div2) : 
        div2[idx] = space /pow(2,idx+1)
        

def plotTheGraph(a_list, leading,div2):
    plt.plot(a_list,leading)
    plt.plot(a_list,div2)
    plt.title('SHA-1 Leading Zeroes')
    plt.xlabel('Leading Zeroes')
    plt.ylabel('Count log_1000')
    plt.yscale('log',base=1000)
    plt.show()

leadingZeros = [0] * 160
expectedValues   = [0] * 160

#numberOfTrials = 10000000000
numberOfTrials = 10000

#The x axis    
xAxislist = list(range(1, 161))

#searchAndPrint(numberOfTrials,2)

search(numberOfTrials, leadingZeros)

#leadingZeros = preResult()

expectedGraphData(numberOfTrials,expectedValues)

plotTheGraph(xAxislist,leadingZeros, expectedValues)
