

def reverseString(input):
    if input == "":
        return ""

    return  reverseString(input[1:]) + input[0]


output = reverseString("harsh")
print(output)