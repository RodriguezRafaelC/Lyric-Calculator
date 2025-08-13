import tkinter as tk


TYPING_SPEED = 150
lyrics = [
    ("'Wag kang bibitaw", 4000),
    ("'Wag kang mawawala", 2700),
    ("oh aking...", 1600),
    ("dinadala...", 1000),
    ("Ang bawat...", 1900),
    ("piyesa ng", 1300),
    ("Ikawwwww...", 3000)
]

current_line_index = 0
current_char_index = 0
displaying_lyrics = False

def press_key(key):
    global displaying_lyrics
    if displaying_lyrics:
        return 
    
    if key == "=":
        start_lyrics()
    elif key == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + str(key))

def start_lyrics():
    global displaying_lyrics, current_line_index, current_char_index
    displaying_lyrics = True
    current_line_index = 0
    current_char_index = 0
    entry_var.set("")
    type_lyric()

def type_lyric():
    global current_line_index, current_char_index, displaying_lyrics

    if current_line_index < len(lyrics):
        line, pause_time = lyrics[current_line_index]
        if current_char_index < len(line):
            entry_var.set(entry_var.get() + line[current_char_index])
            current_char_index += 1
            window.after(TYPING_SPEED, type_lyric)
        else:
            
            current_line_index += 1
            current_char_index = 0
            if current_line_index < len(lyrics):
                window.after(pause_time, lambda: entry_var.set(""))
                window.after(pause_time + TYPING_SPEED, type_lyric)
            else:
                displaying_lyrics = False 
    else:
        displaying_lyrics = False


window = tk.Tk()
window.title("Calculator")
window.configure(bg="#1e1e1e")

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 20), bg="#2d2d2d", fg="white", bd=0, relief="flat", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
    ("C",5,0)
]

for (text, r, c) in buttons:
    b = tk.Button(window, text=text, font=("Arial", 16), width=5, height=2,
                  bg="#333", fg="white", relief="flat",
                  command=lambda key=text: press_key(key))
    b.grid(row=r, column=c, padx=5, pady=5)

window.mainloop()

