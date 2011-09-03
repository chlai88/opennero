# OpenNero will execute ModMain when this mod is loaded
from Tower.client import ClientMain

def ModMain():
    ClientMain()

def StartMe():
    from Tower.module import getMod
    getMod().set_speedup(1.0) # full speed ahead
    getMod().start_sarsa() # start an algorithm for headless mode
