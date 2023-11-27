import cv2
import numpy as np
import threading
import time

class Camera:
    def __init__(self, url):
        self.url, self.cap, self.frame, self.running, self.thread = url, cv2.VideoCapture(url), None, False, None
        self.sensing = Sensing(self)
        self.zero_speed_detector = ZeroSpeedDetection(self)

    def start_camera(self):
        if not self.running:
            self.thread = threading.Thread(target=self._run_camera)
            self.thread.start()

    def stop_camera(self):
        self.running, self.thread = False, None
        self.cap.release()

    def _run_camera(self):
        self.running = True
        while self.running:
            ret, self.frame = self.cap.read()
            if ret:
                self.zero_speed_detector.detect_zero_speed()
            time.sleep(0.01)

class Sensing:
    def __init__(self, camera):
        self.camera, self.is_blue, self.parking_message_displayed = camera, False, False

    def color_sensing(self, color_lower, color_upper):
        while True:
            frame = self.camera.frame
            if frame is not None:
                mask = cv2.inRange(frame, color_lower, color_upper)
                result = cv2.bitwise_and(frame, frame, mask=mask)
                self.is_blue = np.sum(mask > 0) > 150000

                if result is not None:
                    cv2.imshow('Color Sensing', self.camera.frame)

                if self.is_blue != self.parking_message_displayed:
                    message = "주차 구역입니다" if self.is_blue else "주차 구역이 아닙니다"
                    print(message)
                    self.parking_message_displayed = self.is_blue

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.01) 

class ZeroSpeedDetection:
    def __init__(self, camera, mse_threshold=100):# 프레임의 차이 감지의 민감도라고 볼 수 있음
        self.camera, self.previous_frame = camera, None
        self.mse_threshold = mse_threshold

    def calculate_mse(self, frame1, frame2):
        return np.sum((frame1.astype("float") - frame2.astype("float")) ** 2) / float(frame1.shape[0] * frame1.shape[1])

    def detect_zero_speed(self):
        current_frame = self.camera.frame

        if self.previous_frame is not None:
            mse = self.calculate_mse(current_frame, self.previous_frame)
            if mse < self.mse_threshold:
                print("ZeroSpeed")

        self.previous_frame = current_frame


if __name__ == "__main__":
    smartphone_url = 'http://192.168.0.2:8080/video'
    camera = Camera(smartphone_url)
    camera.start_camera()
    camera.sensing.color_sensing(np.array([100, 0, 0]), np.array([255, 100, 100])) # 감지할 색을 바꾸고 싶다면 안쪽의 숫자를 바꿔주면됨.
    camera.stop_camera()

    cv2.destroyAllWindows()

