# functions
# f(x) = x + 5
# f(x, y) = 2 * x + y
# f(x) = 2 * x + y
def calculate_area(x):
	area = x * x
	return area

def sum_nums(x, y):
	res = x + y
	print(res)

# main
area1 = calculate_area(5)
area1 += 5
area2 = calculate_area(9)
print(area1, area2)
sum_nums(area1, area2)