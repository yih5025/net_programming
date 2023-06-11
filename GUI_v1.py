import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

url = "http://1.228.201.87:8010"

root = tk.Tk()
event_id = ""
numbers = [1,2,3,4,5,5,34,75]
data = {
    'warning': '',
    'room': 0
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

row = ""


class MyTableWidget(ttk.Treeview):
    # 주어진 숫자들
    global numbers

    def __init__(self, master, rows, cols):
        super().__init__(master, columns=("", "", ""), show="headings")
        self.initUI()
        self.bind('<ButtonRelease-1>', self.cell_was_clicked)
        self.heading("#1", text="호실")
        self.heading("#2", text="소리")
        self.heading("#3", text="경고")
        self.insert("", 0, values=["1호실", "0", "0"])
        self.insert("", 1, values=["2호실", "0", "0"])
        self.column("#1", anchor="center")
        self.column("#2", anchor="center")
        self.column("#3", anchor="center")

        # self.pack(fill=tk.BOTH, expand=True)
        self.place(relx=0.5, rely=0.5, anchor='n')

        # 열 높이 변경하기
        s = ttk.Style()
        s.theme_use('clam')
        # Add the row height
        s.configure('Treeview', rowheight=80)

    def initUI(self):
        self.pack(padx=0, pady=0)
        print("testing")
        # B70404
        # POST 요청을 보낼 데이터
        
        response = requests.post(url, data=json.dumps(data), headers=headers)
        # response = requests.post(url, json=data)
        data["warning"] = ""
        ###################################################################################################
        # print(response_data)
        try:
            response_data = response.json()
        except ValueError:
            # JSONDecodeError 예외 처리
            print("서버 응답 데이터를 JSON으로 디코딩할 수 없습니다.")
            return
        content = response_data['sound_102']
        if self.get_children():
            item_id = self.get_children()[0]
            new_values = ["1호실", content, 0]
            self.item(item_id, values=new_values)
        ###################################################################################################
        global event_id
        event_id = self.after(1000, self.initUI)  # 1000ms마다 업데이트한다

        # response 받은 후에 처리
        
        self.process_response(response_data)

    def process_response(self, response_data):
        # response를 처리하는 로직을 이곳에 작성
        # 예시로 values 값을 업데이트하고 출력
        if self.get_children():
            item_id = self.get_children()[0]
            content = response_data['sound_102']
            new_values = ["1호실", content, 0]
            self.item(item_id, values=new_values)

    def cell_was_clicked(self, event):  # 셀이 클릭됐을때
        global row
        row = self.focus()
        row = row[len(row) - 1]

    def show_custom_message(self):
        messagebox.showinfo("메시지", "버튼 클릭")
        self.on_confirmation()

    def on_confirmation(self):
        print("확인 버튼이 클릭되었습니다.")


def send(param):  # 호실의 값을 서버에 보낸다
    # send 함수의 로직을 여기에 추가
    # POST 요청을 보낼 데이터
    # response = requests.post(url, data=json.dumps(data), headers=headers)
    data["warning"] = ""
    data["warning"] = param
    print("보냈다")


def sendWarning():
    '''# POST 요청을 보낼 데이터
    data = {
    'waring' : '1'
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # response = requests.post(url, data=json.dumps(data), headers=headers)
    response = requests.post(url, json=data)'''

    send(row)
    ################################################################################################################################################
    # 그래프 값을 갱신할 때 사용할 numbers 리스트 초기화
    global numbers
    
    # 그래프 만들기
    create_graph_window()
    ################################################################################################################################################


def create_graph_window():
    # 새로운 창 생성
    graph_window = tk.Toplevel(root)
    graph_window.title("Graph Window")
    graph_window.attributes("-topmost", True)  # Always on top

    # 그래프를 표시할 프레임 생성
    frame = tk.Frame(graph_window)
    frame.pack()

    # Matplotlib Figure 객체 생성
    figure = Figure(figsize=(6, 4), dpi=100)
    subplot = figure.add_subplot(111)

    # 값 추가하기
    x = range(len(numbers))
    y = [num for num in numbers]  # 최대 기준인 200으로 나눠서 파형을 만듦

    # 그래프 그리기
    subplot.plot(x, y)
    subplot.set_xlabel('X')
    subplot.set_ylabel('Y')
    subplot.set_title('Waveform')

    # 그래프를 Tkinter 프레임에 넣기
    canvas = FigureCanvasTkAgg(figure, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


root.attributes('-fullscreen', True)
root.title("My Table Widget")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tableWidget = MyTableWidget(frame, 2, 3)
tableWidget.pack(fill=tk.BOTH, expand=True)

# 하단 버튼
btn_center = ctk.CTkButton(frame, text="경고 주기", height=40, width=3, command=sendWarning)
btn_center.pack(side="bottom", padx=0, pady=0)

root.mainloop()
