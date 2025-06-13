'''
write a python program that will read the amount of rainfall for each day. Get input from user. Use a sentinel value of 99999 to terminate the program

1. A negative value of rainfall should be rejected.
2. Print the number of valid of recorded days,
3. Print the number of rainy days,
4. Print the rainfall over the period, 
5. Print the max amount of rain that fell on any one day. 
'''
def main():
    print("Enter daily rainfall amounts (99999 to stop):")
    num_days = 0
    rainy_days = 0
    total_rainfall = 0.0
    max_rainfall = 0.0

    while True:
        try:
            rainfall = float(input(f"Day {num_days + 1}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if rainfall == 99999:
            break
        if rainfall < 0:
            print("Negative rainfall is not valid. Try again.")
            continue

        num_days += 1
        total_rainfall += rainfall
        if rainfall > 0:
            rainy_days += 1
        if rainfall > max_rainfall:
            max_rainfall = rainfall

    print("\nSummary:")
    print(f"Number of valid recorded days: {num_days}")
    print(f"Number of rainy days: {rainy_days}")
    print(f"Total rainfall: {total_rainfall}")
    print(f"Maximum rainfall in one day: {max_rainfall}")

if __name__ == "__main__":
    main()