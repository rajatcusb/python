# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
	return (celsius * 9/5) + 32
# Input temperature in Celsius
celsius_temperature = float(input("Enter temperature in Celsius:"))
# Convert Celsius to Fahrenheit
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
# Display the result
print("temperature in farenheit is:",fahrenheit_temperature)
