# Let us say your expense for every month are listed below,
#     January - 2200
#     February - 2350
#     March - 2600
#     April - 2130
#     May - 2190
# Create a list to store these monthly expenses and using that find out,
expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(expense[1] - expense[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
sum = 0
for i in range(3):
    sum += expense[i]
print(sum)

# 3. Find out if you spent exactly 2000 dollars in any month.
for item in expense:
    if item == 2000:
        print(True)
else:
    print(False)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.
expense.append(1980)
print(expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a 
# correction to your monthly expense list based on this.
expense[3] = expense[3] - 200
print(expense)
