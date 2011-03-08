# initialize global variables #
MAX_SPEED = 1
STEP_DT = 0.1
AGENT_X = 10
AGENT_Y = 10
SPEED = 10 # max per-step translational speed
ANGULAR_SPEED = 90 # max angles in degrees agent can turn in one step
TIME_PER_STEP = 0.01 # min time between steps in seconds
STEPS_PER_EPISODE = 100 # max number of steps per episode
MAX_DISTANCE = 1000000 # max possible distance of objects from agent
MIN_DISTANCE = 1 # min distance from object for agent to visit it

ROOMBA_RAD = 4  # Physical Radius of Roomba, for vacuuming and collisions

FIXED_SENSORS = ['wall bump', 'self.x', 'self.y', 'closest.x', 'closest.y']
N_FIXED_SENSORS = len(FIXED_SENSORS)
S_IN_BLOCK = ['x','y','present?','reward']
N_S_IN_BLOCK = len(S_IN_BLOCK)

XDIM = 200.0
YDIM = 200.0
HEIGHT = 20.0
OFFSET = -HEIGHT/2

OBJECT_TYPE_ROOMBA = (1 << 0)
OBJECT_TYPE_WALLS = (1 << 1)
OBJECT_TYPE_FLOOR = (1 << 2)
OBJECT_TYPE_MARKER = (1 << 3)

MOE = 0      # Margin Of Error
WAIT_TIME = 0.1
