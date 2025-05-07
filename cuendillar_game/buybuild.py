from evennia import Command

class CmdBuyBuildInput(Command):
    """
    Handles number input during +buybuild character creation.
    """

    key = "buybuildinput"
    aliases = ["1", "2", "3", "4", "5"]
    locks = "cmd:attr(buybuild_in_progress, True)"
    help_category = "Character Generation"

    def parse(self):
        self.input = self.args.strip()

    def func(self):
        caller = self.caller
        choice = self.input

        if not choice:
            caller.msg("|rPlease type a number to choose an option.|n")
            return

        if choice == "1":
            caller.msg("|wYou chose: Allocate Core Stats! (Coming soon!)|n")
            # TODO: Add Core Stats allocation logic here

        elif choice == "2":
            caller.msg("|wYou chose: Allocate One Power Attributes! (Coming soon!)|n")
            # TODO: Add One Power attribute allocation logic here

        elif choice == "3":
            caller.msg("|wYou chose: Learn Skills! (Coming soon!)|n")
            # TODO: Add Skills learning logic here

        elif choice == "4":
            caller.msg("|wYou chose: Flaws and Advantages! (Coming soon!)|n")
            # TODO: Add Flaws and Advantages logic here

        elif choice == "5":
            caller.db.character_setup_ready = True
            caller.ndb.buybuild_in_progress = False
            caller.msg("|gCharacter build complete! You may now play.|n")

        else:
            caller.msg("|rInvalid choice. Please enter a number from the list.|n")
