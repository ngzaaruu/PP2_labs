def reverse():
    a = input("Enter: ")
    words = a.split()
    reversed_sentence = " ".join(reversed(words))
    print("Reversed: ", reversed_sentence)

reverse()

