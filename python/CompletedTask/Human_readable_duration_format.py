''' CodeWar Task - Human readable duration format
Tag`s - ALGORITHMS FORMATS STRINGS DATES/TIME FORMATTING
4 kyu

write a function which formats a duration, given as
a number of seconds, in a human-friendly way
'''


def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m:
            dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'



a = 0# - 32 - 13*60

answer = format_duration(a)
print(answer)


''' This is my solution. I think that it`s not good!
def format_duration(seconds):
    if not seconds:
        return 'now'

    ans_dict = [60, 60, 24, 365, 365]
    ans_dict_1 = [1, 60, 60 * 60, 24 * 3600, 365 * 24 * 3600]
    ans_list = [seconds // (ans_dict_1[i]) % ans_dict[i] for i in range(5)]

    word_single = [' second', ' minute', ' hour', ' day', ' year']

    for num_pos in range(4, -1, -1):
        if ans_list[num_pos] > 0:
            if ans_list[num_pos] > 1:
                s = 's'
            else:
                s = ''
            ans_list[num_pos] = str(ans_list[num_pos]) + word_single[num_pos] + s

    ans_str = [i for i in ans_list[::-1] if i]
    if len(ans_str) > 1:
        a_s = [i + ', ' for i in ans_str[:-2]]
        a_s.extend([ans_str[-2], ' and ', ans_str[-1]])
    else:
        return ans_str[0]

    return ''.join(a_s)
'''