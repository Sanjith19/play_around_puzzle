import os,sys,re

# 12 red cubes, 13 green cubes, and 14 blue cubes
input_fl = sys.argv[1]

def get_games(inp):
    cubes_count = {'red': 12, 'green': 13, 'blue': 14}
    split_line = inp.split(';')
    game_lst = []
    for line in split_line:
        color_count = {'blue': 0, 'green': 0, 'red': 0}
        for color in list(color_count.keys()):
            count = re.findall(' (\d+) ' + color, line)
            if not count:
                color_count[color] = 0
            else:
                color_count[color] = int(count[0])

            if int(color_count[color]) <= int(cubes_count[color]):
                game_count = int(re.findall('Game ' + '(\d+)' + ':', split_line[0])[0])
            else:
                game_count = 0
            game_lst.append(game_count)
    game = min(game_lst)
    return game
if __name__ == '__main__':
    game_count = 0
    if os.path.isfile(input_fl):
        fl = open(input_fl, 'r')
        flout = open('out2.csv','w')
        for line in fl:
            game_out = get_games(line)
            line = line.replace(',',':')
            line = line.replace(';',',')
            out_string = str(game_out) + ',' + line
            flout.write(out_string)
            game_count += game_out
        fl.close()
        flout.close()
    else:
        game_count += get_games(input_fl)
    print(game_count)
