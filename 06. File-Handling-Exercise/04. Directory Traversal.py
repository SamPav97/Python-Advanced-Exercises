from os import listdir, path


def traverse_dir(current, files_by_ext):
    for element in listdir(current):
        if path.isdir(path.join(current, element)):
            traverse_dir(path.join(current, element), files_by_ext)
        else:
            extension = element.split(".")[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_ext = {}
traverse_dir(".", files_by_ext)

with open("result.txt", "w") as output:
    for ext, files in sorted(files_by_ext.items()):
        output.write(f".{ext}\n")
        for file in sorted(files):
            output.write(f"--- {file}\n")
