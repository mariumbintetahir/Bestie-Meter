import tkinter as tk
from tkinter import messagebox

# -------------------- Data --------------------
questions = [
    "Do you like tea or coffee?",
    "night chats or day hangouts",
    "are u share everything or keep something private kindda person ",
    "loud energy or calm vibes ",
    "are u emotional or chill?"
]

answers_user1 = []
answers_user2 = []
current_q = 0
current_user = 1
user1_name = ""
user2_name = ""

# -------------------- Functions --------------------

def start_quiz():
    global user1_name, user2_name
    user1_name = entry_name1.get().strip() or "User 1"
    user2_name = entry_name2.get().strip() or "User 2"

    start_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    update_question()


def update_question():
    name = user1_name if current_user == 1 else user2_name
    label_question.config(text=f"{name}, {questions[current_q]}")


def submit_answer():
    global current_q, current_user

    ans = entry_answer.get().lower().strip()
    entry_answer.delete(0, tk.END)

    if not ans:
        return

    if current_user == 1:
        answers_user1.append(ans)
    else:
        answers_user2.append(ans)

    current_q += 1

    if current_q < len(questions):
        update_question()
    else:
        if current_user == 1:
            current_user = 2
            current_q = 0
            update_question()
        else:
            calculate_result()


def calculate_result():
    score = 0

    for i in range(len(questions)):
        if answers_user1[i] == answers_user2[i]:
            score += 1

    percentage = (score / len(questions)) * 100

    # Result window
    result_win = tk.Toplevel(root)
    result_win.title("Result")
    result_win.geometry("400x300")
    result_win.configure(bg="#fff0f0")

    tk.Label(result_win, text=f"Compatibility: {percentage:.0f}%",
             font=("Arial", 18, "bold"), bg="#fff0f6").pack(pady=20)

    if percentage < 50:
        msg = "💔 You 2 ppl are not compatible!\nChange your friend ASAP 😂"
    elif percentage >=80:

        msg = "❤️ You two are born to be friends!"
    else:
        msg = "😊 You are somewhat compatible"

    tk.Label(result_win, text=msg, font=("Arial", 12), bg="#fff0f0").pack(pady=10)


# -------------------- GUI --------------------
root = tk.Tk()
root.title("Friendship Compatibility Index")
root.geometry("500x350")
root.configure(bg="#fff8e6")

# -------- Start Frame (Name Input) --------
start_frame = tk.Frame(root, bg="#ffe6e6")
start_frame.pack(fill="both", expand=True)


tk.Label(start_frame, text="Bestie Meter",
         font=("Arial", 16, "bold"), bg="#ffe6f0").pack(pady=20)


tk.Label(start_frame, text="Enter User 1 Name:", bg="#ffe6e6").pack()
entry_name1 = tk.Entry(start_frame)
entry_name1.pack(pady=5)


tk.Label(start_frame, text="Enter User 2 Name:", bg="#ffe6fc").pack()
entry_name2 = tk.Entry(start_frame)
entry_name2.pack(pady=5)


tk.Button(start_frame, text="vibe check", bg="#4CAF50", fg="white",
          command=start_quiz).pack(pady=20)

# -------- Quiz Frame --------
quiz_frame = tk.Frame(root, bg="#ffe6fc")

label_question = tk.Label(quiz_frame, text="",
                          font=("Arial", 12), wraplength=400, bg="#ffe6fc")
label_question.pack(pady=30)

entry_answer = tk.Entry(quiz_frame, width=30)
entry_answer.pack(pady=10)

btn_submit = tk.Button(quiz_frame, text="Submit", bg="#2196F3", fg="white",
                       command=submit_answer)
btn_submit.pack(pady=10)

root.mainloop()
