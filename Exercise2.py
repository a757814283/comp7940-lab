#Exercise 2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    print(f"The factors of {x} are:")
    for i in range(2, x):
        if x % i == 0:
            print(i)
            
#Exercise 2
print_factor(52623)
