from evennia import Command

class CmdRemoveContact(Command):
    """
    Remove an existing contact.

    Usage:
      +removecontact <Name>

    Example:
      +removecontact Tamra
    """

    key = "+removecontact"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        name = self.args.strip()

        if not name:
            caller.msg("Usage: +removecontact <Name>")
            return

        contacts = caller.db.contacts or {}

        if name in contacts:
            del contacts[name]
            caller.db.contacts = contacts
            caller.msg(f"Removed contact: {name}")
        else:
            caller.msg(f"No contact named {name} found.")
