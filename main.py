import turtle


def main():
    print("hello")
    # for loops
    num = 9
    for val in range(0, num):
        print(val)
    for val in range(num):
        print(val)

    # step values
    # will go in intervals of 2, keep in mind second value is always exclusive
    for val in range(0, 22, 2):
        print(val)

    # turle iteration
    bob = turtle.Turtle()
    for side in range(3):
        bob.forward(50)
        bob.left(90)

    # loop through string
    sentence = "This is a string bro"
    for character in sentence:
        print(character)
    # or can loop through this way
    print("\n")
    another_sentence = "another string my dude"
    for index in range(0, len(another_sentence)):
        print(another_sentence[index])

    # while loops
    total = 0
    increase_by = 14
    while total < 1000:
        total += increase_by
        print(total)

    # ending loops with break statements
    for iteration in range(42):
        print('This is iteration number:', iteration+1)
        if iteration > 4:
            break
        print("The loop is done!")


if __name__ == "__main__":
    main()
