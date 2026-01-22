import light_table
def magic_item_A(x):
    if x <51:
        item = "potion of healing"
    elif x <61:
        item = "spell scroll (cantrip)"
    elif x <71:
        item = "potion of climbing"
    elif x <91: 
        item = "1st level spell scroll"
    elif x <95:
        item = "2nd level spell scroll"
    elif x <99:
        item = "bag of holding"
    else:
        item = "driftglobe"
    return item

def magic_item_B(x):
    magicList = ["Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of greater healing",
                 "Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of greater healing",
                 "Potion of greater healing","Potion of greater healing","Potion of greater healing","Potion of fire breath","Potion of fire breath","Potion of fire breath","Potion of fire breath",
                 "Potion of fire breath","Potion of fire breath","Potion of fire breath","Potion of fire breath","Potion of reistance","Potion of reistance","Potion of reistance","Potion of reistance",
                 "Potion of reistance","Potion of reistance","Potion of reistance","Ammunition, +1","Ammunition, +1","Ammunition, +1","Ammunition, +1","Potion of animal friendship","Potion of animal friendship",
                 "Potion of animal friendship","Potion of animal friendship","Potion of animal friendship","Potion of hill giant strength","Potion of hill giant strength","Potion of hill giant strength",
                 "Potion of hill giant strength","Potion of hill giant strength","Potion of growth","Potion of growth","Potion of growth","Potion of growth","Potion of growth","potion of water breathing",
                 "potion of water breathing","potion of water breathing","potion of water breathing","potion of water breathing","2nd level spell scroll","2nd level spell scroll","2nd level spell scroll",
                 "2nd level spell scroll","2nd level spell scroll","3rd level spell scroll","3rd level spell scroll","3rd level spell scroll","3rd level spell scroll","3rd level spell scroll",
                 "Bag of holding","Bag of holding","Bag of holding","Keoghtom's ointment","Keoghtom's ointment","Keoghtom's ointment","Oil of slipperiness","Oil of slipperiness","Oil of slipperiness",
                 "Dust of disapperance","Dust of disapperance","Dust of dryness","Dust of dryness","Dust of sneezing and choking","Dust of sneezing and choking","Elemental gem","Elemental gem",
                 "Philter of love","Philter of love","Alchemy Jug","Cap of water breathing","Cloak of the manta ray","Driftglobe","Goggles of might","Helm of comprehending langauges","Immovable rod",
                 "Lantern of revealing","Mariner's armor","Mithral armor","Potion of poison","Ring of swimming","Robe of useful items","Rope of climbing","Saddle of the cavalier","Wand of magic detection","Wand of secrets"]
    item = magicList[x-1]
    return item

def magic_item_C(x):
    magicList = ["Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing",
                 "Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing","Potion of superior healing",
                 "Potion of superior healing","4th level spell scroll","4th level spell scroll","4th level spell scroll","4th level spell scroll","4th level spell scroll","4th level spell scroll","4th level spell scroll",
                 "Ammunition, +2","Ammunition, +2","Ammunition, +2","Ammunition, +2","Ammunition, +2","Potion of clairvoyance","Potion of clairvoyance","Potion of clairvoyance","Potion of clairvoyance","Potion of clairvoyance",
                 "Potion of diminution","Potion of diminution","Potion of diminution","Potion of diminution","Potion of diminution","Potion of gaseous form","Potion of gaseous form","Potion of gaseous form","Potion of gaseous form",
                 "Potion of gaseous form","Potion of frost giant strength","Potion of frost giant strength","Potion of frost giant strength","Potion of frost giant strength","Potion of frost giant strength",
                 "Potion of stone giant strength","Potion of stone giant strength","Potion of stone giant strength","Potion of stone giant strength","Potion of stone giant strength","Potion of heroism","Potion of heroism",
                 "Potion of heroism","Potion of heroism","Potion of heroism","Potion of Invulnerabililty","Potion of Invulnerabililty","Potion of Invulnerabililty","Potion of Invulnerabililty","Potion of Invulnerabililty",
                 "Potion of mind reading","Potion of mind reading","Potion of mind reading","Potion of mind reading","Potion of mind reading","5th level spell scroll","5th level spell scroll","5th level spell scroll","5th level spell scroll",
                 "5th level spell scroll","Exilir of health","Exilir of health","Exilir of health","Oil ofetherealness","Oil ofetherealness","Oil ofetherealness","Potion of fire giant strength","Potion of fire giant strength","Potion of fire giant strength",
                 "Quaal's feather token","Quaal's feather token","Quaal's feather token","Scroll of protection","Scroll of protection","Scroll of protection","Bag of beans","Bag of beans","Bead of force","Bead of force","Chime of opening",
                 "Decanter of endless water","Eyes of minute seeing","Folding boat","Heward's handy haversack","Horseshoes of speed","Necklace of fireballs","Periapt of health","Sending stones"]
    item = magicList[x-1]
    return item

