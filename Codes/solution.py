import numpy as np
import matplotlib.pyplot as plt

# sincegiven equation is 2x - 3y = 1
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
	plt.fill_between(x,y,np.full(30, 1000 if (np.matmul(n,centre) - p) > 0 else -1000), color = 'red')
	plt.plot(x,y)

# utility function to plot a circle using centre and radius
def plot_circle(centre, radius):
	circle = plt.Circle(centre, radius, fill=None)
	plt.gca().add_patch(circle)
	plt.axis('scaled')

# plot all the given points and the centre of the circle
plt.plot(points[0,:], points[1,:],'o')

# plot the boundary of th given circular region given
plot_circle(centre, radius)

# plot the given line
draw_line(norm_vec,p)

# add all points lying oposite to centre and inside the circle
answer = sum([(np.matmul(norm_vec,k) - p) > 0 and (k[0]**2 + k[1]**2 < 6)for k in ([points[0,i], points[1,i]] for i in range(0,5))])

print(answer)

plt.grid()
plt.show()


