
with open("text.txt", "w") as file:
    file.write("""-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
""")

signs = ["-", ",", ".", "!", "?"]
with open("text.txt", "r") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = " ".join(reversed(line.strip().split()))
            for sign in signs:
                result = result.replace(sign, "@")
            print(result)