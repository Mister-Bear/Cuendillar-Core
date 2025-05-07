from evennia import Command

class CmdBuyBuild(Command):
    """
    Starts character build process.
    Usage:
        +buybuild
        +buybuild reset
    """
    key = "+buybuild"

    def func(self):
        if self.args.strip().lower() == "reset":
            self.caller.ndb.buybuild_step = None
            self.caller.ndb.buybuild_data = {}
            self.caller.msg("|rBuyBuild session reset.|n")
            return

        if not self.caller.ndb.buybuild_step:
            self.caller.ndb.buybuild_step = "choose_class"
            self.caller.ndb.buybuild_data = {}
            self.show_class_options()
            return

        step = self.caller.ndb.buybuild_step
        text = self.args.strip()

        # Class selection
        if step == "choose_class":
            if text == "1":
                self.caller.ndb.buybuild_data["class"] = "Warrior"
            elif text == "2":
                self.caller.ndb.buybuild_data["class"] = "Rogue"
            elif text == "3":
                self.caller.ndb.buybuild_data["class"] = "Channeler"
            else:
                self.caller.msg("|rInvalid choice. Please type 1, 2, or 3.|n")
                return

            chosen = self.caller.ndb.buybuild_data["class"]
            self.caller.msg(f"You selected |c{chosen}|n.\n")
            if chosen == "Channeler":
                self.caller.ndb.buybuild_step = "assign_power_strength"
                self.prompt_power_strength()
            else:
                self.caller.ndb.buybuild_step = "assign_str"
                self.prompt_stat("STR")
            return

        # Channeler flow
        if step == "assign_power_strength":
            if not text.isdigit() or not (1 <= int(text) <= 15):
                self.caller.msg("|rEnter a number between 1 and 15.|n")
                return
            self.caller.ndb.buybuild_data["power_strength"] = int(text)
            self.caller.ndb.buybuild_step = "assign_control"
            self.prompt_control()
            return

        if step == "assign_control":
            if not text.isdigit() or not (1 <= int(text) <= 5):
                self.caller.msg("|rEnter a number between 1 and 5.|n")
                return
            self.caller.ndb.buybuild_data["power_control"] = int(text)
            self.caller.ndb.buybuild_step = "assign_affinities"
            self.prompt_affinities()
            return

        if step == "assign_affinities":
            elements = text.lower().split(",")
            allowed = {"air", "water", "earth", "fire", "spirit"}
            chosen = set(e.strip() for e in elements if e.strip() in allowed)
            if not chosen:
                self.caller.msg("|rPlease enter at least one valid affinity (comma-separated).|n")
                return
            self.caller.ndb.buybuild_data["affinities"] = list(chosen)
            self.caller.ndb.buybuild_step = "assign_str"
            self.prompt_stat("STR")
            return

        # Stat flow
        if step.startswith("assign_"):
            stat = step.replace("assign_", "").upper()
            if not text.isdigit() or not (1 <= int(text) <= 10):
                self.caller.msg("|rEnter a number between 1 and 10.|n")
                return
            self.caller.ndb.buybuild_data[stat] = int(text)

            next_stat = self.next_stat(stat)
            if next_stat:
                self.caller.ndb.buybuild_step = f"assign_{next_stat.lower()}"
                self.prompt_stat(next_stat)
            else:
                self.finalize_build()
            return

    # --- Helper functions ---
    def show_class_options(self):
        msg = "|cChoose your class:|n\n"
        msg += " 1) Warrior\n"
        msg += " 2) Rogue\n"
        msg += " 3) Channeler\n"
        msg += "Type the number of your choice:"
        self.caller.msg(msg)

    def prompt_stat(self, stat):
        self.caller.msg(f"|cAssign value to {stat}|n (1–10):")

    def prompt_power_strength(self):
        self.caller.msg("|cAssign your Power Strength|n (1–15):")

    def prompt_control(self):
        self.caller.msg("|cAssign your Control|n (1–5):")

    def prompt_affinities(self):
        self.caller.msg("|cEnter your elemental affinities|n (comma-separated: air, water, earth, fire, spirit):")

    def next_stat(self, current):
        order = ["STR", "DEX", "CON", "WIT", "INT", "CHA"]
        idx = order.index(current)
        return order[idx + 1] if idx + 1 < len(order) else None

    def finalize_build(self):
        data = self.caller.ndb.buybuild_data
        for key, val in data.items():
            self.caller.db.attributes.add(key.lower(), val)
        self.caller.db.character_setup_ready = True
        self.caller.msg("|gCharacter setup complete! You may now proceed to the next room.|n")
