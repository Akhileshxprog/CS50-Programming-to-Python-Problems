# In a file called faces.py, implement a function called convert that accepts a str
#  as input and returns that same input with any :) converted to 🙂
#  (otherwise known as a slightly smiling face) and any :( converted to 🙁
#  (otherwise known as a slightly frowning face). All other text should be returned unchanged.

def convert(text):
    text = text.replace(":)", ("🙂"))
    text = text.replace(":(", ("🙁"))
    return text

def main():
    user_input = input("Your input here: ")
    result = convert(user_input)
    print(result)


if __name__ == "__main__":
    main()