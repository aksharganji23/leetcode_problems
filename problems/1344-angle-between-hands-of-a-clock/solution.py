class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + (minutes * 0.5)
        minute_angle = minutes * 6
        
        # Find the absolute difference
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller angle
        return min(angle, 360 - angle)
