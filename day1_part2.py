# Your calculation isn't quite right. It looks like some 
# of the digits are actually spelled out with letters: 
# one, two, three, four, five, six, seven, eight, and 
# nine also count as valid "digits".
# Equipped with this new information, you now need to 
# find the real first and last digit on each line. 
#For example:
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 
# 13, 24, 42, 14, and 76. Adding these together produces 
# 281.

# What is the sum of all of the calibration values?

# Coding

import re

dict_numbers_3 = {'one': '1',
    'two': '2',
    'six': '6'}

dict_numbers_4 = {'four': '4',
    'five': '5',
    'nine': '9',
    'zero': '0'}

dict_numbers_5 = {'three': '3',
    'seven': '7',
    'eight': '8'}


with open('input_day1_part1.txt') as example:
    contents = example.readlines()
    numbers = list()
    j = 0
    j3 = 3
    j4 = 4
    j5 = 5
    for i in contents:#linha da lista
        for k in i: #letra da linha
            if k == 'o'or k == 't' or k == 's':
                if dict_numbers_3.get(i[j:j3]):
                    matches = ''.join(dict_numbers_3[i[j:j3]])
                    numbers.append(matches)                  
            
            if k == 'f'or k == 'n' or k == 'z':
                if dict_numbers_4.get(i[j:j4]):
                    matches = ''.join(dict_numbers_4[i[j:j4]])
                    numbers.append(matches)

            if k == 't'or k == 's' or k == 'e':
                if dict_numbers_5.get(i[j:j5]):
                    matches = ''.join(dict_numbers_5[i[j:j5]])
                    numbers.append(matches)
                
            if k.isdigit():
                numbers.append(k)
            else:
                pass

            j+=1
            j3+=1
            j4+=1
            j5+=1
        j=0
        j3=3
        j4=4
        j5=5
        numbers.append('a')
  
    final_numbers = [''.join(item) for item in numbers]
    result = []
    temp_list = []
    for i in final_numbers:
        if i == 'a':
            result.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i)

    result_final = 0
    for j in result:
        a = (j[0]) + (j[-1])
        result_final = int(a)+result_final

    
    print(result_final)