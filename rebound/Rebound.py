import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Move params
g = -9.8 # Gravity
v0_x = 10 # Initial Vx
v0_y = 10 # Initial Vy
m = 1 # Mass

# Time
t_total = 20  # Duration animation in seconds
fps = 64      # Fps
dt = 1 / fps  # Time interval between frames

fig, ax = plt.subplots() # Create figs and axis
ax.set(xlim=[0, 15], ylim=[0, 8], xlabel='X [m]', ylabel='Y [m]') # Graphic limits
scat = ax.scatter([], [], c="r", s=50) # Creation point

x = 1   # Initial position axis X
y = 1   # Initial position axis X
vx = v0_x  # Initial velocity in axis X
vy = v0_y  # Initial velocity in axis Y

air_resistance = 0.00  # Air resistance

def update(frame):
    global x, y, vx, vy
    ax.cla() # Clean graphic
    # Update X and Y position
    x += vx * dt
    y += vy * dt
    
    vy += g * dt
    
    if y <= 0 :
        y = 0
        vy = -vy *0.8  
    
    if x >= 15 or x<=0:
        vx = -vx * 0.8
    
    # Simulate air resistance
    vx *= (1 - air_resistance / m)  
    vy *= (1 - air_resistance / m)  
    
    # Draw new point
    ax.scatter(x, y, c="r", s=50)
    
    # ReDraw labels and limits
    ax.set(xlim=[0, 15], ylim=[0, 8], xlabel='X [m]', ylabel='Y [m]')
    
    return scat,

# Create animation
ani = animation.FuncAnimation(fig=fig, func=update, frames=int(t_total / dt), interval=dt * 1000)

# Show graphic
plt.show()
