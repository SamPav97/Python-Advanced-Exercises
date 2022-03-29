
def start_spring(**kwargs):
    new_dic = {}
    for k, v in kwargs.items():
        if v not in new_dic.keys():
            new_dic[v] = []
        new_dic[v].append(k)

    for k, v in new_dic.items():
        new_dic[k] = sorted(v)

    new_dic = {k: v for k, v in sorted(new_dic.items(), key=lambda x: (-len(x[1]), x[0]))}

    for k, v in new_dic.items():
        new_dic[k] = [f"-{f}" for f in v]

    n = "\n"
    final_list = []
    for s in range(len(new_dic.keys())):
        final_list.append(f"{list(new_dic.keys())[s]}:\n{n.join(list(new_dic.values())[s])}")

    return f"{n.join(final_list)}"


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

