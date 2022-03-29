# nyc_weather.csv contains new york city weather for first few days in the month of January. 
# Write a program that can answer following,
#     What was the average temperature in first week of Jan
#     What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

# The best data structure to use here was a list because all we wanted was access of 
# temperature elements

arr = []

with open("nyc_weather.csv", 'r') as f:
    for line in f:
        token = line.split(',')
        try:
            temp = int(token[1])
            arr.append(temp)
        except:
            print("Invalid temp")

print(arr)

print(sum(arr[0:7])/len(arr[0:7]))
print(max(arr[0:10]))

# nyc_weather.csv contains new york city weather for first few days in the month of January. 
# Write a program that can answer following,
#     What was the temperature on Jan 9?
#     What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

# The best data structure to use here was a dictionary (internally a hash table) because we wanted 
# to know temperature for specific day, requiring key, value pair access where you can look up an 
# element by day using O(1) complexity

dt = {}
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        token = line.split(',')
        try:
            day = token[0]
            temp = int(token[1])
            dt[day] = temp
        except:
            print("Invalid temp")

print(dt)
print(dt['Jan 9'])
print(dt['Jan 4'])