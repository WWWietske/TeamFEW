#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True
from copy import deepcopy
import rndom as rd
import positions as pos
import csvtries
import bfs
import car
import truck
import visualize as vis


# array of all files for the games
games = ['none', '../datasets/Game #1.csv', '../datasets/Game #2.csv',
         '../datasets/Game #3.csv', '../datasets/Game #4.csv',
         '../datasets/Game #5.csv', '../datasets/Game #6.csv',
         '../datasets/Game #7.csv']


def main():
    # check if game exists, open file for game
    game = int(sys.argv[1])
    if game == 0 or game > 7:
        sys.exit("Game does not exist, choose 1 - 7")
    else:
        f = open(games[game], 'rb')

    # set up exits for each of the games
    if game == 1 or game == 2 or game == 3:
        exit = pos.CarPosition(4, 5, 2, 2)
        width, height = 6, 6
    elif game == 4 or game == 5 or game == 6:
        exit = pos.CarPosition(7, 8, 4, 4)
        width, height = 9, 9
    elif game == 7:
        exit = pos.CarPosition(10, 11, 5, 5)
        width, height = 12, 12

    # set up grid with vehicles
    grid_rnd = csvtries.run(f, width, height, exit)
    grid_bfs = deepcopy(grid_rnd)
    grid_test = grid_rnd.copy_grid()

    f.close()

    print "--- Random algoritme ---"
    rd.runrandom(grid_rnd)
    print "--- bfs ---"
    bfs.runbfs(grid_test, exit)

if __name__ == "__main__":
    main()
