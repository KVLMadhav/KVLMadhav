priorities = [
    "Box of Matches", "Food concentrate", "50 feet nylon rope", "Parachute silk", "Portable heater",
    "Two Pistols", "Dehydrated milk", "Two tanks of oxygen", "f ", "Priority10",
    "Priority11", "Priority12", "Priority13", "Priority14", "Priority15"
]

# Function to get the rank of the input priority
def get_priority_rank(priority):
    try:
        rank = priorities.index(priority) + 1
        return f"The rank of '{priority}' is {rank}."
    except ValueError:
        return f"'{priority}' is not in the list of priorities."
input_priority = input("Enter your priority: ")


print(get_priority_rank(input_priority))
