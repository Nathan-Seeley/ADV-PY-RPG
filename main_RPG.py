from rpg_characters import my_hero, my_enemies
import rpg_functions 
from rpg_print_statements import introduction_sequence

def run_battle (hero,enemies,introduction):
    rpg_functions.story_teller (introduction)
    while hero ["health"] > 0:
        for enemy in enemies:
            if hero["health"] > 0:
                rpg_functions.random_battle_generator (hero, enemy)
                rpg_functions.loot_collector (hero, enemy)
                rpg_functions.coin_collector (hero, enemy)
                rpg_functions.level_increaser (hero)
                rpg_functions.new_attacks_generatror (hero)
                rpg_functions.health_increaser (hero)
            elif hero ["health"] < 1:
                print ("OH NO!!! {hero ['name']} was chased out of the house.") 
                print ("Going into a house without permission may not be the best idea?") 
                break
        if hero ["health"] > 0:
            while enemy ["health"] < 1:
                print ("All the BEARS are fast asleep!") 
                print (f"So now {hero ['name']} can enjoy all that is JUUUUUST RIGHT!")
            break   
    return run_battle
battle = run_battle (my_hero, my_enemies,introduction_sequence)

