import random
import random_table
import lootTable
#class for weather forecast
class DailyWeather:
    def __init__(day, temp, perc, wind):
        day.temp = temp
        day.perc = perc
        day.wind = wind
    def __str__(day):
        if day.perc == "Heavy" and day.wind == "Heavy":
            return f"Temperature: {day.temp} Degrees Celsius. Snowfall: {day.perc}. Wind: {day.wind}. Blizzard Warning is in effect for this day."
        else:
            return f"Temperature: {day.temp} Degrees Celsius. Snowfall: {day.perc}. Wind: {day.wind}"

#function that determines dice to roll, x should be replaced by a number and rarely a variable
def d(x):
    num = random.randint(1,x)
    return num

#function for rolling character dice
def roll_stats():
    return [roll_stat() for _ in range(6)]
    
def roll_stat():
    rolls = sorted([d(6) for _ in range(4)], reverse=True)
    return sum(rolls[:3])

#sets the temp, percipitation, and wind for a given day. requires the average temp to use
def weatherSet(avgtemp):
    percset = d(20)
    windset = d(20)
    tempset = d(20)
    #set var wind to the wind condition and perc
    wind = random_table.windandpercip(windset)
    perc = random_table.windandpercip(percset)
    temp = random_table.temperature(tempset,avgtemp,wind,perc)
    weather = DailyWeather(temp, perc, wind)
    return weather
#take parameter flist so the list stays across multiple days
def forecast(flist, needDays, avgtemp):
    #if a week is needed, flist needs to be an empty list, otherwise pop the amount of days from the front
    if needDays == 7:
        flist = []
    elif needDays > 7:
        return 1
    else:
        for x in range(0, needDays):
            flist.pop(x)
    for x in range(0, needDays):
        newday = weatherSet(avgtemp)
        flist.append(newday)
    return flist

#Beast Table Roll

def encounterTime(num):
    timeList = ["Morning","Noon","Evening","Early Night","Midnight","Predawn"]
    schedule = ""
    for x in range(0, num):
        dice = d(6)
        add = timeList[dice-1]
        while add in schedule:
            dice = d(6)
            add = timeList[dice-1]
        if x == num-1:
            schedule = schedule+add
        else:
            schedule = schedule + add+", "
    return schedule

#Takes in num amount of encounters, using the place tables
def encounterGenerator(place, num):
    encountersend = "" 
    for x in range(0,num):
        #At {TIME}, The party encounters {ENCOUNTER} that appear to be {Complication}, and seem to be {Behavior}\n
        encounter = "Near "+encounterTime(1)
        while encounter in encountersend:
            encounter = "Near "+encounterTime(1)
        encountersend = encountersend+encounter+", the party encounters "
        dice = d(6)
        if place == 'brongalv':
            encounter = random_table.brongalvTable(dice)
        elif place == 'orc':
            encounter = random_table.orkTable(dice)
        elif place == 'cryomiir':
            encounter = random_table.cryomiirTable(dice)
        elif place == 'dalelow':
            dice = d(100)
            encounter = random_table.daleTableLow(dice)
            encountersend = encountersend+encounter+"\n"
            continue
        elif place == 'dalemid':
            dice = d(100)
            encounter = random_table.daleTableMid(dice)
            encountersend = encountersend+encounter+"\n"
            continue
        encountersend = encountersend+encounter
        if dice == 3:
            if "Orc" not in encounter or "Draconian" not in encounter or "Constructs" not in encounter or "Goblins" not in encounter:
                encountersend = encountersend+"\n"
                continue
        if "Cryomiir" in encounter or "Davrak" in encounter or "Brongalv Home Defense Unit" in encounter:
            encountersend = encountersend+"\n"
            continue
        if "Partially eaten corpse" in encounter or "Tracks in the snow" in encounter or "Frozen pond with recent hole" in encounter or "Frozen Bodies" in encounter:
            encountersend = encountersend+"\n"
            continue
        dice = d(6)
        encounter = random_table.compilcationTable(dice)
        encountersend = encountersend+" that appear to be "+encounter
        dice = d(6)
        encounter = random_table.behaviorTable(dice)
        if x == num-1:
            encountersend = encountersend+", and seem to be "+encounter
        else:
            encountersend = encountersend+", and seem to be "+encounter+"\n"
    return encountersend

