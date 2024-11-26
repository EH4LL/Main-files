import random

def get_inputs():
    flips = int(input("How many times do you want to flip the coin: "))
    return flips

def simulate_flips(number):
    heads = 0
    tails = 0
    for x in range(number):
        result = random.randint(1,2)
        if result == 1:
            heads += 1
        else:
            tails += 1
    
    return (heads/number,tails/number)

def display_results(heads,tails):
    print(f"Heads {heads}, Tails {tails}")

def main():
    results = simulate_flips(get_inputs())
    display_results(results[0],results[1])

main()