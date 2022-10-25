import sys, time

def slow_print (string_to_print):
    for letter in string_to_print:
        sys.stdout.write (letter)
        sys.stdout.flush ()
        time.sleep (0.5)
    return ("")

import random
from colorama import Fore, init 
init ()
def hero_vs_enemy_battle (hero , enemy):
    hero_health = hero ["health"]
    enemy_health = enemy ["health"]
    enemy_name = enemy ["name"]
    hero_name = hero ["name"]
    while hero_health and enemy_health >= 1:
            enemy_attack_strength = random.choice (enemy ["attacks"]) [1]
            hero_health -= enemy_attack_strength
            print (f"{Fore.RED} {hero_name} took {enemy_attack_strength} damage!")
            hero_attack_strength = random.choice (hero ["attacks"]) [1]
            enemy_health -= hero_attack_strength 
            print (f"{Fore.GREEN}{enemy_name} took {hero_attack_strength} damage!")
            if enemy_health <= 0:
                return (f"{Fore.BLUE} {enemy_name} has been vanquished by {hero_name}!")
            else:
                break
                # print (f"{Fore.BLUE} {hero_name} has been vanquished by {enemy_name}! Please try again")
                
                
    return hero_vs_enemy_battle 
            
            