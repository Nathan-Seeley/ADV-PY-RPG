
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

def story (introduction):
    for line in introduction:
        slow_print (f"{Fore.LIGHTYELLOW_EX} {line}")
    
def hero_vs_enemy_battle (hero , enemy):
    while hero ["health"] and enemy ["health"] >= 1:
        
            hero_attack = random.choice (hero ["attacks"])
            slow_print (f"{Fore.GREEN} {enemy ['name']} takes {hero_attack [1]} damage from {hero ['name']} while using {hero_attack [0]} attack!")
            enemy ["health"] -= hero_attack [1]
            if enemy ["health"] <= 0:
                slow_print (f"{Fore.GREEN} {enemy ['name']} has died! Congratulations!")
                break
            elif enemy ["health"] >= 1:
                slow_print (f"{Fore.LIGHTYELLOW_EX} {enemy ['name']} has {enemy ['health']} health left!")
            enemy_attack = random.choice (enemy ["attacks"])
            slow_print (f"{Fore.RED} {hero ['name']} takes {enemy_attack [1]} damage from {enemy ['name']} while using {enemy_attack [0]} attack!")
            hero ["health"] -= enemy_attack [1]
            
            if hero ["health"] <= 0:
                slow_print (f"{Fore.RED} {hero ['name']} has died. Try again if you dare!")
                break
            elif hero ["health"] >=1:
                slow_print (f"{Fore.LIGHTYELLOW_EX} {hero ['name']} has {hero ['health']} health left!")
                
def equipment_loot (hero, enemy):
    if hero ["health"] > 0:
        slow_print (f"{Fore.GREEN} {hero ['name']} has {hero ['equipment']}.")
        slow_print (f"{Fore.GREEN} {hero ['name']} has gained {enemy ['equipment']} from {enemy ['name']}!")
        hero ["equipment"] = hero ["equipment"].union (enemy ["equipment"])
    

def coin_collection (hero, enemy):
    if hero ["health"] > 0:
        slow_print (f"{Fore.LIGHTYELLOW_EX} {hero['name']} has {hero ['coins']['copper']} copper, {hero ['coins']['silver']} silver and {hero ['coins']['gold']} gold coins")
        slow_print (f"{Fore.GREEN} {hero['name']} has gained {enemy ['coins']['copper']} copper, {enemy ['coins']['silver']} silver and {enemy ['coins']['gold']} gold from {enemy ['name']}!")
        hero ['coins']['copper'] = ((hero ['coins']['copper']) + (enemy ['coins'] ['copper']))
        hero ['coins']['silver'] = ((hero ['coins']['silver']) + (enemy ['coins'] ['silver']))
        hero ['coins']['gold'] = ((hero ['coins']['gold']) + (enemy ['coins'] ['gold']))
     
        
    
    


    
      
