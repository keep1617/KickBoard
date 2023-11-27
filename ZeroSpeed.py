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
    def __init__(self, camera):
        self.camera, self.previous_frame = camera, None

    def detect_zero_speed(self):
        current_frame = self.camera.frame

        if self.previous_frame is not None and np.array_equal(current_frame, self.previous_frame):
            print("ZeroSpeed")

        self.previous_frame = current_frame

if __name__ == "__main__":
    smartphone_url = 'http://172.21.128.43:8080/video'
    camera = Camera(smartphone_url)
    camera.start_camera()
    camera.sensing.color_sensing(np.array([100, 0, 0]), np.array([255, 100, 100]))
    camera.stop_camera()

    cv2.destroyAllWindows()
