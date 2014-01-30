import vector
import boid
import numpy as np
import matplotlib.pyplot as plt

# This is the main program for running a flocking simulation in python
# It uses two objects: a 3D Cartesian vector, and a boid (a birdlike object)
# Look inside boid.py and vector.py to see the objects and their methods

# Boids follow several simple rules:
# -----
# Move towards the centre of mass of the system of boids
# Match velocities with the centre of mass of the system
# Try not to hit other boids - move away from boids if they come within a certain distance

def get_coords(boidlist):
    '''This function strips out x and y data from a list of boid objects for plotting'''
    x=[]
    y=[]

    for i in range(len(boidlist)):
        x.append(boidlist[i].r.x)
        y.append(boidlist[i].r.y)
    return x,y

# Now let's get on with the script
nboid = int(input("how many boids? "))

tmax=500 # Maximum time for the simulation to run
comstrength=0.05 # relative importance of approaching COM
vcomstrength = 0.1 # relative importance of matching velocities
avoidstrength = 1.0 # relative importance of avoidance
avoidrange = 5.0 # Sphere of avoidance radius for boids

popn = [] # This list will hold all the boid objects
boxsize = 10.0 # This boxsize will determine where the boids are initially placed
screensize = 100.0 # This will determine the size of the plotting window
dx = boxsize/(nboid)
dt = 0.5

flocktwo = vector.Three(20.0, 0.0, 0.0)

for j in range(nboid):

    # set up random positions and velocities
    r = vector.Three(np.random.rand()*boxsize,np.random.rand()*boxsize,np.random.rand()*boxsize) # Place boids at random in a box
    v = vector.Three(-2.0 + 4.0*np.random.rand(),-1.0+ 2.0*np.random.rand(),-1.0+2.0*np.random.rand()) # Give them random velocities

    # create new boid object and add to list
    d = boid.Boid(j,r,v,v,1.0)
    popn.append(d)


# Extract x and y coords for plotting
xplot,yplot = get_coords(popn)

# Plot them using matplotlib 
plt.ion() # This switches on interactive mode, so we can keep plotting on the same figure

fig1 = plt.figure() # This is the figure object
ax = fig1.add_subplot(111) # This is the axes of our figure (we can add several to make multiple plots)
ax.set_xlim(-screensize, screensize) # x and y limits of the screen
ax.set_ylim(-screensize, screensize)
scat = ax.scatter(xplot,yplot) # This plots a series of disconnected points (i.e. our boids)

# Now begin simulation
                
t = 0

obstacle = vector.Three(0.0,-10.0,0.0)

while t<tmax:
        
    # Calculate centre of mass and COM velocity
        
    com = vector.Three(0.0,0.0,0.0)
    vcom = vector.Three(0.0,0.0,0.0)

    for j in range(nboid):    
        com = com.add(popn[j].r)
        vcom = vcom.add(popn[j].v)

    # Normalise by number of boids

    com = com.scalarmult(1.0/nboid)
    vcom = vcom.scalarmult(1.0/nboid)    

    origin = vector.Three(0.0,0.0,0.0)
    # Apply flocking rules
    for j in range(nboid):        
        
        # Constrain boids to approach centre of mass
        popn[j].approach_COM(com,comstrength)
        # Boids should attempt to match COM velocity
        popn[j].match_velocities(vcom,vcomstrength)
        # Keep boids on screen by attracting them to the origin - this is optional, stops them flying off
        #popn[j].approach_COM(origin,comstrength)
        # If neighbours are in avoidance range, boids steer away
        for k in range(nboid):
            if j != k:
                sep=popn[j].r.subtract(popn[k].r) # calculate distance between boids
                if sep.mag() < avoidrange: # if distance too small, begin avoidance procedure
                    popn[j].avoid_collisions(popn[k].r,0.1)
        
        # Avoid VERY SCARY obstacle at (0,5,0) - optional
        
        #popn[j].avoid_collisions(obstacle,1.0)
        
        # Now move all the boids
        popn[j].move(dt)    

    # Get coordinates for new population
    xplot,yplot = get_coords(popn)

    # plot
    ax.clear() # clear previous plot
    ax.set_xlim(-screensize,screensize) # reset plot limits
    ax.set_ylim(-screensize,screensize)
    scat = ax.scatter(xplot,yplot) # Make another scatter plot

    plt.draw() # Draw it to the figure on screen

    # advance time
    t = t+ dt

print "Simulation Ended"



