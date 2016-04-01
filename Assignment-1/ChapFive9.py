
tuition = 10000
year = 0

while year < 13:
    year += 1
    if year < 10:
        tuition *= 1.05
        if year == 9:
            print("Tuition in ten years is: ", round(tuition,2))
    else:
        tuition += (tuition*1.05)
        if year == 13:
            print("Total cost of four years\' tuition starting ten years from now: ", round(tuition,2))