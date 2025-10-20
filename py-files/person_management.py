class Person:
    def __init__(self, name, surname, age, job):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job


people = []

while True:
    print("\n=== MENU ===")
    print("1 - Add Person")
    print("2 - Show All")
    print("3 - Delete Person")
    print("4 - Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        name = input("Name: ")
        surname = input("Surname: ")
        age = input("Age: ")
        job = input("Job: ")
        
        p = Person(name, surname, age, job)
        people.append(p)
        print("It is added!")
    
    elif choice == "2":
        if len(people) == 0:
            print("List is empty.")
        else:
            print("Person management list:\n")
            for i in range(len(people)):
                print(f"{i+1}. {people[i].name} {people[i].surname} - {people[i].age} - {people[i].job}")
    
    elif choice == "3":
        if len(people) == 0:
            print("List is empty.")
        else:
            for i in range(len(people)):
                print(f"{i+1}. {people[i].name} {people[i].surname}")
            
            num = int(input("the number to be deleted: "))
            
            if num > 0 and num <= len(people):
                people.pop(num - 1)
                print("It is deleted!")
            else:
                print("There is no such number to be deleted!")
    
    elif choice == "4":
        print("Exiting from program,bye!")
        break
    
    else:
        print("Wrong choice!, please enter a menu choice as mentioned above ")