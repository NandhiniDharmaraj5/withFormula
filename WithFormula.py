# withFormula
In [3]:
import math
a=[15,26,10,9,15,20,18,11,8,20]
b=[128,128,116,124,135,120,126,133,137,127]
def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 
    
def sampleStandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

def pearson_def(x, y):
    scorex = []
    scorey = []
    for i in x: 
        scorex.append((i - mean(x))/sampleStandardDeviation(x)) 
    for j in y:
        scorey.append((j - mean(y))/sampleStandardDeviation(y))   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)


print("mental ability Correlation: ",pearson_def(a,b))
mental ability Correlation:  -0.14312743651646645
In [4]:
import math
a=[2,2,1,3,4,1,5,3,1,2]
b=[10,30,12,24,40,11,56,40,8,14]
def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 
    
def sampleStandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

def correlation_def(x, y):

    scorex = []
    scorey = []

    for i in x: 
        scorex.append((i - mean(x))/sampleStandardDeviation(x)) 

    for j in y:
        scorey.append((j - mean(y))/sampleStandardDeviation(y))   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)

print("stumps and bettle Correlation: ",correlation_def(a,b))
stumps and bettle Correlation:  0.9158498450298386
In [5]:
import math
a=[20,30,40,50,60]
b=[57,61,63,61,57]

def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 
    
def sampleStandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

def correlation_def(x, y):

    scorex = []
    scorey = []

    for i in x: 
        scorex.append((i - mean(x))/sampleStandardDeviation(x)) 

    for j in y:
        scorey.append((j - mean(y))/sampleStandardDeviation(y))   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)

print("hour and gallon Correlation:",correlation_def(a,b))
hour and gallon Correlation: 5.551115123125783e-17
In [ ]:

