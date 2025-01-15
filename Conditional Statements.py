num = 3
if num > 0:
    print(num,"is a positive number.")




num = -1
if num > 0:
    print(num,"is a positive number.")
actual_cost = float(input("Please Enter the actual product price: "))
sale_amount = float(input("Please Enter the Sales Amount: "))
if (sale_amount > actual_cost):
  amount = sale_amount - actual_cost
  print("Total Profit = {0}".FORMAT(amount))  
else:
  print("No Profit!!!")  
            