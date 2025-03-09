import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    heads_count = 0
    tails_count = 0
    results = []
    
    for _ in range(num_flips):
        result = coin_toss()
        results.append(result)
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    total = heads_count + tails_count
    heads_percentage = (heads_count / total) * 100 if total > 0 else 0
    tails_percentage = (tails_count / total) * 100 if total > 0 else 0
    
    return results, heads_count, tails_count, heads_percentage, tails_percentage

def main():
    try:
        num_flips = int(input("Enter the number of coin flips: "))
        if num_flips <= 0:
            print("Please enter a positive integer.")
            return
        
        results, heads_count, tails_count, heads_percentage, tails_percentage = multiple_tosses(num_flips)
        print("\nCoin Toss Results:")
        for result in results:
            print(result)
        
        print(f"\nHeads: {heads_count} ({heads_percentage:.2f}%)")
        print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
