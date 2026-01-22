import discordbot
import discord
from discord import app_commands
from discord.ext import commands
import light_table
import random_table
import charactercreator


intents = discord.Intents.default()
intents.message_content = True  # Required for some interactions if you use ctx messages

#setup-
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

bot = MyBot()
TOKEN = discordbot.getToken()


@bot.event
async def on_ready():
    await bot.tree.sync()  # Register slash commands
    print(f"Bot connected as {bot.user}")

#/roll
@bot.tree.command(name="roll", description="Roll dice")
@app_commands.describe(num="Number of dice", dtype="Type of die (e.g., 6 for d6)")
async def roll(interaction: discord.Interaction, num: int, dtype: int):
    rolls = [light_table.d(dtype) for _ in range(num)]
    total = sum(rolls)
    await interaction.response.send_message(
        f"Rolls: {rolls}\nTotal: {total}"
    )

#/forecast
@bot.tree.command(name="forecast", description="Generate a week of weather")
@app_commands.describe(start_day="Starting day number", days="Number of days (max 7)", start_temp="Starting temperature")
async def forecast(interaction: discord.Interaction, start_day: int, days: int, start_temp: int):
    value = light_table.forecast([], days, start_temp)
    if value == 1:
        await interaction.response.send_message("1 week maximum forecast")
        return

    weekweather = value
    msg = "\n".join(f"{start_day + i} {str(weekweather[i])}" for i in range(days))
    await interaction.response.send_message(msg)

#/encounter
@bot.tree.command(name="encounter", description="Generate a random encounter")
@app_commands.describe(area="Encounter location", level="Difficulty level")
@app_commands.choices(
    area=[
        app_commands.Choice(name="Brongalv", value="brongalv"),
        app_commands.Choice(name="Orc", value="orc"),
        app_commands.Choice(name="Cryomiir", value="cryomiir"),
        app_commands.Choice(name="Dale", value="dale")
    ],
    level=[
        app_commands.Choice(name="Low", value="low"),
        app_commands.Choice(name="Mid", value="mid")
    ]
)
async def encounter(interaction: discord.Interaction, area: str, level: str):
    comproll = light_table.d(6)
    complication = random_table.compilcationTable(comproll)
    behroll = light_table.d(6)
    behavior = random_table.behaviorTable(behroll)
    encountroll = light_table.d(6)

    if area == "brongalv":
        encounter_val = random_table.brongalvTable(encountroll)
    elif area == "orc":
        encounter_val = random_table.orkTable(encountroll)
    elif area == "cryomiir":
        encounter_val = random_table.cryomiirTable(encountroll)
    elif area == "dale":
        encountroll = light_table.d(100)
        if level == "low":
            encounter_val = random_table.daleTableLow(encountroll)
        else:
            encounter_val = random_table.daleTableMid(encountroll)
    else:
        await interaction.response.send_message(
            "Supported tables: brongalv, cryomiir, orc, dale low, dale mid"
        )
        return

    msg = f"Encounter: {encounter_val}\nBehavior: {behavior}\nComplication: {complication}"
    await interaction.response.send_message(msg)

#/randomtime
@bot.tree.command(name="randomtime", description="Generate random encounter times")
@app_commands.describe(num="Number of encounters (max 6)")
async def randomtime(interaction: discord.Interaction, num: int):
    schedule = "Encounters at " + light_table.encounterTime(num)
    await interaction.response.send_message(schedule)

#/createday
@bot.tree.command(name="createday", description="Generate encounters for a day")
@app_commands.describe(place="Encounter location", num="Number of encounters (max 6)")
async def createday(interaction: discord.Interaction, place: str, num: int):
    day_schedule = light_table.encounterGenerator(place, num)
    await interaction.response.send_message(day_schedule)

#/generatehoard
@bot.tree.command(name="generatehoard", description="Generate treasure hoard")
@app_commands.describe(level="Hoard level (integer)")
async def generatehoard(interaction: discord.Interaction, level: int):
    item = light_table.hoard(level)
    await interaction.response.send_message(item)

#Helper for class selection
@bot.tree.command(name="chooseclass", description="Choose your character class")
async def chooseclass(interaction: discord.Interaction):
    await interaction.response.send_message(
        "How would you like to choose your class?",
        ephemeral=True,
        view=charactercreator.ClassChoiceView(interaction.user, ),
    )

#/create
class CharDraft:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.race = None
        self.subrace_choice = {}
        self.subrace = None
        self.stats = None #determined in charactercreator Ability Score view
        self.class_key = None #determined in charactercreator classview
        self.assigned_stats = None
        self.alignment = None

class CharacterCreatorView(discord.ui.View):
    def __init__(self, user: discord.User):
        super().__init__(timeout=600)
        self.user = user
        self.draft = CharDraft(user.id)
        self.steps = []

    '''async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.user.id  # Lock to the user'''
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(
                "This is not your session.", emphemral = True
            )
            return False
        return True

    @discord.ui.button(label="Class", style=discord.ButtonStyle.primary)
    async def dndclass(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Choose your character's class.", ephemeral=True, view=charactercreator.ClassChoiceView(interaction.user),
        )

    @discord.ui.button(label="Background", style=discord.ButtonStyle.primary)
    async def background(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Determine your character's race and background.", ephemeral=True
        )

    @discord.ui.button(label="Ability Scores", style=discord.ButtonStyle.primary)
    async def asi(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Manually roll and assign ability scores or have them automatically rolled and assigned.\nAutomatic assignment requires class to be selected.", ephemeral=True
        )

    @discord.ui.button(label="Alignment", style=discord.ButtonStyle.primary)
    async def alignment(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Determine how subjective morality is to you.", ephemeral=True
        )

    @discord.ui.button(label="Details", style=discord.ButtonStyle.primary)
    async def detail(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Fill out the rest of your character.", ephemeral=True
        )

    @discord.ui.button(label="Finish", style=discord.ButtonStyle.green)
    async def finish(self, interaction: discord.Interaction, button):
        #Check to make sure that all of the fields have been filled out
        await interaction.response.send_message("Character creation finished!", ephemeral=True)
        self.stop()

    async def on_timeout(self):
        pass

@bot.tree.command(name="create", description="Enter character creator")
async def create(interaction: discord.Interaction):
    draft = CharDraft(interaction.user.id)

    await interaction.response.send_message(
        "Entering character creator...",
        view=charactercreator.CreationNavView(interaction.user, draft), 
        ephemeral=True
    )


#run the bot
bot.run(TOKEN)