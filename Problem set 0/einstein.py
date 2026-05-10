# In a file called einstein.py,
#  implement a program in Python that prompts the user for mass
#  as an integer (in kilograms) and then outputs the equivalent 
# number of Joules as an integer. Assume that the user will input an integer.

def joules(mass):
    c = 300000000
    total_energy =  mass * c * c
    return total_energy

def main():
    mass = int(input("Mass(kg): "))
    result = joules(mass)
    print(result)

if __name__ == "__main__":
    main()