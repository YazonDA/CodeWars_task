q = ["1 beer", "1 glass of water", "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer", "10 glasses of water"
]

for question in q:
	ans = sum(int(i) for i in question if i.isdigit())
	suffix = bool(ans - 1) * 'es'
	print(f'{ans} glass{suffix} of water')

