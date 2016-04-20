
series_sum = 0

for numrator in range(1,98,2):
        series_sum += (numrator)/(numrator+2)
        print(numrator,"/",numrator+2,end="")
        if not numrator == 97:
            print(" + ",end="")
        
    

print(" = ",round(series_sum,2))