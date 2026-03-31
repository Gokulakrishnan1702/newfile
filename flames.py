"""
n1=int (input("number1"))
n2=int (input("number2"))
n3=n1*n2
print(n3)
"""
def remove_common_letters(name1, name2):
    name1 = list(name1.replace(" ", "").lower())
    name2 = list(name2.replace(" ", "").lower())

    for letter in name1[:]:  # iterate over a copy of name1
        if letter in name2:
            name1.remove(letter)
            name2.remove(letter)
    
    return len(name1) + len(name2)

def flames_result(count):
    flames = list("FLAMES")
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            right = flames[index + 1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]

def get_relationship(name1, name2):
    count = remove_common_letters(name1, name2)
    final_letter = flames_result(count)
    meanings = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    return meanings[final_letter]

# Example usage
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
result = get_relationship(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")