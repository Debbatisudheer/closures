def create_navigation_algorithm():
    # Initial sensor data
    sensor_data = {"altitude": 2000, "velocity": 60}

    # Closure defining navigation algorithm based on sensor data
    def navigate():
        nonlocal sensor_data  # To modify the sensor_data variable from the outer scope

        # Access sensor data and perform calculations
        altitude = sensor_data["altitude"]
        velocity = sensor_data["velocity"]

        # Check if altitude is below surface level
        if altitude <= 0:
            return 0  # Descent rate is zero if already below surface

        # Example algorithm: adjust descent rate based on altitude and velocity
        if altitude > 1000:
            descent_rate = velocity - 1.5
        else:
            descent_rate = velocity - 1.0

        # Simulate updating sensor data
        sensor_data["altitude"] -= 100  # Decrease altitude
        sensor_data["velocity"] -= 5  # Decrease velocity

        return max(descent_rate, 0)  # Ensure descent rate is not negative

    return navigate


# Create a navigation algorithm closure
navigation_algorithm = create_navigation_algorithm()

# Simulated lunar descent loop
print("Starting lunar descent:")
while True:  # Continue until descent rate reaches zero
    # Get descent rate from the navigation algorithm closure
    descent_rate = navigation_algorithm()

    # Print descent rate for illustration
    print("Descent Rate:", descent_rate)

    # Break the loop when descent rate becomes zero
    if descent_rate == 0:
        break

print("Landing successful. The spacecraft has safely landed on the moon's surface.")