def magic_item_D(x):
    magicList = ["Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing",
                 "Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing",
                 "Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of supreme healing","Potion of Invisibility","Potion of Invisibility","Potion of Invisibility","Potion of Invisibility","Potion of Invisibility",
                 "Potion of Invisibility","Potion of Invisibility","Potion of Invisibility","Potion of Invisibility","Potion of Invisibility","Potion of speed","Potion of speed","Potion of speed","Potion of speed","Potion of speed","Potion of speed","Potion of speed",
                 "Potion of speed","Potion of speed","Potion of speed","6th level spell scroll","6th level spell scroll","6th level spell scroll","6th level spell scroll","6th level spell scroll","6th level spell scroll","6th level spell scroll","6th level spell scroll",
                 "6th level spell scroll","6th level spell scroll","7th level spell scroll","7th level spell scroll","7th level spell scroll","7th level spell scroll","7th level spell scroll","7th level spell scroll","7th level spell scroll",
                 "Ammunition, +3","Ammunition, +3","Ammunition, +3","Ammunition, +3","Ammunition, +3","Oil of sharpness","Oil of sharpness","Oil of sharpness","Oil of sharpness","Oil of sharpness","Potion of flying","Potion of flying","Potion of flying",
                 "Potion of flying","Potion of flying","Potion of cloud giant strength","Potion of cloud giant strength","Potion of cloud giant strength","Potion of cloud giant strength","Potion of cloud giant strength","Potion of longevity",
                 "Potion of longevity","Potion of longevity","Potion of longevity","Potion of longevity","Potion of vitality","Potion of vitality","Potion of vitality","Potion of vitality","Potion of vitality","8th level spell scroll","8th level spell scroll",
                 "8th level spell scroll","8th level spell scroll","8th level spell scroll","Horseshoes of a zephyr","Horseshoes of a zephyr","Horseshoes of a zephyr","Nolzur's marvelous pigments","Horseshoes of a zephyr","Nolzur's marvelous pigments",
                 "Horseshoes of a zephyr","Nolzur's marvelous pigments","Bag of devouring","Portable hole"]
    item = magicList[x-1]
    return item

def magic_item_E(x):
    if x<31:
        item = "8th level spell scroll"
    elif x<56:
        item = "Potion of storm giant strength"
    elif x<71:
        item = "Potion of supreme healing"
    elif x<86:
        item = "9th level spell scroll"
    elif x<94:
        item = "Universal solvent"
    elif x<99:
        item = "Arrow of slaying"
    else:
        item = "Soverign glue"
    return item

def magic_item_F(x):
    magicList = ["+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 weapon","+1 shield","+1 shield","+1 shield","Sentinel shield",
                 "Sentinel shield","Sentinel shield","Amulet of proof against detection and location","Amulet of proof against detection and location","Boots of elvenkind","Boots of elvenkind","Boots of striding and springing","Boots of striding and springing",
                 "Bracers of archery","Bracers of archery","Brooch of shielidng","Brooch of shielidng","Broom of flying","Broom of flying","Cloak of elvenkind","Cloak of elvenkind","Cloak of protection","Cloak of protection","Gauntlets of ogre power",
                 "Gauntlets of ogre power","Hat of disguise","Hat of disguise","Javelin of lightning","Javelin of lightning","Pearl of power","Pearl of power","+1 Rod of the pact keeper","+1 Rod of the pact keeper","Slippers of spider climbing",
                 "Slippers of spider climbing","Staff of the adder","Staff of the adder","Staff of the python","Staff of the python","Sword of vengance","Sword of vengance","Trident of fish command","Trident of fish command","Wand of magic missiles",
                 "Wand of magic missiles","+1 Wand of the war mage","+1 Wand of the war mage","Wand of web","Wand of web","Weapon of warning","Weapon of warning","Adamantine armor (chain mail)","Adamantine armor (chain shirt)","Adamantine armor (scale mail)",
                 "Bag of tricks (gray)","Bag of tricks (rust)","Bag of tricks (tan)","Boots of the winterlands","Circlet of blasting","Deck of illusions","Eversmoking bottle","Eyes of charming","Eyes of the eagle","Figurine of wondrous power (silver raven)",
                 "Gem of brightness","Gloves of missile snaring","Gloves of swimming and climbing","Gloves of theivery","Headband of intellect","Helm of telepathy","Instrument of the bards (Doss lute)","Instrument of the bards (Fochlucan bandore)",
                 "Instrument of the bards (Mac-Fui idh cittern)","Medallion of thoughts","Necklace of adaptation","Periapt of wound closure","Pipes of haunting","Pipes of the sewers","Ring of jumping","Ring of mind shielding","Ring of warmth","Ring of water walking",
                 "Quiver of Quelenna (Ehlonna rules)","Stone of good luck","Wind fan","Winged boots"]
    item = magicList[x-1]
    return item

