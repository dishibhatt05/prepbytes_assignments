'''
Shopping Cost
Tina is preparing a shopping list containing N items. She knows the quantity and price of each item on the list. 
The shop is offering a 20% discount on the items with a quantity of more than 100 units. 
Given the quantity and price of each of the N items, your task is to calculate how much each item will cost.
 '''
n=int(input())
for i in range(n):
  x, y = [int(x) for x in input().split()]  
  amt=x*y
  if x>100:
    print(amt-(0.2*amt))
  else:
    print(amt)
