#x is the result of a d100 roll, tables meant to be used as a way to find items
#All tables from 5e DMG
import light_table

def windandpercip(x):
    if x <= 8:
        condition = "None"
    elif x > 8 and x <= 13:
        condition = "Light"
    else:
        condition = "Heavy"
    return condition

def temperature(x, avgtemp, wind, perc):
    if x <= 11:
        temp = avgtemp
    elif x > 9 and x <= 14:
        if perc == "Heavy" and wind == "Heavy":
            temp = avgtemp
        else:
            temp = avgtemp+10
    else:
        temp = avgtemp-10
    return temp

def daleTableLow(x):
    encounterList = ["a Giant Owl","Goblins","Goblins","Goblins","Goblins",
                     "Area Hunters","Area Hunters","Area Hunters","Owl","Owl","Blood Hawks",
                     "Blood Hawks","Orcs","Orcs","Orcs","Orcs","Orcs",
                     "Kobolds and Winged Kobold","Kobolds and 2 Winged Kobolds",
                     "Kobolds and 3 Winged Kobolds", "Partially eaten corpse","Partially eaten corpse",
                     "Partially eaten corpse","Partially eaten corpse","Partially eaten corpse","Hunters",
                     "Hunters","Hunters","Hunters","Half Ogre","Half Ogre","Half Ogre","Half Ogre","Half Ogre",
                     "Half Ogre","Tracks in the snow","Tracks in the snow","Tracks in the snow","Tracks in the snow",
                     "Tracks in the snow","Ice Mephit","Ice Mephits","Ice Mephits","Ice Mephits","1 Ice Mephit",
                     "Brown Bear","Brown Bear","Brown Bear","Brown Bear","Brown Bear","Orcs","Orcs","Orcs","Polar Bear",
                     "Polar Bear","Brongalv Hunters","Brongalv Hunters","Saber Toothed Tiger","Saber Toothed Tiger",
                     "Saber Toothed Tiger","Frozen pond with recent hole","Frozen pond with recent hole","Frozen pond with recent hole",
                     "Frozen pond with recent hole","Frozen pond with recent hole","Area Berserker","Area Berserker","Area Berserker",
                     "Ogre","Ogre","Griffon","Griffon","Druid","Druid","Druid","Frozen Bodies","Frozen Bodies","Frozen Bodies","Frozen Bodies",
                     "Frozen Bodies","Area Veterans","Orogs","2 Brown Bears","Orcs and an Eye of Gruumsh", "Winter wolves","Yetis","Yetis",
                     "Half Ogre","Manticores","Orcs and an Orc Warboss","Revenant","Troll","Troll","Werebear","Werebear","Young Remorhaz",
                     "Young Remorhaz","Mammoth","Cyromiir","Frost Giant"]
    foe = encounterList[x-1]
    ranges = [
        (1, 6, lambda: light_table.d(6)+3),
        (6, 9, lambda: light_table.d(4)+3),
        (11, 13, lambda: light_table.d(4) + light_table.d(4)),
        (13, 18, lambda: light_table.d(6) + light_table.d(6)),
        (18, 21, lambda: light_table.d(6)),
        (26, 30, lambda: light_table.d(8) + light_table.d(8)),
        (41, 46, lambda: light_table.d(3)),
        (51, 54, lambda: light_table.d(6)+1),
        (56, 58, lambda: light_table.d(6)),
        (81, 82, lambda: light_table.d(3)),
        (82, 83, lambda: light_table.d(4)),
        (84, 85, lambda: light_table.d(8) + light_table.d(8)),
        (85, 86, lambda: light_table.d(3)),
        (86, 88, lambda: light_table.d(4)),
        (89, 90, lambda: light_table.d(3)),
        (90, 91, lambda: light_table.d(6) + light_table.d(6)),
    ]
    for lower, upper, dice_roll in ranges:
        if lower <= x < upper:
            amt = dice_roll()
            return f"{amt} {foe}"
    return foe

