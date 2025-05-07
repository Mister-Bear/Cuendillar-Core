from evennia import Command

class CmdAddContact(Command):
    """
    Add a new important contact.

    Usage:
      +addcontact <Name> = <Description>

    Example:
      +addcontact Tamra = Wise Aes Sedai mentor
    """

    key = "+addcontact"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if "=" not in self.args:
            caller.msg("Usage: +addcontact <Name> = <Description>")
            return

        name, desc = [part.strip() for part in self.args.split("=", 1)]

        contacts = caller.db.contacts or {}
        contacts[name] = desc
        caller.db.contacts = contacts

        caller.msg(f"Added contact: {name}")
