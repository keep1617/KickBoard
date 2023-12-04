

class Judge:
    def __init__(self) :
        self.RGB_sensor = []
        self.GPS_val = []
        self.is_return = False

    def sensing(self, sensor_values):
        self.RGB_sensor = sensor_values
        self.lower = [100, 0, 0] #BGR
        self.upper = [140, 255, 255]
        if self.RGB_sensor >= self.lower and \
           self.RGB_sensor <= self.upper :
            return True
        else :
            return False
    
    def location(self, gps_values) :
        self.GPS_val = gps_values

        school_lat = 35.233197
        school_lon = 129.083096

        lat, lon = gps_values
        
        if abs(school_lat - lat) <= 0.000136 and \
           abs(school_lon - lon) <= 0.000132 :
                return True
        else :
            return False



judge = Judge()

rgb_data = Arduino.b
gps_data = Arduino.a

sensing_result = judge.sensing(rgb_data)

location_result = judge.location(gps_data)


if sensing_result and location_result:
    judge.is_return = True

else:
    judge.is_return = False

print (location_result)
#print(judge.is_return)

#