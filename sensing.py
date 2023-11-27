# import cv2
# import numpy as np
# import threading
# import time

# class Camera:
#     def __init__(self, url):
#         self.url = url
#         self.cap = cv2.VideoCapture(url)
#         self.frame = None
#         self.running = False
#         self.thread = None
#         self.sensing = Sensing(self)

#     def start_camera(self):
#         if not self.running:
#             self.thread = threading.Thread(target=self._run_camera)
#             self.thread.start()

#     def stop_camera(self):
#         self.running = False
#         self.thread.join()
#         self.cap.release()

#     def _run_camera(self):
#         self.running = True
#         while self.running:
#             ret, frame = self.cap.read()
#             if ret:
#                 self.frame = frame
#             time.sleep(0.03)  # Adjust sleep time based on the camera frame rate

# class Sensing:
#     def __init__(self, camera):
#         self.camera = camera
#         self.is_line = False

#     def color_sensing(self, color_lower, color_upper):
#         frame = self.camera.frame
#         if frame is not None:
#             mask = cv2.inRange(frame, color_lower, color_upper)
#             result = cv2.bitwise_and(frame, frame, mask=mask)
#             self.is_line = np.sum(mask > 0) > 150000
#             return result
#         return None

#     def on_cam(self):
#         color_lower = np.array([0, 0, 0])
#         color_upper = np.array([100, 100, 100])
        
        
#         while True:
#             result = self.color_sensing(color_lower, color_upper)
            
#             if result is not None:
#                 cv2.imshow('Color Sensing', self.camera.frame)
            
#             if self.is_line:
#                 print("Line detected!")
#                 # to ui
#             else:
#                 print("No line detected.")
            
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

# # 예제로 빨간색 감지
# if __name__ == "__main__":
#     # 스마트폰의 IP 주소 및 포트 번호 입력
#     smartphone_url = 'http://172.30.1.83:8080/video'

#     camera = Camera(smartphone_url)
#     camera.start_camera()
#     camera.sensing.on_cam()
#     camera.stop_camera()

#     cv2.destroyAllWindows()




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
        
        while True:
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
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break




# 예제로 빨간색 감지
if __name__ == "__main__":
    # 스마트폰의 IP 주소 및 포트 번호 입력
    smartphone_url = 'http://192.168.0.168:8080/video'

    camera = Camera(smartphone_url)
    camera.start_camera()
    camera.sensing.on_cam()
    camera.stop_camera()

    cv2.destroyAllWindows()












































































































































# import cv2
# import numpy as np
# import tkinter as tk
# from tkinter import ttk

# class sensing():
#     def __init__(self, frame):
#         self.frame = frame

#     def line_sensing(self):
        
# class camera():
#     def __init__(self,url):
#         self.url = url

#     def on_cam(self):
#         self.cap = cv2.VideoCapture(self.url)

#         while True:
#             ret, frame = self.cap.read()
#             sensing(frame)



# # 파란색이 일정 이상 감지되면 '성공' 문구를 화면에 표시
#         if blue_pixel_count > 250000:
#             cv2.putText(frame, 'success', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#             # signal to interface?


# def turn_cam():
#     # 스마트폰의 IP 주소 및 포트 번호 입력
#     url = 'http://172.22.43.163:8080/video'

#     cap = cv2.VideoCapture(url)

#     while True:
#     # 프레임 읽기
#         ret, frame = cap.read()

#         lower_blue = np.array([0, 0, 0])
#         upper_blue = np.array([150, 150, 150])

#         mask = cv2.inRange(frame, lower_blue, upper_blue)
#         blue_detected = cv2.bitwise_and(frame, frame, mask=mask)

#         blue_pixel_count = np.sum(mask > 0)

#     # 파란색이 일정 이상 감지되면 '성공' 문구를 화면에 표시
#         if blue_pixel_count > 250000:
#             cv2.putText(frame, 'success', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
            
#             # signal to interface?

#     # 화면에 표시
#         cv2.imshow('Smartphone Camera', frame)

#     # 'q' 키를 누르면 종료
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# root = tk.Tk()
# root.title("NOHS COFFEE")

# # 라벨 생성
# label = ttk.Label(root, text="DRIVING", font =("Helvetika",50))
# label.pack(pady=10)

# style = ttk.Style()
# button_font = ("Helvetika",30)
# style.configure("TButton",font=button_font)

# # 버튼 생성
# button = ttk.Button(root, text="RETURN", command=turn_cam, style='TButton')
# button.pack(pady=10)

# # 윈도우 실행
# root.mainloop()









































































# import cv2
# import numpy as np
# import tkinter as tk
# from tkinter import ttk

# class Sensing:
#     def __init__(self, url):
#         self.cap = cv2.VideoCapture(url)

#     def blue_detection(self, frame):
#         lower_blue = np.array([0, 0, 0])
#         upper_blue = np.array([150, 150, 150])

#         mask = cv2.inRange(frame, lower_blue, upper_blue)
#         blue_detected = cv2.bitwise_and(frame, frame, mask=mask)

#         blue_pixel_count = np.sum(mask > 0)
#         return blue_pixel_count > 250000

#     def process_frame(self):
#         ret, frame = self.cap.read()
#         return frame

#     def release_camera(self):
#         self.cap.release()

# class NOHSCoffeeApp:
#     def __init__(self, root, sensing):
#         self.root = root
#         self.root.title("NOHS COFFEE")

#         self.label = ttk.Label(root, text="DRIVING", font=("Helvetica", 50))
#         self.label.pack(pady=10)

#         style = ttk.Style()
#         button_font = ("Helvetica", 30)
#         style.configure("TButton", font=button_font)

#         self.sensing = sensing

#         # 버튼 생성
#         self.button = ttk.Button(root, text="RETURN", command=self.turn_cam, style='TButton')
#         self.button.pack(pady=10)

#         self.detection_result = tk.StringVar()
#         self.detection_result.set("Detection: False")
#         self.result_label = ttk.Label(root, textvariable=self.detection_result, font=("Helvetica", 20))
#         self.result_label.pack(pady=10)

#     def turn_cam(self):
#         frame = self.sensing.process_frame()
#         detected = self.sensing.blue_detection(frame)
#         self.show_frame(frame)
#         self.update_detection_result(detected)

#     def show_frame(self, frame):
#         cv2.imshow('Smartphone Camera', frame)

#     def update_detection_result(self, detected):
#         result_text = "Detection: True" if detected else "Detection: False"
#         self.detection_result.set(result_text)

#     def run(self):
#         self.root.mainloop()

#     def cleanup(self):
#         self.sensing.release_camera()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     # 스마트폰의 IP 주소 및 포트 번호 입력
#     smartphone_url = 'http://172.30.1.83:8080/video'

#     sensing_instance = Sensing(smartphone_url)

#     root = tk.Tk()
#     app = NOHSCoffeeApp(root, sensing_instance)
#     app.run()
#     app.cleanup()
