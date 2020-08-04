

def most_frequent_days(year):
	from datetime import date
	count_day = (date(year + 1, 1, 1) - date(year, 1, 1)).days % 7
	first_day = date(year, 1, 1).weekday()
	direct = -1 if first_day == 6 else 1
	return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday'][first_day:first_day + count_day][::direct]

	#return int(ans - ans1) % 7


for question in range(1900, 2021):
	print(f'for year == {question} answer is {most_frequent_days(question)}')


#2000, ['Saturday', 'Sunday']

weeks_day = ['0', '1', '2', '3', '4', '5', '6', '0']