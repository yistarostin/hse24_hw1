contigs = open('../po_contig.fa').read().splitlines()
count = 0
total_length = 0
longest = 0
now = 0
prefix = 0
n50 = -1
gaps = list()
for line in (contigs):
    if line[0] == '>':
        if count > 0:
                gaps.append(now)
        count += 1
        longest = max(longest, now)
        now = 0
    current_length = len(line)
    now += current_length
    total_length += current_length

gaps = list(reversed(sorted(gaps)))
for i in gaps:
    prefix += i
    if prefix * 2 >= total_length:
        n50 = i
        break

 
print('Контиги:')
print('\tКоличество контигов:\t\t', count)
print('\tДлина контигов:\t\t\t', total_length)
print('\tДлина самого длинного контига:\t', longest)
print('\tN50:\t\t\t\t', n50)