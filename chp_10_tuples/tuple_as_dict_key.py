if __name__ == '__main__':
    phoneNumbers = {
        ("Ahmad", "Amin"): "03033912903",
        ("Usama", "Ashraf"): "03006797007",
        ("Numan", "Shakir"): "03489899248",
    }
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    for i in phoneNumbers.keys():
        print(firstName+ " "+lastName +": "+phoneNumbers[firstName,lastName])
