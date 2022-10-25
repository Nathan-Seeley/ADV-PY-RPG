
from rpg_functions import hero_vs_enemy_battle, slow_print
from rpg_variables import my_hero, enemy_one, enemy_two, enemy_three

# print_speed = slow_print ()
result = hero_vs_enemy_battle (my_hero, enemy_one)
print (result)

result = hero_vs_enemy_battle (my_hero, enemy_two)
print (result)

result = hero_vs_enemy_battle (my_hero, enemy_three)
print (result)