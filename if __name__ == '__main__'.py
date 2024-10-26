#if __name__ == __main__: (this script can be imported OR run standalone)
#                           functions and classes in this module can be resused
#                           without the main block of code executing
#Good practice (code is modular,
#               helps readability,
#               leaves no global variables,
#               avoid unintended execution)

# ex. library = Import library for functionality
#               when running library directly, display a help page

#def main():
    # Your program goes here

#if __name__ == '__main__':
#    main()

#print(dir())
#print(__name__)

def favorite_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is a script")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()