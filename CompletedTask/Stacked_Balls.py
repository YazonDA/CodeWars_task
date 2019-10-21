'''CodeWars task - Stacked Balls
Tag`s - FUNDAMENTALS
7 kyu
I have stacked some cannon balls in a triangle-based pyramid.
Given the number of layers of my stack, what is the total height?
Return the height as multiple of the ball diameter.
layers >= 0
approximate answers (within 0.001) are good enough.'''


def stack_height_3d(layers):
    return ((2 / 3) ** (1 / 2)) * (layers - 1) + 1 if layers else 0


for i in range(12):
	answer = stack_height_3d(i)
	print(answer)

# nice solution like this
# return layera and f(layers)
#