import discord
from discord.ext import commands
import light_table
import random

'''
5 steps:
Class
Background
ability scores
alignment
remainder (name, gear, etc)'''
#Helpers for ability assignment
def assign_stats_random(stats):
    abilities = [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma",
    ]
    random.shuffle(stats)
    return dict(zip(abilities, stats))

#IMPORTANT: DO NOT KEEP IN VIEW ONCE DB IS MADE
CLASS_PRIORITIES = {
    "monk": ["Dexterity", "Wisdom", "Constitution"],
    "wizard": ["Intelligence", "Constitution", "Dexterity"],
    "rogue": ["Dexterity", "Constitution", "Wisdom"],
}

def assign_stats(stats, class_key):
    priorities = CLASS_PRIORITIES[class_key]
    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    stats = sorted(stats, reverse=True)

    assignment = {}

    # Assign highest stats to priority abilities
    for ability, score in zip(priorities, stats):
            assignment[ability] = score

    # Assign remaining stats arbitrarily (or later via UI)
    remaining_scores = stats[len(priorities):]
    remaining_abilities = [a for a in abilities if a not in assignment]

    for ability, score in zip(remaining_abilities, remaining_scores):
        assignment[ability] = score

    return assignment


class CreationNavView(discord.ui.View):
    def __init__(self, user, draft):
        super().__init__(timeout=300)
        self.user = user
        self.draft = draft

    async def interaction_check(self, interaction):
        return interaction.user.id == self.user.id

    @discord.ui.button(label="Class", style=discord.ButtonStyle.primary)
    async def class_step(self, interaction, button):
        await interaction.response.send_message(
            "Choose your class:",
            ephemeral=True,
            view=ClassChoiceView(self.user, self.draft),
        )


    @discord.ui.button(label="Background", style=discord.ButtonStyle.secondary)
    async def background(self, interaction, button):
        await interaction.response.send_message(
            "Background selection coming soon.",
            ephemeral=True,
        )

    @discord.ui.button(label="Ability Scores", style=discord.ButtonStyle.secondary)
    async def ability_scores(self, interaction, button):
        await interaction.response.send_message(
            "Choose how to determine ability scores:",
            ephemeral=True,
            view=AbilityScoreView(self.user, self.draft),
        )

    @discord.ui.button(label="Alignment", style=discord.ButtonStyle.secondary)
    async def alignment(self, interaction, button):
        await interaction.response.send_message(
            "Determine how subjective morality is",
            ephemeral=True,
            view=AlignmentView(self.user, self.draft),
        )

    @discord.ui.button(label="Details", style=discord.ButtonStyle.secondary)
    async def details(self, interaction, button):
        await interaction.response.send_message(
            "Character details coming soon.",
            ephemeral=True,
        )


'''1. Class
provide users a prompt to either choose their class or view the options, which displays the available classes and 
a short description of the classes with primary ability scores and subclasses'''

# db.py (or characterdata.py)

def get_classes():
    return [
        {
            "key": "monk",
            "name": "Monk",
            "description": (
                "**Monk**\n"
                "Primary Ability: Dexterity\n"
                "Fast martial artist using ki.\n"
                "Subclasses: Open Hand, Shadow, Four Elements"
            ),
        },
        {
            "key": "wizard",
            "name": "Wizard",
            "description": (
                "**Wizard**\n"
                "Primary Ability: Intelligence\n"
                "Arcane spellcaster with a spellbook.\n"
                "Subclasses: Evocation, Illusion, Necromancy"
            ),
        },
    ]


class ClassCarouselView(discord.ui.View):
    def __init__(self, user, draft, classes, index=0):
        super().__init__(timeout=180)
        self.user = user
        self.draft = draft
        self.classes = classes
        self.index = index


    def current_class(self):
        return self.classes[self.index]
    

    async def interaction_check(self, interaction):
        return interaction.user.id == self.user.id

    def current_class(self):
        return self.classes[self.index]

    async def update_message(self, interaction):
        data = self.current_class()
        await interaction.response.edit_message(
            content=data["description"],
            view=self,
        )

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.secondary)
    async def previous(self, interaction, button):
        self.index = (self.index - 1) % len(self.classes)
        await self.update_message(interaction)

    @discord.ui.button(label="Choose This Class", style=discord.ButtonStyle.success)
    async def choose(self, interaction, button):
        chosen = self.current_class()

        self.draft.class_key = chosen["key"]

        await interaction.response.send_message(
            f"You chose **{chosen['name']}**.",
            ephemeral=True,
            view=CreationNavView(self.user, self.draft),
        )
        self.stop()


    @discord.ui.button(label="Next", style=discord.ButtonStyle.secondary)
    async def next(self, interaction, button):
        self.index = (self.index + 1) % len(self.classes)
        await self.update_message(interaction)


