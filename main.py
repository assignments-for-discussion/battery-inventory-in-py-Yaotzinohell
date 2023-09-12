def count_batteries_by_health(present_capacities):
    # Initialize counters for healthy, exchange, and failed batteries
    counts={ 
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    # Rated capacity of a new battery
    rated_capacity = 120  # Ah

    # Loop through each battery's present capacity
    for present_capacity in present_capacities:
        # Calculate SoH%
        soh_percentage = (present_capacity / rated_capacity) * 100
        print(soh_percentage)

        # Classify the battery based on SoH%
        if soh_percentage > 80 and soh_percentage <= 100:
            counts["healthy"] += 1
        elif soh_percentage >= 63 and soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    # Return the counts of healthy, exchange, and failed batteries
    return counts
    

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = []
    present_capacities = [115, 118, 80, 95, 91, 72]
    """
    #For user inputs on present_capacities we can make use of the below code

    # Prompt the user for input
    present_string = input("Enter a list of numbers separated by spaces: ")

    # Split the input string into a list of strings
    present_list = present_string.split()

    # Convert the list of strings to a list of integers
    present_capacities = [int(num_str) for num_str in present_list]

    # Print the resulting list
    print("You entered:", present_capacities)
    """
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == counts["healthy"]
    assert counts["exchange"] == counts["exchange"]
    assert counts["failed"] == counts["failed"]
    print("Healthy Batteries:", counts["healthy"])
    print("Exchange Batteries:", counts["exchange"])
    print("Failed Batteries:", counts["failed"])
    print("Done counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()
