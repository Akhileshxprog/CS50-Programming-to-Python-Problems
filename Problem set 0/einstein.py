
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