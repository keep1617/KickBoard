from tkinter import *
import subprocess
import random
import cv2
import numpy as np
import threading
import time

class Camera:
    def __init__(self, url):
        self.url = url
        self.cap = cv2.VideoCapture(url)
        self.frame = None
        self.prev_frame = None  # 이전 프레임 저장
        self.running = False
        self.thread = None
        self.sensing = Sensing(self)

    def start_camera(self):
        if not self.running:
            self.thread = threading.Thread(target=self._run_camera)
            self.thread.start()

    def stop_camera(self):
        self.running = False
        self.thread.join()
        self.cap.release()

    def _run_camera(self):
        self.running = True
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.prev_frame = self.frame
                self.frame = frame
            time.sleep(0.01)  # Adjust sleep time based on the camera frame rate

class Sensing:
    def __init__(self, camera):
        self.camera = camera
        self.is_line = False
        self.is_stopped = False  # 정지 여부 추가

    def color_sensing(self, color_lower, color_upper):
        frame = self.camera.frame
        if frame is not None:
            mask = cv2.inRange(frame, color_lower, color_upper)
            result = cv2.bitwise_and(frame, frame, mask=mask)
            self.is_line = np.sum(mask > 0) > 250000  # Adjust the threshold as needed
            return result
        return None

    def check_movement(self):
        if self.camera.prev_frame is not None and self.camera.frame is not None:
            diff = cv2.absdiff(self.camera.prev_frame, self.camera.frame)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 1:  # Adjust the threshold as needed
                    self.is_line = False
                    self.is_stopped = False
                    return
            self.is_line = True
            self.is_stopped = True
    # def check_stopped(self):
    #     if self.camera.prev_frame is not None and self.camera.frame is not None:
    #         diff = cv2.absdiff(self.camera.prev_frame, self.camera.frame)
    #         gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #         _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    #         contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #         for contour in contours:
    #             if cv2.contourArea(contour) > 1000:  # Adjust the threshold as needed
    #                 self.is_stopped = False
    #                 return
    #         self.is_stopped = True

    def on_cam(self):
        color_lower = np.array([0, 0, 100])
        color_upper = np.array([100, 100, 255])
        
        start_time = time.time()
        print(start_time)
        while True:  #20초 안에 반납 못하면 끝
            result = self.color_sensing(color_lower, color_upper)
            self.check_movement()  # 정지 여부 확인 추가
            
            if result is not None:
                cv2.imshow('Color Sensing', self.camera.frame)
            
            # if self.is_line:
            #     print("Line detected!")
            # else:
            #     print("No line detected.")
            
            if self.is_stopped:
                print("Stopped!")
            else:
                print("Not stopped.")
            if self.is_line and self.is_stopped:
                return True
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= 20:
                return "Try Again bro"
            

            





def event():
    smartphone_url = 'http://192.168.0.168:8080/video'

    camera = Camera(smartphone_url)
    camera.start_camera()
    boolean_value = True
    camera.sensing.on_cam()
    camera.stop_camera()
    if boolean_value == True:
        result_label.config(text=f'반납완료')
    if boolean_value == "Try Again bro":
        result_label.config(text=f'20초가 지났어요 다시 반납하세요')
    

    cv2.destroyAllWindows()
        


# 예제로 빨간색 감지
if __name__ == "__main__":
    # 스마트폰의 IP 주소 및 포트 번호 입력
    

    tk = Tk()

    button = Button(tk,text = '반납시작', command = event)  
    result_label = Label(tk, text='Boolean 값: None')

    button.pack( padx = 10, pady = 10)
    result_label.pack()


    tk.mainloop()