def daleTableMid(x):
    encounterList = ["2 saber-toothed tigers","2 saber-toothed tigers","2 saber-toothed tigers","2 saber-toothed tigers",
                     "2 saber-toothed tigers","Half Ogre(s)","Half Ogre(s)","brown bears","brown bears","brown bears",
                     "polar bear(s)","polar bear(s)","polar bear(s)","polar bear(s)","polar bear(s)","orc berserkers",
                     "orc berserkers","draconian berserkers","draconian berserkers","draconian berserkers","strange ice growth",
                     "strange ice growth","strange ice growth","strange ice growth","strange ice growth","orc scouts",
                     "orc scouts","draconian scouts","draconian scouts","draconian scouts","ice mephits","ice mephits",
                     "ice mephits","ice mephits","ice mephits","zombies in a house buried in the snow","zombies in a house buried in the snow",
                     "zombies in a house buried in the snow","zombies in a house buried in the snow","zombies in a house buried in the snow",
                     "1 manticore","1 manticore","1 manticore","1 manticore","1 manticore","orcs","orcs","orcs","orcs","orcs",
                     "ogres","ogres","ogres","griffons","griffons","orc veteran(s)","draconian veteran(s)","orc kill team",
                     "draconian kill team","brongalv kill team","hour(s) of surprise blizzard weather","hour(s) of surprise blizzard weather",
                     "hour(s) of surprise blizzard weather","hour(s) of surprise blizzard weather","hour(s) of surprise blizzard weather",
                     "1 young remorhaz","1 young remorhaz","1 young remorhaz","warg riders","warg riders","warg riders","warg riders",
                     "1 revenant","1 revenant","1 revenant","minutes of a howl","minutes of a howl","minutes of a howl","minutes of a howl",
                     "minutes of a howl","mammoth(s)","mammoth(s)","Cryomiir","Cryomiir","winter wolves","winter wolves",
                     "yetis","yetis","frost giant(s)","frost giant(s)","werebear(s)","werebear(s)","trolls","trolls",
                     "1 abominable yeti","1 abominable yeti","1 remorhaz","1 remorhaz","1 roc","young remorhazes"]
    foe = encounterList[x-1]
    ranges = [
        (5, 8, lambda: light_table.d(4)),
        (8, 11, lambda: light_table.d(3) + 1),
        (11, 16, lambda: light_table.d(3)),
        (16, 21, lambda: light_table.d(4) + light_table.d(4)),
        (26, 31, lambda: light_table.d(8) + light_table.d(8)),
        (31, 36, lambda: light_table.d(4) + light_table.d(4)),
        (36, 41, lambda: light_table.d(6) + light_table.d(6) + 1),
        (46, 51, lambda: light_table.d(6) + 3 + light_table.d(6)),
        (51, 54, lambda: light_table.d(6) + 2),
        (54, 56, lambda: light_table.d(4) + light_table.d(4)),
        (56, 58, lambda: light_table.d(4)),
        (61, 66, lambda: light_table.d(4)),
        (69, 73, lambda: light_table.d(8) + light_table.d(8)),
        (76, 81, lambda: light_table.d(3)),
        (81, 83, lambda: light_table.d(3)),
        (85, 87, lambda: light_table.d(4) + light_table.d(4)),
        (87, 89, lambda: light_table.d(6) + 2),
        (89, 91, lambda: light_table.d(2)),
        (91, 93, lambda: light_table.d(3)),
        (93, 95, lambda: light_table.d(4)),
    ]
    for lower, upper, dice_roll in ranges:
        if lower <= x < upper:
            amt = dice_roll()
            return f"{amt} {foe}"
    return foe


def behaviorTable(x):
    behaviorList = ["Digging a Hole","Apathetic","Carrying Food",
                "Hungry","On Patrol","Resting"]
    behavior = behaviorList[x-1]
    return behavior

def compilcationTable(x):
    compList = ["Sick","Starving","Frostbitten","Using Broken Gear",
                "Injured","Understaffed"]
    complication = compList[x-1]
    return complication

def beastTable(x):
    beastList = ["Dire Wolves","Bear","Owlbear","Yeti","a Frost Troll",
                 "Prey Wildlife"]
    beast = beastList[x-1]
    return beast

def enviromentTable(x): #x is a d10
    enviroList = ["Heavy Snowfall (diff terrain)","Heavy Snowfall (diff terrain)","Strong Winds(dis on projectile attack)",
                  "Strong Winds(dis on projectile attack)","Heavy Snow Falling (-15ft vision)","Cliff Face","Crevice",
                  "Slippery Ice (half movement or DC 15 dex save to avoid falling prone)","Heavy Snow Falling (-15ft vision)",
                  "Thin Ice (DC 15 dex to avoid falling through Ice)"]
    enviro = enviroList[x-1]
    return enviro
    
