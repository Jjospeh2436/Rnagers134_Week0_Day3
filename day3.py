


def voter_age(num):
    if num < 18:
        print("kid")
        if num < 1 and num >= 0:
            print("Just a little baby")
        elif num < 0:
            print("Quit messing with me!")
    elif num > 18 and num < 64:
        print("adult")
    else:
        print("senior")

voter_age(15)
voter_age(19)
voter_age(85)
voter_age(0)
voter_age(-85)

names = ["Javier", "Ben", "Kym", "Grace", "Michael"]

for name in names:
    print(name)
    last = input("What is your last name?  ")
    x = f"This is you full name: {name.title()} {last.title()}"
    print(f'\t{x}')


def full_name():
    first = input("What is your first name? ")
    sec = input("What is your last name? ")
    print(first.title() + " " + sec.title())

full_name()


def name_list(lis):
    for l in lis:
        print(l.title() + " . . . last name unknown")

name_list(names) 