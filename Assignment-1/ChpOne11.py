# To calculate the population year on year : Chapter1 - 11
initial_population = 312032486
days_year = 365
print("Initial Population: " + str(initial_population))
year1_births = (365*24*60*60)//(7)
year1_deaths = (365*24*60*60)//(13)
year1_immigrants = (365*24*60*60)//(45)
year1_change = year1_births + year1_immigrants - year1_deaths

year1_population = initial_population + year1_change
print("Population growth: " + str(year1_change))
print("Population after first year: " + str(year1_population))

year2_population = year1_population + year1_change
print("Population after second year: " + str(year2_population))

year3_population = year2_population + year1_change
print("Population after third year: " + str(year3_population))

year4_population = year3_population + year1_change
print("Population after fourth year: " + str(year4_population))

year5_population = year4_population + year1_change
print("Population after fifth year: " + str(year5_population))

