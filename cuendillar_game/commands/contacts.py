from evennia import Command

class CmdContacts(Command):
    """
    View, add, or remove important contacts.

    Usage:
      +contacts
      +contacts/add <Name> = <Description>
      +contacts/remove <Name>

    Examples:
      +contacts
      +contacts/add Tamra = Wise Aes Sedai mentor
      +contacts/remove Tamra
    """

    key = "+contacts"
    aliases = ["+contacts/add", "+contacts/remove"]
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        raw_input = self.raw_string.strip() if hasattr(self, "raw_string") else self.args.strip()

        # No arguments: Just show all contacts
        if not raw_input or raw_input.lower() == "+contacts":
            contacts = caller.db.contacts or {}
            if not contacts:
                caller.msg("You have no contacts set.")
                return
            msg = "=== CONTACTS ===\n"
            for name, desc in contacts.items():
                msg += f"{name}: {desc}\n"
            caller.msg(msg.strip())
            return

        # Handle +contacts/add
        if raw_input.lower().startswith("+contacts/add "):
            try:
                content = raw_input[len("+contacts/add "):]
                name, description = [part.strip() for part in content.split("=", 1)]
            except ValueError:
                caller.msg("Usage: +contacts/add <Name> = <Description>")
                return

            contacts = caller.db.contacts or {}
            contacts[name] = description
            caller.db.contacts = contacts
            caller.msg(f"Added contact: {name}")
            return

        # Handle +contacts/remove
        if raw_input.lower().startswith("+contacts/remove "):
            name = raw_input[len("+contacts/remove "):].strip()
            contacts = caller.db.contacts or {}

            if name in contacts:
                del contacts[name]
                caller.db.contacts = contacts
                caller.msg(f"Removed contact: {name}")
            else:
                caller.msg(f"No contact named {name} found.")
            return

        # Otherwise: bad input
        caller.msg("Unknown subcommand. Use +contacts, +contacts/add, or +contacts/remove.")
