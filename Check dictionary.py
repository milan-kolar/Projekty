colours = {"red":"červená", "green":"zelená", "blue":"modrá"}
numbers = {"one":"jedna", "two":"dvě", "three":"tři"}

def locate(key, value, dictionary):
    if dictionary.get(key) == None:
        print("Not found")
        return(False)
    elif dictionary.get(key) != value:
        return(False)
    else:
        return(True)

print(locate("yellow", "žlutá", colours))
print(locate("one", "jedna", numbers))
print(locate("green", "červená", colours))
print(locate("green", "zelená", colours))