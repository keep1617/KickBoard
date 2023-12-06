from tkinter import *
import pygame
import serial
import math
import numpy as np

#start here
class UI():

    def __init__(self,bool):
        self.tk = Tk()
       
        self.button = None
        self.button1 = None
        self.button2 = None
        self.activate = None

    def show_result(self):
        x = Arduino()
        self.rgb = []

        for i in range(0,5):

            x.get_sen()
            print(x.sen_rgb)
            self.rgb.append(x.sen_rgb)
        matrix = np.array(self.rgb, dtype = object)
       
        column_median = np.median(matrix,axis=0)

        column_median_list = column_median.tolist()

        print("각 열의 중간값 (NumPy 배열):", column_median)
        print("각 열의 중간값 (Python 리스트):", column_median_list)

            
        
        x.sen_gps
        judge = Judge()

        rgb_data = column_median_list
        gps_data = x.sen_gps
        print(x.sen_rgb)
        print(x.sen_gps)
        sensing_result = judge.sensing(rgb_data)
        location_result = judge.location(gps_data)

        self.bool = sensing_result and location_result
        print(self.bool)
               



        if self.button1 and self.button2:
            self.button1.pack_forget()
            self.button2.pack_forget()
            
        if self.bool == True:
            self.button.pack_forget()
            self.result_label.config(text=f'반납완료')
            self.play_success()
            self.button2 = Button(self.tk, text='종료', command = self.tk.destroy)
            self.button2.pack( padx=10, pady=10)
            
                
        else:
            self.button.pack_forget()
            self.result_label.config(text=f'반납실패')
            self.play_failed()
            self.button1 = Button(self.tk, text='다시 반납', command = lambda:self.show_result())
            self.button1.pack(side = 'left', padx=10, pady=10)
            self.button2 = Button(self.tk, text='종료', command = self.tk.destroy)
            self.button2.pack(side ='right' ,padx=10, pady=10)

# end here
    def create_buttons(self):
        
        self.button = Button(self.tk, text='반납시작', command = lambda:self.show_result())
        self.result_label = Label(self.tk, text="Boolean 값: None")
        self.button.pack(padx=10, pady=10)
#start here

    def activate(self):
        self.activate = True 

    def play_success(file_path='success.mp3'):
        
        pygame.init()

     
        pygame.mixer.init()
        success_sound = pygame.mixer.Sound('success.mp3')
        success_sound.play()
        
        pygame.time.delay(200)
        pygame.quit

    
    def play_failed(file_path='failed.mp3'):
        
        pygame.init()

       
        pygame.mixer.init()
        failed_sound = pygame.mixer.Sound('failed.mp3')
        failed_sound.play()
        pygame.time.delay(200)
        pygame.quit

#end here

#start here
class Arduino:
    def __init__(self, port='/dev/ttyACM0', baud_rate=115200, timeout=None):
        
        self.ser = serial.Serial(port, baud_rate, timeout=timeout) # 포트번호와 전송률 설정
        

    def get_sen(self):
        self.data = self.ser.readline().decode('utf-8').strip()  # 아두이노 보드가 시리얼모니터에 출력하는 문자열을 저장
                                                                 # 문자열은 '위도', '경도', 'R', 'G', 'B' 순서로 구성

        self.data_list = [float(value) for value in self.data.split(',') if value]  # 문자열을 ','기준으로 분할하여 list[float]로 변환

        self.GPS_read(self.data_list)  # 위도, 경도 추출
        self.color_sensor(self.data_list) # R, G, B 값 추출
        


    def GPS_read(self, list):
        
        self.sen_gps = list[0:2]  # 위도, 경도 추출


    def color_sensor(self,list):
        
        self.sen_rgb = list[2:5]  # R, G, B 값 추출
#end here



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
        range = math.sqrt(abs(middle_lat-edge_lat)**2 + abs(middle_lon-edge_lon))

        #특공관 중앙에서 현재 위치까지의 거리 계산
        length = math.sqrt(abs(middle_lat - lat)**2 + abs(middle_lon - lon)**2)

        #현재 위치가 특공관 범위 내에 있다면 True를 출력
        if length <= range : 
            return True
        else :
            return False
        
        
#start here

bool =True
ui = UI(bool) 
ui.create_buttons()
ui.result_label.pack()

ui.tk.mainloop()

#end here
