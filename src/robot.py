# Main module for robot movement logic
# # import time
# # import math
# # import random
# #
# # # Constants
# # MAP_SIZE = 10  # Map size in meters
# # TIME_STEP = 0.002  # Time step in seconds
# # SPEED = 1  # Speed in meters per second
# #
# # # Initialize the robot's position
# # robot_x = MAP_SIZE / 2
# # robot_y = MAP_SIZE / 2
# #
# # def get_new_heading():
# #     """Generate a random new heading between 0 and 359 degrees."""
# #     return random.randint(0, 359)
# #
# # def move_robot(x, y, heading):
# #     """Update the robot's position based on the heading and speed."""
# #     radian_angle = math.radians(heading)
# #     x += math.cos(radian_angle) * SPEED * TIME_STEP
# #     y += math.sin(radian_angle) * SPEED * TIME_STEP
# #     # Ensure the robot stays within bounds
# #     x = max(0, min(x, MAP_SIZE))
# #     y = max(0, min(y, MAP_SIZE))
# #     return x, y
# #
# # def main():
# #     heading = get_new_heading()
# #     print(f"Initial heading: {heading} degrees")
# #     print("Starting simulation...")
# #
# #     try:
# #         while True:
# #             global robot_x, robot_y
# #             robot_x, robot_y = move_robot(robot_x, robot_y, heading)
# #             print(f"Current location: ({robot_x:.2f}, {robot_y:.2f})")
# #             time.sleep(TIME_STEP)
# #     except KeyboardInterrupt:
# #         print("Simulation stopped.")
# #
# # if __name__ == "__main__":
# #     main()
#
# import time
# import math
# import random
#
# # Constants
# MAP_SIZE = 10  # Map size in meters
# TIME_STEP = 1  # Time step in seconds
# SPEED = 1  # Speed in meters per second
# HEADING_UPDATE_INTERVAL = 30  # Heading update interval in seconds
#
# # Initialize the robot's position
# robot_x = MAP_SIZE / 2
# robot_y = MAP_SIZE / 2
#
# def get_new_heading():
#     """Generate a random new heading between 0 and 359 degrees."""
#     return random.randint(0, 359)
#
# def move_robot(x, y, heading):
#     """Update the robot's position based on the heading and speed."""
#     radian_angle = math.radians(heading)
#     x += math.cos(radian_angle) * SPEED * TIME_STEP
#     y += math.sin(radian_angle) * SPEED * TIME_STEP
#     # Ensure the robot stays within bounds
#     x = max(0, min(x, MAP_SIZE))
#     y = max(0, min(y, MAP_SIZE))
#     return x, y
#
# def main():
#     heading = get_new_heading()
#     last_heading_change = time.time()
#     print(f"Initial heading: {heading} degrees")
#     print("Starting simulation...")
#
#     try:
#         while True:
#             current_time = time.time()
#             if current_time - last_heading_change >= HEADING_UPDATE_INTERVAL:
#                 heading = get_new_heading()
#                 last_heading_change = current_time
#                 print(f"New heading: {heading} degrees")
#
#             global robot_x, robot_y
#             robot_x, robot_y = move_robot(robot_x, robot_y, heading)
#             print(f"Current location: ({robot_x:.2f}, {robot_y:.2f}), Heading:{heading}")
#             time.sleep(TIME_STEP)
#             # print(current_time-last_heading_change)
#             # print(last_heading_change)
#     except KeyboardInterrupt:
#         print("Simulation stopped.")
#
# if __name__ == "__main__":
#     main()
import time
import math
import random

# Constants
MAP_SIZE = 100  # Map size in meters (both width and height)
TIME_STEP = 1  # Time step in seconds
SPEED = 1  # Speed in meters per second
HEADING_UPDATE_INTERVAL = 30  # Heading update interval in seconds

# Initialize the robot's position at the center (0, 0)
robot_x = 0
robot_y = 0


def get_new_heading():
    """Generate a random new heading between 0 and 359 degrees."""
    return random.randint(0, 359)


def move_robot(x, y, heading):
    """Update the robot's position based on the heading and speed."""
    radian_angle = math.radians(heading)
    x += math.cos(radian_angle) * SPEED * TIME_STEP
    y += math.sin(radian_angle) * SPEED * TIME_STEP

    # Check if the robot is outside the bounds, reset to center if it is
    if not (-MAP_SIZE / 2 <= x <= MAP_SIZE / 2) or not (-MAP_SIZE / 2 <= y <= MAP_SIZE / 2):
        x, y = 0, 0  # Reset position to the center (0, 0)
        print("Robot out of bounds, resetting to center (0, 0)")

    return x, y


def main():
    heading = get_new_heading()
    last_heading_change = time.time()
    print(f"Initial heading: {heading} degrees")
    print("Starting simulation...")

    try:
        while True:
            current_time = time.time()
            if current_time - last_heading_change >= HEADING_UPDATE_INTERVAL:
                heading = get_new_heading()
                last_heading_change = current_time
                print(f"New heading: {heading} degrees")

            global robot_x, robot_y
            robot_x, robot_y = move_robot(robot_x, robot_y, heading)
            print(f"Current location: ({robot_x:.2f}, {robot_y:.2f}), Heading:{heading}")
            time.sleep(TIME_STEP)
    except KeyboardInterrupt:
        print("Simulation stopped.")


if __name__ == "__main__":
    main()
# Main module for robot movement logic
