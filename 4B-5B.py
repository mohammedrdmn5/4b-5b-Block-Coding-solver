Dictionary = [{"name": "0", "4b": '0000', "5b": '11110'}, {"name": "1", "4b": '0001', "5b": '01001'},
              {"name": "2", "4b": '0010 ', "5b": '10100'}, {"name": "3", "4b": '0011 ', "5b": '10101'},
              {"name": "4", "4b": '0100 ', "5b": '01010'}, {"name": "5", "4b": '0101 ', "5b": '01011'},
              {"name": "6", "4b": '0110 ', "5b": '01110'}, {"name": "7", "4b": '0111 ', "5b": '01111'},
              {"name": "8", "4b": '1000 ', "5b": '10010'}, {"name": "9", "4b": '1001 ', "5b": '10011'},
              {"name": "A", "4b": '1010 ', "5b": '10110'}, {"name": "B", "4b": '1011 ', "5b": '10111'},
              {"name": "C", "4b": '1100 ', "5b": '11010'}, {"name": "D", "4b": '1101 ', "5b": '11011'},
              {"name": "E", "4b": '1110 ', "5b": '11100'}, {"name": "F", "4b": '1111 ', "5b": '11101'}]

value = input('Enter the HEX value: ').upper()

print('4 Bit => ', end='\t')
for every_input in value:
    for every_dict in Dictionary:
        if every_input == every_dict['name']:
            print(every_dict['4b'], end=' ')

print('\n5 Bit => ', end='\t')
for every_input in value:
    for every_dict in Dictionary:
        if every_input == every_dict['name']:
            print(every_dict['5b'], end=' ')

