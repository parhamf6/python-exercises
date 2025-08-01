class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        x = float(celsius)
        ans = [(x + 273.1500),(x * 1.80 + 32.0000)]
        return ans
