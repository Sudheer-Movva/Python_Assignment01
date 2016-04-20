currentTuition = 10000
incRate = 5
i = 1
futureTuition = 0
sumTot = 0
while i<=14:
    if(futureTuition ==0):
        futureTuition = currentTuition+(currentTuition*incRate)/100
    else:
        if(i==10):
            tenYrTuition = futureTuition
        if(i>10):
            sumTot = sumTot+futureTuition
        futureTuition = futureTuition+(futureTuition*incRate)/100
    i+=1
print("Tuition in 10 years time is ", round(tenYrTuition,2))
print("Cost of four years worth of tuition starting 10 years from now is ", round(sumTot,2))