from rpg_characters import my_hero, my_enemies
import rpg_functions 
from rpg_print_statements import introduction_sequence

def run_battle (hero,enemies):
    # rpg_functions.story (introduction_sequence)
    for enemy in enemies:
        # rpg_functions.hero_vs_enemy_battle (hero, enemy)
        # rpg_functions.equipment_loot (hero, enemy)
        rpg_functions.coin_collection (hero, enemy)
    return run_battle
battle = run_battle (my_hero, my_enemies)
