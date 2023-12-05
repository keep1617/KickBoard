import math

#Arduino의 RGB센서와 GPS센서의 값을 받아 반납 조건을 충족하는지 판단하는 class
class Judge:
    def __init__(self) :
        self.RGB_sensor = []
        self.GPS_val = []
        self.is_return = False


    def sensing(self, sensor_values):
        #rgb 센서의 값이 색 범위 안(lower와 upper 사이)에 해당하면 True를 출력

        self.RGB_sensor = sensor_values

        self.lower = [100, 0, 0]   #RGB
        self.upper = [140, 255, 255]

        if self.RGB_sensor >= self.lower and \
           self.RGB_sensor <= self.upper :
            return True
        else :
            return False
    

    def location(self, gps_values) :
        #GPS 값이 특공관 위치에 해당하면 True를 출력
        #특공관 중앙의 위도, 경도 값을 중심으로 일정 범위 내에 있는지 확인

        self.GPS_val = gps_values

        #특공관 중앙의 위도, 경도
        middle_lat = 35.233280
        middle_lon = 129.082891

        #특공관 가장 끝의 위도, 경도
        edge_lat = 35.233061
        edge_lon = 129.083228

        #현재 위치의 위도, 경도
        lat, lon = gps_values
        
        #특공관 중앙에서 가장 끝을 기준으로 특공관 범위 내를 원 범위로 계산
        range = math.sqrt((middle_lat-edge_lat)**2 + (middle_lon-edge_lon))

        #특공관 중앙에서 현재 위치까지의 거리 계산
        length = math.sqrt((middle_lat - lat)**2 + (middle_lon - lon)**2)
        
        #현재 위치가 특공관 범위 내에 있다면 True를 출력
        if length <= range : 
            return True
        else :
            return False


judge = Judge()

#Arduino class에서 rgb, gps data를 받아 각각 rgb_data, gps_data에 저장
rgb_data = Arduino.b
gps_data = Arduino.a

#Arduino로부터 받은 rgb, gps값이 각각 True인지 판별
sensing_result = judge.sensing(rgb_data)
location_result = judge.location(gps_data)

#rgb, gps 모두 범위 안에 해당하면 True를 출력
if sensing_result and location_result:
    judge.is_return = True

else:
    judge.is_return = False

print(judge.is_return)

#