def orkTable(x):
    orkList = [1,2,3,"Orcs","Davrak",6]
    if x == 1:
        y = light_table.d(6)
        ork = beastTable(y)
    elif x == 2:
        y = light_table.d(4)
        if y == 1:
            ork = "Brongalv Hunting Constructs"
            ork = str(light_table.d(6))+" "+ork
        if y == 2:
            ork = "Draconian Headhunters"
            ork = str(light_table.d(6))+" "+ork
        else:
            ork = "Orc Hunters, otherwise 10 New Shandr Hunters"
            ork = str(light_table.d(6)+light_table.d(4))+" "+ork
    elif x == 3:
        #enviroment hazard, at night sudden heavy snowfall or strong wind
        y = light_table.d(10)
        ork = enviromentTable(y)
        z = light_table.d(3)
        if z > 1 and z < 3:
            y = light_table.d(6)
            orkbeast = beastTable(y)
            ork = orkbeast + " near " + ork
        if z == 3:
            y = light_table.d(6)
            if y == 3:
                y == 1
            orkencounter = orkTable(y)
            ork = orkencounter + " near " + ork
    elif x > 3 and x < 6:
        ork = orkList[x-1]
        if ork == "Orcs":
            ork = str(light_table.d(6)+light_table.d(6))+" "+ork
    else:
        y = light_table.d(5)
        z = light_table.d(5)
        ork1 = orkTable(y)
        ork2 = orkTable(z)
        ork = ork1 + ", and " + ork2
    return ork

def brongalvTable(x):
    bronList = [1,2,3,"Constructs","Brongalv Home Defense Unit",6]
    if x == 1:
        y = light_table.d(6)
        bron = beastTable(y)
    elif x == 2:
        y = light_table.d(3)
        if y == 1:
            bron = "Ork Infiltrators"
            bron = str(light_table.d(6))+" "+bron
        else:
            bron = "Brongalv Hunting Constructs"
            bron = str(light_table.d(6))+" "+bron
    elif x == 3:
        #enviroment hazard, at night sudden heavy snowfall or strong wind
        y = light_table.d(10)
        bron = enviromentTable(y)
        z = light_table.d(3)
        if z > 1 and z < 3:
            y = light_table.d(6)
            bronbeast = beastTable(y)
            bron = bronbeast + " near " + bron
        if z == 3:
            y = light_table.d(6)
            if y == 3:
                y == 1
            bronencounter = brongalvTable(y)
            bron = bronencounter + " near " + bron
    elif x > 3 and x < 6:
        bron = bronList[x-1]
        if bron == "Constructs":
            bron = str(light_table.d(6)+light_table.d(6))+" "+bron
    else:
        y = light_table.d(5)
        z = light_table.d(5)
        bron1 = brongalvTable(y)
        bron2 = brongalvTable(z)
        bron = bron1 + ", and " + bron2
    return bron

def cryomiirTable(x):
    cryoList = [1,2,3,"Draconians","Cryomiir",6]
    if x == 1:
        y = light_table.d(6)
        cryo = beastTable(y)
    elif x == 2:
        y = light_table.d(3)
        if y == 1:
            cryo = "Orc Infiltrators"
            cryo = str(light_table.d(6))+" "+cryo
        else:
            cryo = "Draconian Hunters"
            cryo = str(light_table.d(6))+" "+cryo
    elif x == 3:
        #enviroment hazard, at night sudden heavy snowfall or strong wind
        y = light_table.d(10)
        cryo = enviromentTable(y)
        z = light_table.d(3)
        if z > 1 and z < 3:
            y = light_table.d(6)
            cryobeast = beastTable(y)
            cryo = cryobeast + " near " + cryo
        if z == 3:
            y = light_table.d(6)
            if y == 3:
                y == 1
            cryoencounter = cryomiirTable(y)
            cryo = cryoencounter + " near " + cryo
    elif x > 3 and x < 6:
        cryo = cryoList[x-1]
        if cryo == "Draconians":
            cryo = str(light_table.d(6)+light_table.d(6))+" "+cryo
    else:
        y = light_table.d(5)
        z = light_table.d(5)
        cryo1 = cryomiirTable(y)
        cryo2 = cryomiirTable(z)
        cryo = cryo1 + ", and " + cryo2
    return cryo