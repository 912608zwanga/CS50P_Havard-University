# variable to keep track
amount_due = 50
 
# Loop until amount due is greater than 0
while amount_due > 0:
    # print amount due
    print(f"Amount Due: {amount_due}")
    # Ask user for payment, insert coin
    coin = int(input("Insert Coin: "))
    # check if coin is 25, 10, or 5
    if coin in [25, 10, 5]:
        amount_due -= coin # if so, subtract coin from amountDue

#  calculate change
change_owed = abs(amount_due)
# print result
print(f"Change Owed: {change_owed}")