def magic_item_G(x):
    magicList = ["+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","+2 weapon","Figurine of wondrous power(roll d8)","Figurine of wondrous power(roll d8)","Figurine of wondrous power(roll d8)",
                 "Adamantine armor (breastplate)","Adamantine armor (splint)","Amulet of health","Armor of vulnerabitlity","Arrow-catching shield","Belt of dwarvenkind","Belt of hill giant strength","Berserker axe","Boots of levitation","Boots of speed",
                 "Bowl of commanding water elementals","Bracers of defense","Braizer of commanding fire elementals","+1 Chainmail","Chainmail armor of resistance","+1 Chain shirt","Chain shirt armor of resistance","Cloak of displacement","Cloak of the bat",
                 "Cube of force","Daern's instant fortress","Dagger of venom","Dimensional shackles","Dragon slayer","Eleven chain","Flame tounge","Gem of seeing","Giant slayer","Glamoured studded leather","Helm of teleportation","Horn of blasting",
                 "Horn of Valhalla (silver or brass)","Instrument of the bards (Canaith mandolin)","Instrument of the bards (Cli lyre)","Ioun stone (awareness)","Ioun stone (protection)","Ioun stone (reserve)","Ioun stone (sustenance)","Iron bands of Bilarro",
                 "+1 leather armor","Leather armor of resistance","Mace of disruption","Mace of smiting","Mace of terror","Mantle of spell resistance","Necklace of prayer beads","Periapt of proof against poison","Ring of animal influence","Ring of evasion",
                 "Ring of feather falling","Ring of free action","Ring of protection","Ring of resistance","Ring of spell storing","Ring of the ram","Ring of X-ray vision","Robe of eyes","Rod of rulership","+2 Rod of the pact keeper","Rope of entaglement",
                 "+1 scale mail","Scale mail armor of resistance","+2 shield","Shield of missile attraction","Staff of charming","Staff of healing","Staff of swarming insects","Staff of the woodlands","Staff of withering","Stone of controlling earth elementals",
                 "Sun blade","Sword of life stealing","Sword of wounding","Tentacle rod","Vicious weapon","Wand of binding","Wand of enemy detection","Wand of fear","Wand of fireballs","Wand of lightning bolts","Wand of paralysis","+2 Wand of the war mage",
                 "Wand of wonder","Wings of flying"]
    item = magicList[x-1]
    return item

def magic_item_H(x):
    magicList = ["+3 weapon","+3 weapon","+3 weapon","+3 weapon","+3 weapon","+3 weapon","+3 weapon","+3 weapon","+3 weapon","+3 weapon","Amulet of the planes","Amulet of the planes","Carpet of flying","Carpet of flying","Crystal ball (very rare)","Crystal ball (very rare)",
                 "Ring of regeneration","Ring of regeneration","Ring of shooting stars","Ring of shooting stars","Ring of telekinesis","Ring of telekinesis","Robe of scintillating colors","Robe of scintillating colors","Robe of stars","Robe of stars","Rod of absorption",
                 "Rod of absorption","Rod of alertness","Rod of alertness","Rod of security","Rod of security","+3 Rod of the pact keeper","+3 Rod of the pact keeper","Scimitar of speed","Scimitar of speed","+3 shield","+3 shield","Staff of fire","Staff of fire",
                 "Staff of frost","Staff of frost","Staff of power","Staff of power","Staff of striking","Staff of striking","Staff of thunder and lightning","Staff of thunder and lightning","Sword of sharpness","Sword of sharpness","Wand of polymorph","Wand of polymorph",
                 "+3 Wand of the war mage","+3 Wand of the war mage","Adamatine armor (half plate)","Adamantine armor (plate)","Animated shield","Belt of fire giant strength","Belt of frost or stone giant strength","+1 breastplate","Breastplate of resistance","Candle of invocation",
                 "+2 Chain mail","+2 Chain shirt","Cloak of arachnida","Dancing sword","Demon armor","Dragon scale mail","Dwarven plate","Dwarven thrower","Efreeti bottle","Figurine of wondrous power (obsidian steed)","Frost brand","Helm of brilliance","Horn of Valhalla (bronze)",
                 "Instrument of the bards (Francis Bagpipes(use Anstruth harp))","Ioun stone (absorption)","Ioun stone (agility)","Ioun stone (fortitude)","Ioun stone (insight)","Ioun stone (intellect)","Ioun stone (leadership)","Ioun stone (strenght)","+2 Leather armor",
                 "Manual of bodily health","Manual of gainful excercise","Manual of golems","Manual of quickness of action","Mirror of life trapping","Nine lives stealer","Oathbow","+2 scale mail","Spellguard shield","+1 Splint","Splint armor of resistance","+1 Studded leather",
                 "Studded leather of resistance","Tome of clear thought","Tome of leadership and influence","Tome of understanding"]
    item = magicList[x-1]
    return item

