
import random
from colorama import Fore, init 
init ()
import sys, time


def slow_print (string_to_print):
    init()
    for letter in string_to_print:
        sys.stdout.write (letter)
        sys.stdout.flush ()
        time.sleep (0.05)
    print ("")
def story (introduction):
    for line in introduction:
        slow_print (f"{Fore.LIGHTYELLOW_EX} {line}")
    
def hero_vs_enemy_battle (hero , enemy):
    while hero ["health"] and enemy ["health"] >= 1:
        enemy_attack = random.choice (enemy ["attacks"])
        slow_print (f"{Fore.RED} {hero ['name']} takes {enemy_attack [1]} damage from {enemy ['name']} while using {enemy_attack [0]} attack!")
        hero ["health"] -= enemy_attack [1]
        slow_print (f"{Fore.LIGHTYELLOW_EX} {hero ['name']} has {hero ['health']} health left!")
           
        hero_attack = random.choice (hero ["attacks"])
        slow_print (f"{Fore.GREEN} {enemy ['name']} takes {hero_attack [1]} damage from {hero ['name']} while using {hero_attack [0]} attack!")
        enemy ["health"] -= hero_attack [1]
        slow_print (f"{Fore.LIGHTYELLOW_EX} {enemy ['name']} has {enemy ['health']} health left!")
            
        if enemy ["health"] <= 0:
            slow_print (f"{Fore.GREEN} {enemy ['name']} has died! Congratulations!")
            return (f"{hero ['name']} now has {hero ['health']} left!")  
        elif hero ["health"] <= 0:
            slow_print (f"{Fore.RED} {hero ['name']} has died. Try again if you dare!")
            break

def equipment_loot (hero, enemy):
    if hero ["health"] > 0:
        new_hero_equipment_set = (hero ["equipment"]).union (enemy ["equipment"])
        slow_print (f"{Fore.GREEN} {hero ['name']} now has {new_hero_equipment_set} for equipment.")
        
def coin_collection (hero, enemy):
    if hero ["health"] > 0:
        slow_print (f"{Fore.LIGHTYELLOW_EX} {hero['name']} has {hero ['coins']['copper']} copper, {hero ['coins']['silver']} silver and {hero ['coins']['gold']} gold coins")
        new_coin_count_copper = ((hero ['coins']['copper']) + (enemy ['coins']['copper']))
        new_coin_count_silver = ((hero ['coins']['silver']) + (enemy ['coins']['silver']))
        new_coin_count_gold = ((hero ['coins']['gold']) + (enemy ['coins']['gold']))
        slow_print (f"{Fore.Green} {hero['name']} has gained {enemy ['coin']['copper']} copper, {enemy ['coin']['silver']} silver and {enemy ['coin']['gold']} gold from {enemy ['name']}!")   
        slow_print (f"{Fore.GREEN} {hero ['name']} now has {new_coin_count_copper} copper, {new_coin_count_silver} silver and {new_coin_count_gold} gold coins!")

    
      
