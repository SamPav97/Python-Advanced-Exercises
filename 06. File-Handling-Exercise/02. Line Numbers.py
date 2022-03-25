import string

with open("text.txt", "r") as file:
    lines = []
    row = 0
    for line in file.readlines():
        punct = len([pun for pun in line if pun in string.punctuation])
        letters = len([i for i in line if i.isalpha()])
        row += 1
        lines += [f"Line {row}: {''.join(line.strip())} ({letters}) ({punct})"]
    with open("output.txt", "w") as output_file:
        output_file.write("\n". join(lines))