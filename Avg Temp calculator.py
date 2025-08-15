# Basic Data Processing Script: Average Temperature

# Sample temperature data in Celsius
temperatures = [28.5, 30.2, 27.8, 29.4, 31.0, 28.9, 30.5]

# Calculate the average
total = sum(temperatures)
count = len(temperatures)
average_temp = total / count

# Display results
print("Temperature Data:", temperatures)
print(f"Number of readings: {count}")
print(f"Average Temperature: {average_temp:.2f}°C")
