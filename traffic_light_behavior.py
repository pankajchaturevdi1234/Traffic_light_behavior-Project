import time

# Constants
RED_LIGHT_TIME = 60  # If traffic is stationary for 1 minute
GREEN_LIGHT_TIME = 5  # Time to show green light if traffic is moving
YELLOW_LIGHT_TIME = 10  # Time to show yellow light for slow-moving traffic

def traffic_light_simulation():
    while True:
        traffic_condition = input("\nEnter traffic condition (standstill, moving, slow): ").strip().lower()

        if traffic_condition == "standstill":
            print("Red light! Heavy traffic detected.")
            for i in range(RED_LIGHT_TIME, 0, -1):
                print(f"Red light remaining: {i} seconds", end="\r")
                time.sleep(1)

        elif traffic_condition == "moving":
            print("Green light! Traffic is moving smoothly.")
            for i in range(GREEN_LIGHT_TIME, 0, -1):
                print(f"Green light remaining: {i} seconds", end="\r")
                time.sleep(1)

        elif traffic_condition == "slow":
            print("Yellow light! Traffic is moving slowly.")
            for i in range(YELLOW_LIGHT_TIME, 0, -1):
                print(f"Yellow light remaining: {i} seconds", end="\r")
                time.sleep(1)

        else:
            print("Invalid input! Please enter 'standstill', 'moving', or 'slow'.")

# Run the simulation
traffic_light_simulation()