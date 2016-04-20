# Calculate gratuity amount and total amount : Chapter 2 - 5

sub_total, gratuity_per = eval(input("Enter the sub total and gratuity%: "))

gratuity_amount = round((sub_total*gratuity_per)/100,2)
total_amount = round(sub_total + gratuity_amount,2)

print("Gratuity Amount is ",gratuity_amount," and the Total Amount is ",total_amount)
