import discord
from discord.ext import commands
from pretty_help import Navigation, PrettyHelp

from asyncio import sleep
import os
import random

bot = commands.Bot(command_prefix="$", description="Simple economy bot")
