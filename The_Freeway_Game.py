'''CodeWars task - The Freeway Game
Tag`s - ALGORITHMS
6 kyu
Instruction is here:
https://www.codewars.com/kata/the-freeway-game/train/python'''

import pysnooper
@pysnooper.snoop()
def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):
    ans = 0
    for i in other_cars:
    	time_m = dist_km_to_exit / my_speed_kph
    	time_h = (dist_km_to_exit / i[1]) + (i[0] / 60)
    	if ((i[0] / 60) < 0 and i[1] > my_speed_kph) or ((i[0] / 60) > 0 and i[1] < my_speed_kph):
    		pass
    	elif time_m < time_h:
    		ans += 1
    	elif time_m > time_h:
    		ans -= 1
    return ans


a = [[50.0, 130.0, [[-1.0, 120.0], [-1.5, 120.0]], 2],
[50.0, 110.0, [[1.0, 120.0], [1.5, 125.0]], -2],
[50.0, 120.0, [[-1.0, 115.0], [-1.5, 110.0],[1.0, 130.0], [1.5, 130.0]], 0],
[30.0, 100.0, [[-1.0, 110.0], [-0.7, 102.0], [-1.5, 108.0]], 0],
[30.0, 130.0, [[1.0, 120.0], [0.7, 125.0], [1.5, 110.0]], 0],
[50, 130, [[-1.4366258083940355, 132.77438071869292],
[4.526981289656501, 119.22881833462822],
[-3.3880220641791903, 113.45508727198846],
[-0.2013490990995379, 110.53810451164581],
[1.8208204116344104, 119.95891329889353]], 0],
[50, 130, [[-0.8219083795606039, 111.13965189290249],
[-0.7694637798801924, 118.4517526479155],
[3.776865499920385, 110.8323427495286],
[4.18387090751332, 116.70913433866652],
[-4.028203610334051, 112.23064285463585]], 2]]

for i in a:
	if freeway_game(i[0], i[1], i[2]) == i[3]:
		print('Correct!')
	else:
		print('Wrong!')

