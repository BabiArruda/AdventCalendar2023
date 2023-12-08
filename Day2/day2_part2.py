# --- Part Two ---
# The Elf says they've stopped producing snow because they aren't getting any water! 
#He isn't sure why the water stopped; however, he can show you how to get to the water source 
#to check it out for yourself. It's just up ahead!
# As you continue your walk, the Elf poses a second question: in each game you played, 
#what is the fewest number of cubes of each color that could have been in the bag to make the 
#game possible?
# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. 
# If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied 
#together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 
#630, and 36, respectively. Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of 
#the power of these sets?

import re
import operator
    
with open('/home/barbara/Codes_Projects/AdventCalendar2023/Day2/input_day2.txt') as example:
    games = example.readlines()
    final_games = list()
    
for i in games:
    new_game = i.split(';')
    final_games.append(new_game)
 
colours = {'red' : [], 'blue' : [], 'green': [], 'game': []}
count = 0
result = []

for i in final_games:
    for j in i: #primeira tirada de mao
        temp_list = j.split(',') #analise de cada cor
        while count < len(temp_list):
            if 'red' in temp_list[count]:
                red = re.findall(r'-?\d+(?:\.\d+)?', temp_list[count])
                if len(red) == 2 :
                    colours['game'].append(int(red.pop(0)))
                    colours['red'].append(int(red.pop()))
                else:
                    colours['red'].append(int(red.pop()))
            elif 'blue' in temp_list[count]:
                blue = re.findall(r'-?\d+(?:\.\d+)?', temp_list[count])
                if len(blue) == 2:
                    colours['game'].append(int(blue.pop(0)))
                    colours['blue'].append(int(blue.pop()))
                else:
                    colours['blue'].append(int(blue.pop()))
            elif 'green' in temp_list[count]:
                green = re.findall(r'-?\d+(?:\.\d+)?', temp_list[count])
                if len(green) == 2:
                    colours['game'].append(int(green.pop(0)))
                    colours['green'].append(int(green.pop()))
                else:
                    colours['green'].append(int(green.pop()))
            
            count +=1
        count = 0
    max_red = max(colours['red'])
    max_blue = max(colours['blue'])
    max_green = max(colours['green'])
    temp_result = max_red*max_blue*max_green
    result.append(temp_result)
    colours = {'red' : [], 'blue' : [], 'green': [], 'game': []}
    k = 0

print(sum(result))

        