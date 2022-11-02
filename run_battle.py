import rpg_functions

def battle (hero,enemies,introduction):
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
                break
        if hero ["health"] > 0:
            if enemy ["health"] < 1:
                print ("Congratulations")
                print ("")
                print ("All the BEARS are fast asleep!")
                print ("") 
                print (f"So now {hero ['name']} can enjoy all that is JUUUUUST RIGHT!")
                break   
        