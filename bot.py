""" Prototype of bot-assistant for maintaining phone book """

# validations for input parameters
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please, enter person name and phone."
        except KeyError:
            return "Person not found."
        except IndexError:
            return "Not applicable. Input parameter is missing."
        except Exception as e:
            return f'Error: {e}'

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    old_phone = contacts[name] 
    contacts[name] = phone

    return "Contact updated."
      
@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts[name]

    return phone

    
def show_all(contacts):
    if len(contacts) == 0:
        return "Phone book is empty."    
    else:
        return f"Contact list with users :\n{contacts}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))    
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()