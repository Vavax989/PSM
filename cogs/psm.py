import discord
from discord.ext import commands
from commands_library import ERLC_PRIVATE_SERVER_COMMANDS

class PSM(commands.Cog):
    """
    A cog for managing private server commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="execute")
    async def execute(self, ctx, command: str, *args):
        """
        Executes a private server command.
        Usage: ,execute <command> [arguments]
        """
        response = self.handle_command(command, args)
        await ctx.send(response)

    def handle_command(self, command, args):
        """
        Handles and executes a private server command.
        Args:
            command (str): The command to execute (e.g., ':kick').
            args (tuple): Arguments for the command.
        Returns:
            str: A response message (success or error).
        """
        for category, commands in ERLC_PRIVATE_SERVER_COMMANDS.items():
            if command in commands:
                cmd_details = commands[command]
                return (
                    f"Executing command: {command}\n"
                    f"Description: {cmd_details['description']}\n"
                    f"Example: {cmd_details['example']}\n"
                    f"Arguments Provided: {args if args else 'None'}"
                )
        return f"Error: Command '{command}' not found. Please use a valid command."


# Setup the cog
async def setup(bot):
    await bot.add_cog(PSM(bot))