def magic_item_I(x):
    magicList = ["Defender","Defender","Defender","Defender","Defender","Hammer of thunderbolts","Hammer of thunderbolts","Hammer of thunderbolts","Hammer of thunderbolts","Hammer of thunderbolts","Luck blade","Luck blade","Luck blade","Luck blade","Luck blade",
                 "Sword of answering","Sword of answering","Sword of answering","Sword of answering","Sword of answering","Holy avenger","Holy avenger","Holy avenger","Ring of djinni summoning","Ring of djinni summoning","Ring of djinni summoning",
                 "Ring of invisibility","Ring of invisibility","Ring of invisibility","Ring of spell turning","Ring of spell turning","Ring of spell turning","Rod of lordly might","Rod of lordly might","Rod of lordly might","Staff of the magi","Staff of the magi",
                 "Staff of the magi","Vorpal sword","Vorpal sword","Vorpal sword","Belt of cloud giant strength","Belt of cloud giant strength","+2 breastplate","+2 breastplate","+3 chainmail","+3 chainmail","+3 chain shirt","+3 chain shirt","Cloak of invisibility",
                 "Cloak of invisibility","Crystal ball (legendary)","Crystal ball (legendary)","+1 half plate","+1 half plate","Iron flask","Iron flask","+3 leather armor","+3 leather armor","+1 plate armor","+1 plate armor","Robe of the archmagi","Robe of the archmagi",
                 "Rod of ressurection","Rod of ressurection","+1 scale mail","+1 scale mail","Scarab of protection","scarab of protection","+2 splint","+2 splint","+2 studded leather","+2 studded leather","Well of many worlds","Well of many worlds","See list","Apparatus of Kwalish",
                 "Armor of invulnerability","Belt of storm giant strength","Cubic gate","Deck of many things","Efreeti chain","Half plate of resistance","Horn of Valhalla (iron)","Instrument of the bards (Ollamh harp)","Ioun stone (greater absorption)",
                 "Ioun stone (mastery)","Ioun stone (regeneration)","Plate armor of etherealness","Plate armor of resistance","Ring of air elemental command","Ring of fire elemental command","Ring of earth elemental command","Ring of 3 wishes","Ring of water elemental command",
                 "Sphere of annihilation","Talisman of pure good","Talisman of the sphere","Talisman of ultimate evil","Tome of the stilled tounge"]
    item = magicList[x-1]
    if item == "See list":
        dice = light_table.d(12)
        armorList = ["+2 half plate","+2 half plate","+2 plate armor","+2 plate armor","+3 studded leather","+3 studded leather","+3 breastplate","+3 breastplate","+3 splint","+3 splint","+3 half plate","+3 plate armor"]
        item = armorList[dice-1]
    return item

def gemstones_10(x):
    gemList = ["Azurite (opaque mottled deep blue)","Band agate (translucent striped brown, blue, white, or red)","Blue quartz (transparent pale blue)","Eye agate (translucent circles of gray, white, brown, blue, or green)","Hermatite (opaque gray black)",
               "Lapis Lazuli (opaque light and dark blue with yellow flecks)","Malachite (opaque striated light and dark green)","Moss agate (translucent pink or yellow-white with mossy gray or green markings)","Obsidian (opaque black)","Rhodochrosite (opaque light pink)",
               "Tiger eye (translucent brown with golden center)","Turquoise (light blie-green)"]
    item = gemList[x-1]
    return item

