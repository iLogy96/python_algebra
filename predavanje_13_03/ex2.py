def checkIfTrue(list, string):
    i = 0
    while i < len(list):
        if string != list[i]:
            print(f"{list[i]} isn't equal to the given string: {string}")
            break
        i += 1
    else:
        print("All items are the same as given string")


checkIfTrue(["Random", "Random", "asgasga", "Random"], "Random")
