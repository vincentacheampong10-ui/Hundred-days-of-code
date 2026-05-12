enemies = 1



def increase_enemies():
    # Local Scope
    enemies = 2
    print(f"enimes inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
player_health


# Modifying Global Scope

enemie = 1

def increase_enemie():
    global enemie
    enemie += 2
    print(f"enime inside function: {enemie}")

increase_enemies()
print(f"enemies outside function: {enemie}")