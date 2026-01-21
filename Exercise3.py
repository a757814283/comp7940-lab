#From Exercise 2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    #print(f"The factors of {x} are:")
    for i in range(2, x):
        if x % i == 0:
            print(i)
        
#Exercise 3
# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
for num in l:
    print(f"Factors of {num}:")
    print_factor(num)
    print()
