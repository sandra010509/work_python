print("========== SHOPPINGRECEIPT ==========")
items =[]
total_expenditure = 0

number_of_items =0
int(input("enter number of items purchased: "))

for i in range (number_of_items):
      print("\nItem", i + 1)

      name = input("enter item name: ")
      quantity = int(input("enter quantity: "))
      unit_price =0.00
float(input("enter unit price: "))
total_price = quantity * unit_price
total_expenditure += total_price
item.append([name, quantity, unit_price, total_price])
print("\n==============RECEIPT==============")
print("S/N\tDescription\tQuality\tUnitprice\tTotal price")

for i in range(len(items)):
            
       print(i + 1, "\t", items[i][0], "\t\t",
             items[i][1], "\t\t",
             items[i][2], "\t\t",
             items[i][3])
print("____________________________________")
print("TOTAL EXPENDITURE: ",
      total_expenditure)
print("====================================")
print("thanks for shopping!")
      
      
