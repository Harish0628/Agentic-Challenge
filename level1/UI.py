import tkinter
from tkinter import scrolledtext
from pypdf import PdfReader
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
import pathlib
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(0)

#---------------------Background----------------------------
window=tkinter.Tk()
window.title("Pdf Anlyser")
window.minsize(width=600,height=600)
window.config(bg="#0b0b0b")
centre_canvas=tkinter.Canvas(width=550,height=400,bg="#101111",relief="ridge")
centre_canvas.place(x=25,y=180)
top1_canvas= tkinter.Canvas(width=550,height=35,bg="#1a1818",relief="ridge")
top1_canvas.place(x=25,y=60)
top2_canvas= tkinter.Canvas(width=550,height=50,bg="#1a1818",relief="ridge")
top2_canvas.place(x=25,y=100)


#--------------------Content----------------------------------
title=tkinter.Label( text="Pdf Analyzer", font=("Courier", 22, "bold"), fg="#8e969e", bg="#0b0b0b")
title.place(x=200,y=10)

response=tkinter.Label( text="Response: ", font=("Courier", 16, "bold"), fg="#8e969e", bg="#101111")
response.place(x=30,y=190)

prompt_Label=tkinter.Label( text="Prompt: ", font=("Courier", 14, "bold"), fg="#8e969e", bg="#161616")
prompt_Label.place(x=30,y=110)

path_Label=tkinter.Label( text="File path: ", font=("Courier", 14, "bold"), fg="#8e969e", bg="#161616")
path_Label.place(x=30,y=65)

#-------------Logic------------------------

path=tkinter.Entry(width=65,bg="#D4D4D4")
path.place(x=148,y=68)

prompt=tkinter.Entry(width=35,bg="#D4D4D4",font=2)
prompt.place(x=115,y=110)

path_var=""
response_text=""

def save_path():
    global path_var
    path_var=path.get()
    print(path_var)
    

def paste_path():
    path.insert(0,window.clipboard_get())

def save_prompt():
    global prompt_var
    prompt_var=prompt.get()
    print(prompt_var)
    response_text=get_prompt(prompt_var,path=path_var)

    put_response(response_text)

response_box = None
def put_response(text):
    """Show scrollable response in the canvas area"""
    global response_box

    if response_box:
        response_box.destroy()

    response_box = scrolledtext.ScrolledText(
        window,
        wrap="word",      
        width=75,
        height=22,
        font=("Arial", 10, "bold"),
        fg="#ffffff",
        bg="#101111",
        relief="flat",
        insertbackground="white"  
    )
    response_box.place(x=30, y=218)
    response_box.insert("1.0", text)
    response_box.configure(state="disabled")  


save_path_button=tkinter.Button(text="✔",width=2,height=1,font=("Courier", 10, "bold") ,
                                command=save_path,fg="#008000",bg= "#161616")
save_path_button.place(x=548,y=65)

paste_path_button=tkinter.Button(text="paste",width=5,height=1,font=("Courier", 10, "bold") ,
                                 command=paste_path,fg="#008000",bg= "#161616")
paste_path_button.place(x=495,y=65)

save_prompt_button=tkinter.Button(text="✔",width=2,height=1,font=("Courier", 10, "bold") ,
                                  command=save_prompt,fg="#008000",bg= "#161616")
save_prompt_button.place(x=548,y=115)

#--------------------------Connecting---------------------

prompt_var=""

def get_prompt(prompt_v,path):
    client = genai.Client()
    prompt = prompt_v
    filepath = pathlib.Path(path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=filepath.read_bytes(),
                mime_type="application/pdf",
            ),
            prompt,
        ],
        
    )
    print(response.text)
    return response.text


window.mainloop()