import random
from colorama import Fore, init
init ()
import sys, time


def slow_print (string_to_print):
    for letter in string_to_print:
        sys.stdout.write (letter)
        sys.stdout.flush ()
        time.sleep (0.05)
    print ("")

def story_teller (story):
    print (f"{Fore.CYAN}Welcome to a childrens story adventure.")
    for line in story:
        slow_print (line)
    
def random_battle_generator (hero , enemy):
    while hero ["health"] and enemy ["health"]> 0:
        hero_attack = random.choice (hero ["attacks"])
        print (f"{Fore.GREEN}")
        slow_print (f"{enemy ['name']} loses {hero_attack [1]} energy points because of {hero ['name']}'s {hero_attack [0]} attack!")
        enemy ["health"] -= hero_attack [1]
            
        if enemy ["health"] <= 0:
            print (f"{Fore.RED}")
            slow_print (f"{enemy ['name']} has fallen asleep!")
            break
        elif enemy ["health"] >= 1:
            print (f"{Fore.LIGHTYELLOW_EX}")
            slow_print (f"{enemy ['name']} has {enemy ['health']} energy points left!")
            
        enemy_attack = random.choice (enemy ["attacks"])
        print (f"{Fore.RED}")
        slow_print (f"{hero ['name']} loses {enemy_attack [1]} energy points because of {enemy ['name']}'s {enemy_attack [0]} attack!")
        hero ["health"] -= enemy_attack [1]
        if hero ["health"] >0:
            print (f"{Fore.LIGHTYELLOW_EX}")
            slow_print (f"{hero ['name']} has {hero ['health']} energy points left!")
        elif hero ["health"] < 0:
            break

def loot_collector (hero, enemy):
    if hero ["health"] > 0:
        print (f"{Fore.GREEN}")
        slow_print (f"{hero ['name']} is equiped with {hero ['equipment']}.")
        slow_print (f"{hero ['name']} has gained {enemy ['equipment']} from {enemy ['name']}!")
        hero ["equipment"] = hero ["equipment"].union (enemy ["equipment"])
    
def coin_collector (hero, enemy):
    if hero ["health"] > 0:
        print (f"{Fore.LIGHTYELLOW_EX}") 
        slow_print (f"{hero['name']} has {hero ['coins']['copper']} copper, {hero ['coins']['silver']} silver and {hero ['coins']['gold']} gold coins")
        slow_print (f"{hero['name']} has gained {enemy ['coins']['copper']} copper, {enemy ['coins']['silver']} silver and {enemy ['coins']['gold']} gold from {enemy ['name']}!")
        hero ['coins']['copper'] = ((hero ['coins']['copper']) + (enemy ['coins'] ['copper']))
        hero ['coins']['silver'] = ((hero ['coins']['silver']) + (enemy ['coins'] ['silver']))
        hero ['coins']['gold'] = ((hero ['coins']['gold']) + (enemy ['coins'] ['gold']))

def level_increaser (hero):
    if hero ["health"] > 0:
        hero ["level"] = hero ["level"] + 1
        print (f"{Fore.GREEN}")
        slow_print (f"{hero ['name']} has increased to level {hero ['level']}!")

def new_attacks_generatror (hero):
    if hero ["health"] > 0:
        attack_strength = (50, 75, 100, 150)
        random_attack_strength = random.choice (attack_strength)
        print (f"{Fore.LIGHTYELLOW_EX}")
        slow_print (f"{hero['name']} attacks are {hero['attacks']}.")
        user_attack_name = (input (f"{hero['name']} has learned a new attack! Name the attack: "))
        new_attack_list = [(str(user_attack_name),random_attack_strength)]
        new_attack_tuple = tuple (new_attack_list)
        hero ["attacks"]  = hero ["attacks"] + new_attack_tuple
def health_increaser (hero):
    if hero ["health"] > 0:     
        hero["health"] += 15
        print (f"{Fore.LIGHTGREEN_EX}")
        slow_print (f"{hero['name']} has gained 15 energy points.")
        slow_print (f"{hero['name']} now has {hero['health']} energy points.")