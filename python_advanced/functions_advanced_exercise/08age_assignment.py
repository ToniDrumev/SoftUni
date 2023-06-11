def age_assignment(*args, **kwargs):
    age_by_names = {}
    result = []

    for name in args:
        if name[0] in kwargs:
            age_by_names[name] = kwargs[name[0]]

    for key, value in sorted(age_by_names.items(), key=lambda x: x[0]):
        result.append(f"{key} is {value} years old.")

    return "\n".join(result)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))