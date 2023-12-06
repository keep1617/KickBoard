#start here
class Judge:
    def __init__(self) :
        self.RGB_sensor = []
        self.GPS_val = []
        self.is_return = False

    def sensing(self, sensor_values):
        self.RGB_sensor = sensor_values

        lower = np.array([41, 26, 17])  # BGR
        upper = np.array([57, 37, 28])
        rgb123 = np.array(self.RGB_sensor) 


        if np.all(lower <= rgb123) and np.all(rgb123 <= upper):
            return True
        else:
            return False
        
    
    def location(self, gps_values) :
        #GPS 값이 웅비관 킥보드 주차장 위치에 해당하면 True를 출력
        #주차장 중앙의 위도, 경도 값을 중심으로 일정 범위 내에 있는지 확인

        self.GPS_val = gps_values

        #웅비관 킥보드 주차장 중앙의 위도, 경도
        middle_lat = 35.237052
        middle_lon = 129.077633

        #웅비관 킥보드 주차장 가장 끝의 위도, 경도
        edge_lat = 35.236781
        edge_lon = 129.077513

        #현재 위치의 위도, 경도
        lat, lon = gps_values

        #중앙에서 가장 끝을 기준으로 주차장 범위 내를 원 범위로 계산
        range = math.sqrt(abs(middle_lat-edge_lat)**2 + abs(middle_lon-edge_lon))

        #주차장 중앙에서 현재 위치까지의 거리 계산
        length = math.sqrt(abs(middle_lat - lat)**2 + abs(middle_lon - lon)**2)

        #현재 위치가 범위 내에 있다면 True를 출력
        if length <= range : 
            return True
        else :
            return False
        

bool =True
ui = UI(bool) 
ui.create_buttons()
ui.result_label.pack()

ui.tk.mainloop()

#end here
