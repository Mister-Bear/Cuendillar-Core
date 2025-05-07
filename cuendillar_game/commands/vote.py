from evennia import Command
from evennia.utils import search
import time

class CmdVote(Command):
    """
    Vote to give XP to another player.

    Usage:
      +vote <target>

    Example:
      +vote Saidin
    """

    key = "+vote"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if not self.args:
            caller.msg("Usage: +vote <target>")
            return

        target_name = self.args.strip()
        target = search.object_search(target_name)
        if not target:
            caller.msg(f"Could not find '{target_name}'.")
            return
        target = target[0]

        if caller == target:
            caller.msg("You cannot vote for yourself.")
            return

        now = time.time()
        last_votes = caller.db.last_votes or {}

        # Check daily limit
        today = time.strftime("%Y-%m-%d", time.gmtime(now))
        daily_votes = caller.db.daily_vote_count or {}
        votes_today = daily_votes.get(today, 0)

        if votes_today >= 4:
            caller.msg("You have used all 4 of your votes for today. Come back tomorrow!")
            return

        # Check if already voted for this player today
        voted_today = last_votes.get(today, [])
        if target.key in voted_today:
            caller.msg(f"You have already voted for {target.key} today.")
            return

        # Check cooldown (30 minutes between votes)
        last_vote_time = caller.db.last_vote_time or 0
        if now - last_vote_time < 1800:
            mins_left = int((1800 - (now - last_vote_time)) / 60)
            caller.msg(f"You must wait {mins_left} more minutes before voting again.")
            return

        # Give XP
        current_xp = target.db.xp or 0
        target.db.xp = current_xp + 0.5  # Each vote gives 0.5 XP

        # Update vote records
        voted_today.append(target.key)
        last_votes[today] = voted_today
        caller.db.last_votes = last_votes

        daily_votes[today] = votes_today + 1
        caller.db.daily_vote_count = daily_votes

        caller.db.last_vote_time = now

        # Messages
        caller.msg(f"You have voted for {target.key} and awarded them 0.5 XP!")
        target.msg(f"You have received 0.5 XP from {caller.key}'s vote!")

