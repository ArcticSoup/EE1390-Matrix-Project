import numpy as np
import matplotlib.pyplot as plt

# since given equation is 2x - 3y = 1
norm_vec = np.array([2, -3])
p = 1


# since given inequality is x^2 + y^2 <= 6
centre = np.array([0,0])
radius = np.sqrt(6)

# set of given points and the centre of the circle
points = np.array([
	[2, 5/2.0, 1/4.0, 1/8.0,centre[0]],
	[3/4.0, 3/4.0, -1/4.0, 1/4.0,centre[1]]
	])

# utility function to plot a line given n1, n2 and p.
def draw_line(n,p):
	x = np.arange(-15,15,1)
	y = (p - n[0]*x)/(n[1] + 0.0)

	# fill colour on the shorter side, which can be decided using
	# the centre of the circle

	# We can find the side using matrix multiplication of the centre of the circle,
	# and the normal vector

	if np.matmul(n,centre) - p > 0:
		lower_bound = 1000
	else:
		lower_bound = -1000
	plt.fill_between(x,y,np.full(30, lower_bound), color = 'pink', label = '2x - 3y - 1 > 0')
	plt.plot(x,y, color = 'cyan', linewidth=2)

# utility function to plot a circle using centre and radius
def plot_circle(centre, radius):
	circle = plt.Circle(centre, radius, fill='pink', alpha = 0.7, label = 'x^2 + y^2 <= 6')
	plt.gca().add_patch(circle)
	plt.axis(xmin = -4.0,xmax = 4.0,ymin = -3.5, ymax = 3.5)

# plot all the given points and the centre of the circle
letters = ['A', 'B', 'C', 'D']
for i in range(0,4):
	plt.plot(points[0,i], points[1,i],'o', color = 'black')
	plt.text(points[0,i] + 0.1, points[1,i] + 0.1, letters[i])
plt.plot(points[0,4], points[1,4],'o', color = 'cyan')
plt.text(points[0,4] + 0.05, points[1,4], 'O')
# plot the boundary of th given circular region given
plot_circle(centre, radius)

# plot the given line
draw_line(norm_vec,p)

# matrix containing all the points
point_set = np.vstack((np.array([points[0,0],points[1,0]]), np.array([points[0,1],points[1,1]]),
	np.array([points[0,2],points[1,2]]), np.array([points[0,3],points[1,3]]))).T

# matrix whose diagnoal entries are the sum of squares of points
square_sum = np.matmul(point_set.T, point_set)

# matrix which has entries > 0 for point lying on the other side of the line compared to origin
position_relative_to_line = np.matmul(norm_vec,point_set) - p

# matrix which has entries True if point is in the smaller part of the circle else false
answer_array = np.array([(square_sum[i,i] < 6 and position_relative_to_line[i] > 0) for i in range(0,4)])

# print(answer_array)

answer = sum(answer_array)

print(answer)

plt.grid()
plt.legend()
plt.savefig('../Figures/graph.eps', format = 'eps', dpi = 1000)
plt.show()


