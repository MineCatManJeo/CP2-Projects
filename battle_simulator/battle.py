# Battle simulation
from InquirerPy import inquirer
import random

from read_file import read_file as read

def stats(character,stats,level_stat=0):
    # Assigns values to each of the characters with accurate damage / health ect with your stats
    character.append(100 + 25*stats['hea']*(1+level_stat/7)) # Health
    character.append(20*(1+stats['spe']/(5-random.choice([0,0.5,1]))) + (5+random.choice([0,0.5,1]))*stats['str']*(1+level_stat/7)) # Damage
    character.append((1+0.025*(1+level_stat/40))**(-stats['def'])) # Damage Reduction
    return character

def battle_set_up(rf_enemy,sel_char):
    print('\033c')

    rf_enemy = random.choice([x for x in rf_enemy if x['dif'] <= sel_char['level']/3])

    # Create Player Stats:
    xp_cap = sel_char['level']+1 * 50
    current_xp = sel_char['xp']
    player = []
    enemy = []

    stats(player,sel_char)
    stats(enemy,rf_enemy,sel_char['level'])
    outcome = battle(enemy,player,rf_enemy,sel_char)
    if outcome == "Win":
        xp = ((sel_char['level']+1)/15) * ((rf_enemy['dif']+1)/15) * 1250
        print(f"\033cYou defeated the {rf_enemy["name"]} and gained {xp:.0f} expirience!")
        xp += current_xp
        while xp >= xp_cap:
            xp -= xp_cap
            xp_cap += 50
            sel_char['level'] += 1
            sel_char['points'] += 1
        sel_char['xp'] = round(xp)
        inquirer.text(message="Press [Enter] to Continue").execute()
        return sel_char


    elif outcome == 'Fail':
        print('\033cYou Died\nBetter Luck Next Time!')
        return sel_char

def attack(turn,opponent,pronoun):
    critical = random.choice([1,1.5])
    if critical == 1.5:
        print("Critical hit!")
    opponent[0] -= (turn[1]*critical)*opponent[2]
    if opponent[0] < 1:
        opponent[0] = 0
    print(f'{pronoun} did [{(turn[1]*critical)*opponent[2]:.0f}] damage!')


def battle(enemy,player,rf_enemy,sel_char):
    print(f'\033c{sel_char['name']} Attacks, Health: [{player[0]:.0f}]:\n')
    attack(player,enemy,'You')
    print(f"The {rf_enemy['name'].lower()} now has [{enemy[0]:.0f}] health!")

    if enemy[0] < 1:
        return 'Win'
    print(f'\n\n{rf_enemy['name']} Attacks, Health: [{enemy[0]:.0f}]:\n')
    attack(enemy,player,"They")
    print(f"You now have [{player[0]:.0f}] health!\n")
    if player[0] < 1:
        return 'Fail' 
    
    inquirer.text(message="Press [Enter] to Continue").execute()
    outcome = battle(enemy,player,rf_enemy,sel_char)
    return outcome