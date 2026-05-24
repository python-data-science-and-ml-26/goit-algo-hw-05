
class DuplicatedKeyError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Please provide both name and phone number."
        except IndexError:
            return "Error: Please provide a name."
        except KeyError:
            return "Error: Contact not found."
        except DuplicatedKeyError:
            return "Error: Contact with this name already exists."

    return inner



def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()

    if not cmd:
        return "", []
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        raise DuplicatedKeyError
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
        name, phone = args

        if name not in contacts:
            raise KeyError

        contacts[name] = phone
        return "Contact updated."


@input_error
def find_contact(args, contacts):
    name = args[0]

    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


def list_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

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
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


