def add_contact(args, contacts):
    if len(args) != 2:
        return "❌ Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return f"✅ Contact '{name}' added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "❌ Please provide name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"🔁 Contact '{name}' updated."
    else:
        return f"⚠️ Contact '{name}' not found."


def get_phone(args, contacts):
    if len(args) != 1:
        return "❌ Please provide a name to search."
    name = args[0]
    if name in contacts:
        return f"📞 {name}: {contacts[name]}"
    else:
        return f"⚠️ Contact '{name}' not found."


def show_all(contacts):
    if not contacts:
        return "📭 No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args

def main():
    contacts = {}
    print("🤖 Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("👋 Good bye!")
            break
        elif command == "hello":
            print("💬 How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("❓ Unknown command. Try again.")


if __name__ == "__main__":
    main()