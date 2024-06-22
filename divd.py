

def divd(a,b):
    # i want a/b to have precision of 6
    return (a/b)


def divdivd(a,b):
    return divd(a,b) / b

print(divdivd(1,3))