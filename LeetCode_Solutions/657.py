def main(moves):
    d = {'L':0, 'R':0, 'U':0,'D':0}

    for move in moves:
        if move in d:
            d[move] += 1

    if d['L'] == d['R'] and d['D'] == d['U']:
        print('even')

main(['L','R'])