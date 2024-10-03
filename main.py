from input import dict
input = ["GUD"]

i = 0
loop_bool = False
kina = 0
atlanten = 0

def loop(inputlist: list) -> tuple[list, bool]:
    global kina
    global atlanten
    returnlist = []
    done = True
    for obj in inputlist:
        if not obj == "Kina" and not obj == "Atlanten":
            obj = dict[obj]
            returnlist += obj
        elif obj == "Kina":
            kina += 1
        elif obj == "Atlanten":
            atlanten += 1
        done = False
    return (returnlist, done)

while loop_bool == False:
    newlist, _ = loop(input)
    print(_)
    loop_bool = _
    i += 1
    print(i)
    for item in newlist:
        print(item, end=",")
    print("")
    input = newlist


print(f"Kina: {kina}, Atlanten: {atlanten}")

from math import sqrt
print(f"sqrt_Kina: {round(sqrt(kina), 10)}, sqrt_Atlanten: {round(sqrt(atlanten), 10)}")
