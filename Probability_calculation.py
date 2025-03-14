# This program calculates the Probability that an illiterate servant post 5 letter correctly.

x = int(input("Number of letters:"))
# This procedure calculates the total number of ways, the illiterate servant can post the letters.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

Number_of_exhaustive_cases = factorial(x)
Number_of_exhaustive_cases_1 = x * (x - 1) * (x - 2) * (x - 3) * (x - 4)
# This procedure calculates the number of ways the illiterate servant can post the letters correctly.   
# checks if factorial (x ) equals number_of_exhaustive_cases_1
if factorial(x) == Number_of_exhaustive_cases_1:
    Number_of_correct_cases = 1
else:   
    Number_of_correct_cases = 0

# This procedure calculates the probability that the illiterate servant can post the letters correctly.
Probability = Number_of_correct_cases / Number_of_exhaustive_cases  
print("The probability that the illiterate servant can post the letters correctly is:", Probability)
# Output:
# Number of letters:5
# The probability that the illiterate servant can post the letters correctly is: 0.0001