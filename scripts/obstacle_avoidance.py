from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import random

print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

waypoints = [
    (37.4289, -122.1760, 20),
    (37.4295, -122.1750, 20),
    (37.4290, -122.1740, 20)
]

def detect_obstacle():
    # Simulated obstacle detection
    return random.choice([False, False, False, True])  # 25% chance

def reroute(lat, lon, alt):
    print("Obstacle detected! Rerouting...")
    new_lat = lat + 0.0001
    new_lon = lon + 0.0001
    return LocationGlobalRelative(new_lat, new_lon, alt)

def arm_and_takeoff(target_alt):
    print("Arming and taking off...")
    while not vehicle.is_armable:
        time.sleep(1)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        time.sleep(1)
    vehicle.simple_takeoff(target_alt)
    while vehicle.location.global_relative_frame.alt < target_alt * 0.95:
        time.sleep(1)
    print("Target altitude reached.")

def fly_with_avoidance(points):
    for lat, lon, alt in points:
        if detect_obstacle():
            loc = reroute(lat, lon, alt)
        else:
            loc = LocationGlobalRelative(lat, lon, alt)
        print(f"Flying to {loc.lat}, {loc.lon}")
        vehicle.simple_goto(loc)
        time.sleep(15)

if __name__ == "__main__":
    arm_and_takeoff(20)
    fly_with_avoidance(waypoints)
    vehicle.mode = VehicleMode("RTL")
    vehicle.close()
    print("Mission completed with obstacle avoidance.")
