from tkinter import *
import random
import pygame
import time



class UI():

    def __init__(self,bool):
        self.tk = Tk()
       
        self.button = None
        self.button1 = None
        self.button2 = None
        self.activate = None

    def show_result(self):##인자는 Judge class 의 is_return 함수로 받는다
                        #self.bool = bool
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

                

    def create_buttons(self):
        
        self.button = Button(self.tk, text='반납시작', command = lambda:ui.show_result())
        self.result_label = Label(self.tk, text="Boolean 값: None")
        self.button.pack(padx=10, pady=10)


    def activate(self):
        self.activate = True ## Arduino Activate  변수

    def play_success(file_path='success.mp3'):
        # Pygame 초기화
        pygame.init()

        # 믹서 초기화
        pygame.mixer.init()
        success_sound = pygame.mixer.Sound('success.mp3')
        success_sound.play()
        
        pygame.time.delay(200)
        pygame.quit

    
    def play_failed(file_path='failed.mp3'):
        # Pygame 초기화
        pygame.init()

        # 믹서 초기화
        pygame.mixer.init()
        failed_sound = pygame.mixer.Sound('failed.mp3')
        failed_sound.play()
        pygame.time.delay(200)
        pygame.quit

bool =True
ui = UI(bool) #bool 값 Judge 에서 받아오기
ui.create_buttons()
ui.result_label.pack()

ui.tk.mainloop()

#
