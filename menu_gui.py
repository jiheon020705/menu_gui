from tkinter import *
import random
from PIL import ImageTk,Image

menulist = ['짜장면','짬뽕','탕수육','라면','국밥']

#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자

# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
label = Label(tk,text='AI 가 추천해주는 메뉴는 ? ') 
# 3. 레이블 배치 실행
label.pack()

# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
def event():
    menu = random.choice(menulist)
    button['text'] = menu
    
 
button = Button(tk,text='추천 메뉴.',command=event)
#button2 = Button(tk,text='버튼2 입니다.')
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
#button2.pack(side=LEFT, padx=10, pady= 10)

# 4. 메인루프 실행
tk.mainloop()