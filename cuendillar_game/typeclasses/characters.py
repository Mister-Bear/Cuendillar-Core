"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game.
"""

from evennia.objects.objects import DefaultCharacter
from .objects import ObjectParent
from commands.cmdsets import CharacterCmdSet  # <- this must point to the right place

class Character(ObjectParent, DefaultCharacter):
    """
    The Character class for Cuendillar: Reforged.
    """
    def at_object_creation(self):
        super().at_object_creation()
        self.cmdset.add(CharacterCmdSet, permanent=True)