class ClassModal(discord.ui.Modal):
    def __init__(self, draft):
        super().__init__(title="Choose Your Class")
        self.draft = draft

        self.choice = discord.ui.TextInput(
            label="Chosen class",
            placeholder="e.g. Monk, Wizard, Rogue",
            required=True,
        )
        self.add_item(self.choice)

    async def on_submit(self, interaction: discord.Interaction):
        chosen_class = self.choice.value.strip().lower()
        self.draft.class_key = chosen_class

        await interaction.response.send_message(
            f"You chose **{chosen_class.title()}**.",
            ephemeral=True,
            view=CreationNavView(interaction.user, self.draft),
        )


        
'''
Dropdown example
class ClassChoose(discord.ui.Select):
    def __init__(self, user):
        options = [
            discord.SelectOption(label="View Classes and input", value="new"),
            discord.SelectOption(label="input", value="old")
        ]
        super().__init__(placeholder="Choose an action", options=options)
        self.user = user

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(
                "This is not your session.",
                ephemeral=True
            )
            return

        choice = self.values[0]

        if choice == "new":
            await interaction.response.send_modal(ClassModal(mode="new"))
        elif choice == "old":
            await interaction.response.send_modal(ClassModal(mode="old"))'''


class ClassChoiceView(discord.ui.View):
    def __init__(self, user, draft):
        super().__init__(timeout=120)
        self.user = user
        self.draft = draft

    async def interaction_check(self, interaction):
        return interaction.user.id == self.user.id

    @discord.ui.button(label="View Classes", style=discord.ButtonStyle.success)
    async def view_classes(self, interaction, button):
        classes = get_classes()
        first = classes[0]
        await interaction.response.send_message(
            first["description"],
            ephemeral=True,
            view=ClassCarouselView(interaction.user, self.draft, classes,),
        )

    @discord.ui.button(label="Continue (Manual Entry)", style=discord.ButtonStyle.primary)
    async def continue_manual(self, interaction, button):
        await interaction.response.send_modal(ClassModal(self.draft))

'''
2. Background
provide users a prompt to either choose their race or view the options, which displays the available races and 
a short description of the races with their subraces, and ability increases and racial abilities

same for background, with potential to create one.

3. Ability scores
offer to perfrom 4d6 drop the lowest, then autoassign based off class. Requires class to be done for autoassign.
may allow users to input manually'''

class ManModalPrimary(discord.ui.Modal, title="Ability Scores (1/2)"):
    def __init__(self, draft):
        super().__init__()
        self.draft = draft
        self.str = discord.ui.TextInput(label="Strength")
        self.dex = discord.ui.TextInput(label="Dexterity")
        self.con = discord.ui.TextInput(label="Constitution")
        for item in (self.str, self.dex, self.con):
            self.add_item(item)

    async def on_submit(self, interaction: discord.Interaction):
        self.draft.stats = {
            "str": int(self.str.value),
            "dex": int(self.dex.value),
            "con": int(self.con.value),
        }

        #Respond with a message containing a button to open the next modal
        await interaction.response.send_message(
            "Primary stats saved. Click below to enter remaining stats.",
            ephemeral=True,
            view=EnterRemainingStatsButton(self.draft)
        )

class EnterRemainingStatsButton(discord.ui.View):
    def __init__(self, draft):
        super().__init__()
        self.draft = draft

    @discord.ui.button(label="Enter Remaining Stats", style=discord.ButtonStyle.primary)
    async def open_final_modal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ManModalFinal(self.draft))





class ManModalFinal(discord.ui.Modal, title="Ability Scores (2/2)"):
    def __init__(self, draft):
        super().__init__()
        self.draft = draft

        # Remaining three stats
        self.intel = discord.ui.TextInput(label="Intelligence", placeholder="e.g. 12")
        self.wis = discord.ui.TextInput(label="Wisdom", placeholder="e.g. 10")
        self.cha = discord.ui.TextInput(label="Charisma", placeholder="e.g. 8")

        for item in (self.intel, self.wis, self.cha):
            self.add_item(item)

    async def on_submit(self, interaction: discord.Interaction):
        # Update draft with final stats
        self.draft.stats.update({
            "int": int(self.intel.value),
            "wis": int(self.wis.value),
            "cha": int(self.cha.value),
        })

        # Confirm and return to creation nav
        await interaction.response.send_message(
            "Ability scores saved.",
            ephemeral=True,
            view=CreationNavView(interaction.user, self.draft),
        )


