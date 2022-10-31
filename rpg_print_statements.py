from colorama import Fore, init 
init ()

welcome_story_one = ("After a long journey you are exhausted but then you see a house in a clearing ahead!")
welcome_story_two = ("You are starving and tired. All that you want is somewhere to sit, eat and sleep!")
welcome_story_three = ("You go in, but as you do, you are confronted by three beasts!")
battle_question_one = ("Do you have what it takes to defeat these three?")
introduction_sequence = (welcome_story_one,welcome_story_two,welcome_story_three,battle_question_one)


# enemy_damage = (f"{Fore.GREEN}{enemy['name']} took {hero ['attack'][1]} damage!")
# hero_damage = (f"{Fore.RED} {hero ['name']} took {enemy ['attack'][1]} damage!")
# enemy_death = (f"{Fore.GREEN} {enemy ['name']} has been vanquished by {hero ['name']}!")
# hero_death = (f"{Fore.RED} {hero['name']} has been vanquished by {enemy ['name']}!")
# hero_loot = (f"{Fore.GREEN} {hero ['name']} has looted {enemy['equipment']}!")
# hero_equipment_update = (f"{Fore.GREEN} {hero ['name']} now has {hero ['equipment'].update(enemy ['equipment'])}!")