'''CodeWars task - Torrent download
Tag`s - FUNDAMENTALS
7 kyu
nput:
Array of files
File example: {"name": "alien", "size_GB": 38.0, "speed_Mbps": 38}
Output:
List of files in the order of completed download
Time in seconds to download last file'''


def torrent(files):
	#time = lambda x: int(x['size_GB'] / x['speed_Mbps'] * 8000)
	#ans = [(i['name'], int(i['size_GB'] / i['speed_Mbps'] * 8000)) for i in files]
	#ans = sorted([(i['name'], int(i['size_GB'] / i['speed_Mbps'] * 8000)) for i in files])
	ans = sorted(
				sorted(
					[(i['name'], i['size_GB'] / i['speed_Mbps'] * 8000)
					for i in files]), 
				key=lambda x: x[1])
	return [i[0] for i in ans], ans[-1][1]
	#return ans

file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}
file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}

ask = [
[[file_1, file_2, file_3],(["terminator", "alien", "predator"], 152000)],
[[file_1, file_4],(["alien", "zombieland"], 8000)],
[[file_4, file_1],(["alien", "zombieland"], 8000)]
]

for i in range(len(ask)):
	answer = torrent(ask[i][0])
	ans_txt = 'Correct' if answer == ask[i][1] else 'Wrong'
	print(f'Answer {answer} is {ans_txt}!')
