formula_dict_3b = [{'input': '000', 'negative': '1011', 'positive': '0100'},
                   {'input': '001', 'negative': '1001', 'positive': '1001'},
                   {'input': '010', 'negative': '0101', 'positive': '0101'},
                   {'input': '011', 'negative': '1100', 'positive': '0011'},
                   {'input': '100', 'negative': '1101', 'positive': '0010'},
                   {'input': '101', 'negative': '1010', 'positive': '1010'},
                   {'input': '110', 'negative': '0110', 'positive': '0110'}
                   ]
formula_dict_5b = [{'input': '00000', 'negative': '100111', 'positive': '011000'},
                   {'input': '00001', 'negative': '011101', 'positive': '100010'},
                   {'input': '00010', 'negative': '101101', 'positive': '010010'},
                   {'input': '00011', 'negative': '110001', 'positive': '110001'},
                   {'input': '00100', 'negative': '110101', 'positive': '001010'},
                   {'input': '00101', 'negative': '101001', 'positive': '101001'},
                   {'input': '00110', 'negative': '011001', 'positive': '011001'},
                   {'input': '00111', 'negative': '111000', 'positive': '000111'},
                   {'input': '01000', 'negative': '111001', 'positive': '000110'},
                   {'input': '01001', 'negative': '100101', 'positive': '100101'},
                   {'input': '01010', 'negative': '010101', 'positive': '010101'},
                   {'input': '01011', 'negative': '110100', 'positive': '110100'},
                   {'input': '01100', 'negative': '001101', 'positive': '001101'},
                   {'input': '01101', 'negative': '101100', 'positive': '101100'},
                   {'input': '01110', 'negative': '011100', 'positive': '011100'},
                   {'input': '01111', 'negative': '010111', 'positive': '101000'},
                   {'input': '10000', 'negative': '011011', 'positive': '100100'},
                   {'input': '10001', 'negative': '100011', 'positive': '100011'},
                   {'input': '10010', 'negative': '010011', 'positive': '010011'},
                   {'input': '10011', 'negative': '110010', 'positive': '110010'},
                   {'input': '10100', 'negative': '001011', 'positive': '001011'},
                   {'input': '10101', 'negative': '101010', 'positive': '101010'},
                   {'input': '10110', 'negative': '011010', 'positive': '011010'},
                   {'input': '10111', 'negative': '111010', 'positive': '000101'},
                   {'input': '11000', 'negative': '110011', 'positive': '001100'},
                   {'input': '11001', 'negative': '100110', 'positive': '100110'},
                   {'input': '11010', 'negative': '010110', 'positive': '010110'},
                   {'input': '11011', 'negative': '110110', 'positive': '001001'},
                   {'input': '11100', 'negative': '001110', 'positive': '001110'},
                   {'input': '11101', 'negative': '101110', 'positive': '010001'},
                   {'input': '11110', 'negative': '011110', 'positive': '100001'},
                   {'input': '11111', 'negative': '101011', 'positive': '010100'}
                   ]

value = input('Enter the 8Bit (2 HEX ONLY) value: ').upper()

ini_string = value

print(f"\nInitial string:\t{ini_string}\n")

res = "{0:08b}".format(int(ini_string, 16))

print('H\tG\tF\tE\tD\tC\tB\tA')
for bit in res:
    print(bit, end='\t')
index = 0
temp_store_last5 = list()
temp_store_first3 = list()
store_f5l3 = list()

for bit in res:
    if index < 3:
        temp_store_first3.append(bit)
    else:
        temp_store_last5.append(bit)
    index += 1

for bit in temp_store_last5:
    store_f5l3.append(bit)
for bit in temp_store_first3:
    store_f5l3.append(bit)

num_of_ones = 0
num_of_zeros = 0

print('\n\nE\tD\tC\tB\tA\tH\tG\tF')
for bit in store_f5l3:
    print(bit, end='\t')
    if bit == '0':
        num_of_zeros += 1
    else:
        num_of_ones += 1

result = num_of_ones - num_of_zeros

join_5b = "".join(temp_store_last5)

join_3b = "".join(temp_store_first3)

bit_of_5_result = ''
index_of_5b = 0
for bit_of_5 in formula_dict_5b:
    if join_5b == bit_of_5['input']:
        if result >= 0:
            bit_of_5_result = bit_of_5['positive']
            break
        else:
            bit_of_5_result = bit_of_5['negative']
            break
    index_of_5b += 1

bit_of_3_result = ''
index_of_3b = 0
for bit_of_3 in formula_dict_3b:
    if join_3b == bit_of_3['input']:
        if result >= 0:
            bit_of_3_result = bit_of_3['positive']
            break
        else:
            bit_of_3_result = bit_of_3['negative']
            break
    index_of_3b += 1

print(f"""\n\nRunning Disparity   = Number of ones – Number of zeros
Here = {num_of_ones} – {num_of_zeros}  = {result}
5b/6b code table, D.{index_of_5b}, {join_5b} is {bit_of_5_result} and 3b/4b code table, D.x.{index_of_3b}, {join_3b} is {bit_of_3_result}.
Combine these bits will result of {bit_of_5_result}{bit_of_3_result}""")
