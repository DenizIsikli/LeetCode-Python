class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output = [float, float]
        output[0] = celsius + 273.15
        output[1] = (celsius * 9/5) + 32
        return output

    # Set output to a list of floats
    # Convert the temperature to Kelvin
    # Convert the temperature to Fahrenheit
    # Return the list of floats
