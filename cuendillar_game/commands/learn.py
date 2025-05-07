from evennia import Command
from commands.skills import skills  # Import the master skill list!

class CmdLearn(Command):
    """
    Learn a new skill or improve an existing skill by spending XP.

    Usage:
      +learn <skillname>

    Example:
      +learn Swordplay
    """

    key = "+learn"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if not self.args:
            caller.msg("Usage: +learn <skillname>")
            return

        skill_name = self.args.strip().title()

        # Search the full skills list
        skill_entry = next((s for s in skills if s["name"].lower() == skill_name.lower()), None)

        if not skill_entry:
            caller.msg(f"The skill '{skill_name}' does not exist.")
            return

        # Check if already has the skill
        char_skills = caller.db.skills or {}
        current_level = char_skills.get(skill_entry["name"], 0)

        if current_level >= 5:
            caller.msg(f"You have already mastered {skill_name} at 5 dots!")
            return

        # Calculate XP cost
        next_level = current_level + 1
        xp_cost = next_level * 3  # (Level x 3 XP)

        # Check XP
        if not caller.db.xp or caller.db.xp < xp_cost:
            caller.msg(f"Not enough XP. {skill_name} costs {xp_cost} XP to learn or upgrade.")
            return

        # Deduct XP and upgrade skill
        caller.db.xp -= xp_cost
        char_skills[skill_entry["name"]] = next_level
        caller.db.skills = char_skills  # Save it back

        caller.msg(f"You have learned or improved {skill_name} to level {next_level}! (-{xp_cost} XP)")
