# Create a list of all odd numbers between 1 and a max number. Max number is something you need to 
# take from a user using input() function

num = int(input())
odd = []

for i in range(1, num+1):
    if not i%2==0:
        odd.append(i)
print(odd)