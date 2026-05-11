# In deep.py, implement a program that prompts the user for the answer
#  to the Great Question of Life, the Universe and Everything,
#  outputting Yes if the user inputs 42 or (case-insensitively)
#  forty-two or forty two. Otherwise output No.


def main():
    user_input = input("What is the answer to the great question? ")
    print(deep(user_input))


def deep(que):
    que = que.lower().strip()
    if que == "42" or que == "forty-two" or que == "forty two":
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    main()
