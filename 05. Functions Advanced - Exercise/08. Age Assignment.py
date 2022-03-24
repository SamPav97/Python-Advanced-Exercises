def age_assignment(*args, **kwargs):

    dict = {}
    for k, v in kwargs.items():
        for name in args:
            if name.startswith(k):
                dict[name] = v
    return dict


print(age_assignment("Peter", "George", G=26, P=19))