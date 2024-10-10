scaffolds = open('../po_scaffold.fa').read().splitlines()
count = 0
total_length = 0
gaps = list()
longest_id = 0
prefix = 0
n50 = -1
longest_scaffold = str()
current_scaffold = str()

for line in scaffolds:
    if line[0] == '>':
        if count > 0:
                gaps.append(len(current_scaffold))
        count += 1
        if  len(current_scaffold) > len(longest_scaffold):
            longest_scaffold = current_scaffold
        current_scaffold = str()
    current_scaffold += line
    current_length = len(line)
    total_length += current_length

gaps = list(reversed(sorted(gaps)))
for i in gaps:
    prefix += i
    if prefix * 2 >= total_length:
        n50 = i
        break
print('Скаффолды:')
print('\tКоличество скаффолдов:\t\t\t', count)
print('\tДлина скаффолдов:\t\t\t', total_length)
print('\tN50:\t\t\t\t\t',n50)
print('\tДлина самого длинного скаффолда:\t', len(longest_scaffold))

num_of_gaps = 0
total_len_of_gaps = longest_scaffold.count('N')
current_gap = 0
for i in range(len(longest_scaffold)):
    if longest_scaffold[i] != 'N' and longest_scaffold[i - 1] == 'N':
        num_of_gaps += 1

print('Самый длинный скаффолд:')
print('\tКоличество гэпов:\t', num_of_gaps)
print('\tОбщая длина гэпов:\t', total_len_of_gaps)