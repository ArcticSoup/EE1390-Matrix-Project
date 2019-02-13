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
	plt.fill_between(x,y,np.full(30, lower_bound), color = 'yellow')
	plt.plot(x,y, color = 'red')

# utility function to plot a circle using centre and radius
def plot_circle(centre, radius):
	circle = plt.Circle(centre, radius, fill=None)
	plt.gca().add_patch(circle)
	plt.axis('scaled')

# plot all the given points and the centre of the circle
plt.plot(points[0,:], points[1,:],'o', color = 'blue')

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
plt.savefig('../Figures/graph.eps', format = 'eps', dpi = 1000)
plt.show()