def gemstones_50(x):
    gemList = ["Bloodstone (opaque dark gray with red flecks)","Carnelian (opaque orange to red brown)","Chalcedony (opaque white)","Chrysoprase (translucent green)","Citrine (transparent pale yellow-brown)","Jasper (opaque blue, black, or brown)","Moonstone (translucent white with pale blue glow)",
               "Onyx (opaque bands of black and white, or pure blakc and white)","Quartz (transparent white, smoky gray, or yellow)","Sardonyx (opaque bands of red and white)","Star rose quartz (translucent rosy tone with white star center)","Zircon (transparent pale blue green)"]
    item = gemList[x-1]
    return item

def gemstones_100(x):
    gemList = ["Amber (transparent watery gold to rich gold)","Amethyst (transparent deep purple)","Chrysoberyl (transparent yellow-green to pale green)","Coral (opaque crimson)","Garnet (transparent red, brown-green, or violet)","Jade (translucent light green, deep green, or white)",
               "Jet (opaque deep black)","Pearl (opaque lustrous white, yellow, or pink)","Spinel (transparent red, red-brown, or deep green)","Tourmaline (transparent plae green, blue, brown, or red)"]
    item = gemList[x-1]
    return item

def gemstones_500(x):
    gemList = ["Alexandrite (transparent dark green)","Aquamarine (transparent pale blue green)","Black pearl (opaque pure black)","Blue spinel (transparent deep blue)","Peridot (transparent rich olive green)","Topaz (transparent golden yellow)"]
    item = gemList[x-1]
    return item

def gemstones_1000(x):
    gemList = ["Black opal (translucent dark green with black mottling an golden flecks)","Blue sapphire (transparent blue white to medium blue)","Emerald (transparent deep green)","Fire opal (translucent firey red)","Opal (translucent pale blue with green and golden mottling)",
               "Star ruby (translucent ruby with star shaped center)","Yellow sapphire (transparent firey yellow or yellow-green)"]
    item = gemList[x-1]
    return item

def gemstones_5000(x):
    gemList = ["Black sapphire (translucent lustrous black with glowing highlights)","Diamond (transparent blue white, canary, pink, brown, or blue)","Jacinth (transparent firey orange)","Ruby (transparent clear red to deep crimson)"]
    item = gemList[x-1]
    return item

def art_25(x):
    artList = ["Silver ewer","Carved bone statuette","Small gold bracelet","Clot of gold vestments","Black velvet mask stitched with silver thread","Copper chalice with silver filigree","Pair of engraved bone dice","Small mirror set in a painted wooden frame",
               "Embroidered silk hankerchief","Gold locket with a painted portrait inside"]
    item = artList[x-1]
    return item

def art_250(x):
    artList = ["Gold ring set with bloodstone","Carved ivory statuette","Large gold bracelet","Silver necklace with a gemstone pendant","Bronze crown","Silk robe with gold embroidery","Large wellmade tapestry","Brass mug with jade inlay",
               "Box of turquoise animal figures","Gold bird cage with electrum filigree"]
    item = artList[x-1]
    return item

def art_750(x):
    artList = ["Silver chalice set with moonstones","Silver plated steel longsword with jet set in hilt","Carved harp of exotic wood woth ivory inlay and zircon gems","Small gold idol","Gold dragon comb set with red garnets as eyes",
               "Bottle stopper cork embossed with gold leaf and set with amethysts","Ceremonial electrum dagger with a black pearl in pommel","Silver and gold brooch","Obsidian statuette with gold fittings and inlay","Painted gold war mask"]
    item = artList[x-1]
    return item

def art_2500(x):
    artList = ["Fine gold chain set with a fire opal","Old masterpiece painting","Embroidered silk and velvet mantle set with numerous moonstones","Platinum bracelet set with a sapphire","Embroidered glove set with jewel chips",
               "Jeweled anklet","Gold music box","Gold circlet set with four aquamarines","Eye patch with a mock eye set in blue sapphire and moonstone","A necklace string of small pink pearls"]
    item = artList[x-1]
    return item

def art_7500(x):
    artList = ["Jeweled gold crown","Jeweled platinum ring","Small gold statuette set with rubies","Gold cup set with emeralds","Gold jewelery box with platinum filigree","Painted gold child's sarcophagus","Jade game board with solid gold playing pieces",
               "Bejeweled ivory drinking horn with gold filigree"]
    item = artList[x-1]
    return item