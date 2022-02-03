import time

def sum(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total

def timefunction(f, inputvalue):
    time1 = time.time()
    x = f(inputvalue)
    time2 = time.time()
    return time2 - time1

def bench(f, intervalsize, numberofintervals, startvalue, numberruns):
    f_out = open("testfile.csv","w+") 
    inputvalue = startvalue
    for i in range(numberofintervals):
        total = 0
        for j in range(numberruns):
            total = total + timefunction(f,inputvalue)
        outputvalue = total / numberruns 
        f_out.write(str(inputvalue)+","+str(outputvalue)+"\r")
        inputvalue = inputvalue + intervalsize
    f_out.close()

bench(sum, 10000, 10, 10000, 10)
