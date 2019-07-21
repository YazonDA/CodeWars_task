''' CodeWar Task - Human readable duration format
Tag`s - ALGORITHMS FORMATS STRINGS DATES/TIME FORMATTING
4 kyu

write a function which formats a duration, given as
a number of seconds, in a human-friendly way
'''
import time


def format_duration(seconds):
    if not seconds:
        return 'now'
    ans_dict = [60, 60, 24, 365]
    ans_list = []
    for i in range(len(ans_dict)):
        ans_list.append(seconds % ans_dict[i])
        seconds = seconds // ans_dict[i]

    ans_list.append(seconds)
    ans_str = ans_list
    return ans_str


a = 936620009

answer = format_duration(a)
print(answer)
print(time.ctime(a))
