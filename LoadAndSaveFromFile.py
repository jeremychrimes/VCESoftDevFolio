def checkInterger(val):
    try:
        val = int(val)
        return True
    except:
        return False

print("Software Development People Database")

mainMenuOptions = ["Add", "List", "Modify"]

people = list()


for key, item in enumerate(mainMenuOptions):
    print("{0}. {1}".format(key, item))

def clientadd():
    person = list()
    name = str(input("What is the person's name? "))
    person.append(name)
    ageInputted = False
    while ageInputted is not True:
        age = input("How old is {}: ".format(name))
        ageintChecked = checkInterger(age)
        if (ageintChecked == True):
            person.append(int(age))
            ageInputted = True
    genderInputted = False
    while genderInputted is not True:
        gender = input("What Gender is {0}: ".format(name))
        if gender.lower() == "MALE":
            person.append("MALE")
            genderInputted = True
        elif gender.upper() == "FEMALE":
            person.append("FEMALE")
            genderInputted = True
    people.append(person)
clientadd()
