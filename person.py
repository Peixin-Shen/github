Dict={"A":50, "B":60, "C":70}
print(Dict)

def eat(name):
    Dict[name]+=1
    # return Dict[name]

def exercise(name):
    Dict[name]+=-1
    return Dict[name]

def speack(name):
    print(name,Dict[name])


speack("A")
eat('A')
speack("A")
