import random

def generate_loot(loot_table):
    \"\"\"Generates a random loot item from the provided loot table.\"\"\"
    return random.choice(loot_table)

# Example loot table (will be expanded later)
common_loot = [
    "gold coin",
    "healing potion",
    "short sword",
    "wooden shield",
    "iron dagger",
    "leather armor",
    "map",
    "rope"
]

rare_loot = [
    "magic ring",
    "phoenix feather",
    "amulet of power"
]

def generate_loot(loot_table):
    \"\"\"Generates a random loot item from the provided loot table.\"\"\"
    return random.choice(loot_table)

def generate_specific_loot(loot_table, specific_loot_type):
    \"\"\"Generates a specific type of loot from the provided loot table.\"\"\"
    if specific_loot_type == "weapon":
        return random.choice(loot_table)
    elif specific_loot_type == "armor":
        return random.choice(loot_loot_table)
    else:
        return random.choice(loot_table)

# Example loot table (will be expanded later)
# Example loot table (will be expanded later)
common_loot = [
    "gold coin",
    "healing potion",
    "short sword",
    "wooden shield",
    "iron dagger",
    "leather armor",
    "map",
    "rope"
]
