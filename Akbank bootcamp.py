#Defining part for class
class Library():



    def __init__(self):
        try:
            file = open("books.txt", "r")

        except FileNotFoundError:           #To check whether the file exist,ı use try and except block
            file = open("books.txt", "w")
            file.close()

        file = open("books.txt","r")
        information = []
        for i in file.readlines():           #I read the information in the txt file and hold them in a list called informations
            x = i.strip("\n")                #Of course ı convert them to proper strings and put them to the list after that.
            x = x.split(",")
            information.append(x)
        self.information = information
        file.close()




    def list_books(self):
        try:
            for i in self.information:                           #Instead of reading txt file one more time,ı use the list above
                print("Book: {} , Author: {}".format(i[0],i[1]))
        except IndexError:
            print("There is no book in the library")             #Encountered some problems during improving process so added for just safety.

    def add_book(self):
        x1 = input("Please write the name of the book which you want to add the library")      #I  take information from user and send them to new variables.
        x2 = input("Please write the author of the book which you want to add the library")
        x3 = input("Please write the release date of the book which you want to add the library")
        x4 = input("Please write the page number of the book which you want to add the library")
        new_book = [x1,x2,x3,x4]            #I create a new list with my variables
        new_book = ",".join(new_book)
        file = open("books.txt","a")
        file.write("{}\n".format(new_book)) #I convert them to string and write them to the file
        file.close()
        self.__init__()
        print("The book has been added successfully.")  #I close the file and execute self.init() because my information list might change.

    def remove_book(self):
        removing_book = None
        x1 = input("Please write the name of the book which you want to remove the library")
        for i in self.information:
            if (i[0] == x1):
                removing_book = (self.information).index(i)     #User give a name and ı look for the name in the list by using for.
                print(removing_book)                             #If a find it ı assign index number to my variable.
                (self.information).pop(removing_book)           #Delete it from my list and write my list to the file from beginning.
                with open("books.txt","w") as file:
                    for i in self.information:
                        x = ",".join(i)+"\n"
                        file.write(x)
                print("The book has been removed successfully.")
        file.close()
        if (removing_book == None):
            print("The book which you wanted to remove doesn't exist.")   #The error part and executing part for self.init()
        self.__init__()




lib = Library()

#Creating part of the menu



while True:

    print("\n***Menu***\n1-)List Book\n2-)Add Book\n3-)Remove Book\n\nNote:If you want to close the menu please press x\n")

    demand = input("Please choose what you want to do.")

    if(demand == ("1" or "List Books")):
        lib.list_books()
    elif(demand ==  ("2" or "Add Book")):                                   #Depending on the input,menu executes different methods of the library.
        lib.add_book()
    elif(demand ==  ("3" or "Remove Book")):
        lib.remove_book()
    elif(demand == "x"):
        print("The Menu has been closed.")
        break
    else:
        print("Please write your input correctly")