class AutoRollView(discord.ui.View):
    def __init__(self, user, draft):
        super().__init__(timeout=120)
        self.user = user
        self.draft = draft

    async def interaction_check(self, interaction):
        return interaction.user.id == self.user.id

    
    @discord.ui.button(label="Roll", style=discord.ButtonStyle.success)
    async def roll(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.do_roll(interaction)
    
    async def do_roll(self, interaction: discord.Interaction):
        self.rolls = light_table.roll_stats()
        self.draft.stats = self.rolls

        text = "**Rolled Ability Scores:**\n"
        text += ", ".join(str(x) for x in self.rolls)

        # If class already chosen → auto-assign
        if self.draft.class_key:
            assignment = assign_stats(self.rolls, self.draft.class_key)
            self.draft.assigned_stats = assignment

            text += "\n\n**Auto-Assigned based on Class:**\n"
            for ability, score in assignment.items():
                text += f"{ability}: {score}\n"

        else:
            assignment = assign_stats_random(self.rolls)
            self.draft.assigned_stats = assignment

            text += "\n\n**Auto-Assigned randomly:**\n"
            for ability, score in assignment.items():
                text += f"{ability}: {score}\n"
        
        total = sum(self.rolls)
        text += f"total is {total}"

        await interaction.response.edit_message(
            content=text,
            view=self,
        )

    

    #Can choose to reroll later
    @discord.ui.button(label="Reroll", style=discord.ButtonStyle.secondary)
    async def reroll(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.do_roll(interaction)

    @discord.ui.button(label="Confirm Scores", style=discord.ButtonStyle.primary)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.draft.stats:
            await interaction.response.send_message(
                "You must roll scores first.",
                ephemeral=True,
            )
            return

        await interaction.response.send_message(
            "Ability scores stored.",
            ephemeral=True,
            view=CreationNavView(self.user, self.draft),
        )
        self.stop()





class AbilityScoreView(discord.ui.View):
    def __init__(self, user, draft):
        super().__init__(timeout=120)
        self.user = user
        self.draft = draft

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.user.id

    @discord.ui.button(label="Roll Automatically", style=discord.ButtonStyle.success)
    async def roll(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Switch to AutoRollView, first response must be an edit_message
        await interaction.response.edit_message(
            content="Rolling ability scores automatically...",
            view=AutoRollView(self.user, self.draft),
        )

    @discord.ui.button(label="Roll and insert manually", style=discord.ButtonStyle.primary)
    async def manual(self, interaction: discord.Interaction, button: discord.ui.Button):
        #Must be the first response to this interaction
        await interaction.response.send_modal(ManModalPrimary(self.draft))

'''
4. Alignment
'''
class AlignmentOps(discord.ui.Button):
    def __init__(self, label: str, row: int):
        super().__init__(
            label=label,
            style=discord.ButtonStyle.primary,
            row=row,
            custom_id=f"alignment:{label.lower().replace(' ', '_')}",
        )

    async def callback(self, interaction: discord.Interaction):
        view: AlignmentView = self.view  # type: ignore

        view.draft.alignment = self.label

        await interaction.response.send_message(
            f"Alignment set to **{self.label}**.",
            ephemeral=True,
            view=CreationNavView(view.user, view.draft),
        )

        view.stop()


class AlignmentView(discord.ui.View):
    def __init__(self, user, draft):
        super().__init__(timeout=120)
        self.user = user
        self.draft = draft

        alignments = [
            ("Lawful Good", 0), ("Lawful Neutral", 0), ("Lawful Evil", 0),
            ("Neutral Good", 1), ("True Neutral", 1), ("Neutral Evil", 1),
            ("Chaotic Good", 2), ("Chaotic Neutral", 2), ("Chaotic Evil", 2),
        ]

        for label, row in alignments:
            print(type(discord.ui.Button), discord.ui.Button)
            self.add_item(AlignmentOps(label, row))

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.user.id
    


'''
5. Name, other details.
'''
