from Roulette import Roulette


roulette = Roulette.fromFile('namesFile')

while 0 < roulette.getUncheckedPlayersCount():
    print(roulette.spinAndShot())

