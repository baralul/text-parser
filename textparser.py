filename = "text.txt"
i = 0
output = ""

# Open the file for reading
with open(filename, 'r') as f:
    # Read the contents of the file
    text = f.read()
    while i < len(text):
        if text[i] == "(":
            i += 1
            while i < len(text) and text[i] != ")":
                output += text[i]
                i += 1
            print(output)
        i += 1
        output = ""
