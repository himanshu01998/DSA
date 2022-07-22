numDays = int(input("How many days temprature: "))

total = 0
temp = []

for i in range(0, numDays):
    nextDay = int(input("Enter Day "+str(i+1)+" Temprature: "))
    temp.append(nextDay)
    total += nextDay

avg = (total/numDays)
print("Average:",avg)
days = 0

for item in temp:
    if item > avg:
        days += 1

print(str(days),"temp was higher than average")
