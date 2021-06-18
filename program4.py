print ("hello world")

i = 0
j = 1
k = 0
while i<100:
    print(k)
    k = i + j
    i = j
    j = k

for i in range (0,10):
    print(i)
    for j in range (0,3):
        print ("hi")

def primeFinder (max):
        for i in range(2,max):
                for j in range(2,i):
                    if i % j ==0:
                        break
                else:
                    print (i)
                return (max)