def hoard(level):
    if level<5:
        amt = d(6)+d(6)+d(6)+d(6)+d(6)+d(6)
        amt = amt*100
        amt = str(amt)
        hoard = amt + " Copper pieces, "
        amt = d(6)+d(6)+d(6)
        amt = amt*100
        amt = str(amt)
        hoard = hoard +amt+" Silver pieces, "
        amt = d(6)+d(6)
        amt = amt*10
        amt = str(amt)
        hoard = hoard +amt+" Gold pieces, "
        dice = d(100)
        #2d6 for if
        if (dice>6 and dice<17) or (dice>26 and dice<45) or (dice>52 and dice<66) or (dice>70 and dice<79) or (dice>80 and dice<86) or (dice>92 or dice<98) or (dice>99):
            amtdie = d(6)+d(6)
        else:
            amtdie = d(4)+d(4)

        #ranges = [
        #    (8,17, lambda: lootTable.gemstones_10(d(12)))
        #    (17,26, lambda: lootTable.art_25(d(10)))
        #    (26,37, lambda: lootTable.gemstones_50(d(12)))
        #    (37,45, lambda: lootTable.gemstones_10(d(12)))
        #    (45,53, lambda: lootTable.art_25(d(10)))
        #    (53,61, lambda: lootTable.gemstones_50(d(12)))
        #    (61,66, lambda: lootTable.gemstones_10(d(12)))
        #    (66,71, lambda: lootTable.art_25(d(10)))
        #    (71,76, lambda: lootTable.gemstones_50(d(12)))
        #    (76,79, lambda: lootTable.gemstones_10(d(12)))
        #    (79,81, lambda: lootTable.art_25(d(10)))
        #    (81,86, lambda: lootTable.gemstones_50(d(12)))
        #    (86,93, lambda: lootTable.art_25(d(10)))
        #    (93,98, lambda: lootTable.gemstones_50(d(12)))
        #    (98,100, lambda: lootTable.art_25(d(10)))
        #    (100,101, lambda: lootTable.gemstone_50(d(12)))
        #]
        #for lower, upper, roll in ranges:
        #if lower <= x < upper:
        #    item = roll()
        #    hoard = hoard+item+", "
        #return hoard
        
        #for loop to seed gems or art objects
        for x in range(0,amtdie):
            if dice<7:
                return hoard
            elif dice<17:
                num = d(12)
                gem = lootTable.gemstones_10(num)
                hoard = hoard+gem+", "
            elif dice<26:
                num = d(10)
                art = lootTable.art_25(num)
                hoard = hoard+art+", "
            elif dice<37:
                num = d(12)
                gem = lootTable.gemstones_50(num)
                hoard = hoard+gem+", "
            elif dice<45:
                num = d(12)
                gem = lootTable.gemstones_10(num)
                hoard = hoard+gem+", "
            elif dice<53:
                num = d(10)
                art = lootTable.art_25(num)
                hoard = hoard+art+", "
            elif dice<61:
                num = d(12)
                gem = lootTable.gemstones_50(num)
                hoard = hoard+gem+", "
            elif dice<66:
                num = d(12)
                gem = lootTable.gemstones_10(num)
                hoard = hoard+gem+", "
            elif dice<71:
                num = d(10)
                art = lootTable.art_25(num)
                hoard = hoard+art+", "
            elif dice<76:
                num = d(12)
                gem = lootTable.gemstones_50(num)
                hoard = hoard+gem+", "
            elif dice<79:
                num = d(12)
                gem = lootTable.gemstones_10(num)
                hoard = hoard+gem+", "
            elif dice<81:
                num = d(10)
                art = lootTable.art_25(num)
                hoard = hoard+art+", "
            elif dice<86:
                num = d(12)
                gem = lootTable.gemstones_50(num)
                hoard = hoard+gem+", "
            elif dice<93:
                num = d(10)
                art = lootTable.art_25(num)
                hoard = hoard+art+", "
            elif dice<98:
                num = d(12)
                gem = lootTable.gemstones_50(num)
                hoard = hoard+gem+", "
            elif dice<100:
                num = d(10)
                art = lootTable.art_25(num)
                hoard = hoard+art+", "
            else:
                num = d(12)
                gem = lootTable.gemstones_50(num)
                hoard = hoard+gem+", "
        if dice<37:
            hoard = hoard+"have been found in the hoard"
            return hoard
        elif dice<61:
            amtdie = d(6)
        elif dice<98:
            amtdie = d(4)
        else:
            amtdie = 1
        for x in range(0, amtdie):
            if dice<60:
                num = d(100)
                item = lootTable.magic_item_A(num)
                hoard = hoard+item+", "
            elif dice<76:
                num = d(100)
                item = lootTable.magic_item_B(num)
                hoard = hoard+item+", "
            elif dice<86:
                num = d(100)
                item = lootTable.magic_item_C(num)
                hoard = hoard+item+", "
            elif dice<98:
                num = d(100)
                item = lootTable.magic_item_F(num)
                hoard = hoard+item+", "
            elif dice<=100:
                num = d(100)
                item = lootTable.magic_item_A(num)
                hoard = hoard+item+", "
        hoard = hoard+"have been found in the hoard"
        return hoard
            
