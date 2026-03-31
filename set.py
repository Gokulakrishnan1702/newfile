akash = {"apple", "orange", "pineapple"}

# Check if "apple" is in the set
if "apple" in akash:
    print("yes")

# Add elements to the set
akash.update(["onion", 1])  # update expects an iterable

# Print each element in the set
for item in akash:
    print(item)