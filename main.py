import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from steganography import hide_message, reveal_message

def select_image_hide():
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.bmp")]
    )
    hide_image_entry.delete(0, tk.END)
    hide_image_entry.insert(0, path)

def hide():
    image = hide_image_entry.get()
    message = hide_text.get("1.0", tk.END).strip()
    password = hide_password_entry.get().strip()
    if not image or not message:
        messagebox.showerror("Error", "Please select image and enter message!")
        return
    if not password:
        messagebox.showerror("Error", "Please enter a password!")
        return
    output = image.rsplit(".", 1)[0] + "_hidden.png"
    try:
        hide_message(image, message, output, password)
        messagebox.showinfo("Success", f"Message hidden!\nSaved as:\n{output}")
        hide_text.delete("1.0", tk.END)
        hide_text.insert(tk.END, "***** Message Hidden! *****")
        hide_text.config(fg="#00e676")
        hide_password_entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def select_image_reveal():
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.bmp")]
    )
    reveal_image_entry.delete(0, tk.END)
    reveal_image_entry.insert(0, path)

def reveal():
    image = reveal_image_entry.get()
    password = reveal_password_entry.get().strip()
    if not image:
        messagebox.showerror("Error", "Please select an image!")
        return
    if not password:
        messagebox.showerror("Error", "Please enter the password!")
        return
    result = reveal_message(image, password)
    reveal_result.config(state=tk.NORMAL)
    reveal_result.delete("1.0", tk.END)
    if "ACCESS DENIED" in result:
        reveal_result.config(fg="#ff5555")
    else:
        reveal_result.config(fg="#00e676")
    reveal_result.insert(tk.END, result)
    reveal_result.config(state=tk.DISABLED)

def on_enter_hide(e):
    hide_btn.config(bg="#00c853")

def on_leave_hide(e):
    hide_btn.config(bg="#00e676")

def on_enter_reveal(e):
    reveal_btn.config(bg="#1565c0")

def on_leave_reveal(e):
    reveal_btn.config(bg="#1e88e5")

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("400x380")
    about_window.resizable(False, False)
    about_window.configure(bg="#0f0f1a")
    about_window.grab_set()

    tk.Label(about_window,
             text="🔐",
             font=("Arial", 35),
             bg="#0f0f1a").pack(pady=10)

    tk.Label(about_window,
             text="Steganography Tool",
             font=("Arial", 16, "bold"),
             bg="#0f0f1a",
             fg="#ffffff").pack()

    tk.Frame(about_window,
             bg="#333355",
             height=1).pack(fill="x", padx=20, pady=10)

    info_frame = tk.Frame(about_window,
                          bg="#16213e",
                          padx=20, pady=15)
    info_frame.pack(fill="x", padx=20)

    details = [
        ("📌 Purpose", "Hide & reveal secret messages\ninside images using LSB"),
        ("🛠️ Technology", "Python, Tkinter, Pillow (PIL)"),
        ("🔒 Algorithm", "LSB Steganography"),
        ("👨‍💻 Made By", "Anmol Gupta"),
        ("🎓 Institute", "Government Polytechnic"),
        ("💼 Internship", "Cybersecurity Internship"),
    ]

    for label, value in details:
        row = tk.Frame(info_frame, bg="#16213e")
        row.pack(fill="x", pady=4)
        tk.Label(row,
                 text=label,
                 font=("Arial", 9, "bold"),
                 bg="#16213e",
                 fg="#00e676",
                 width=16,
                 anchor="w").pack(side="left")
        tk.Label(row,
                 text=value,
                 font=("Arial", 9),
                 bg="#16213e",
                 fg="#cccccc",
                 anchor="w",
                 justify="left").pack(side="left")

    tk.Frame(about_window,
             bg="#333355",
             height=1).pack(fill="x", padx=20, pady=10)

    tk.Button(about_window,
              text="Close",
              command=about_window.destroy,
              bg="#333355",
              fg="white",
              font=("Arial", 10),
              relief="flat",
              padx=20,
              pady=5,
              cursor="hand2").pack(pady=5)

# Main Window
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("540x750")
root.resizable(False, False)
root.configure(bg="#0f0f1a")

# Title
title_frame = tk.Frame(root, bg="#0f0f1a")
title_frame.pack(pady=15)

tk.Label(title_frame,
         text="🔐",
         font=("Arial", 30),
         bg="#0f0f1a").pack()

tk.Label(title_frame,
         text="Steganography Tool",
         font=("Arial", 20, "bold"),
         bg="#0f0f1a",
         fg="#ffffff").pack()

tk.Label(title_frame,
         text="Hide & Reveal Secret Messages in Images",
         font=("Arial", 9),
         bg="#0f0f1a",
         fg="#888888").pack(pady=2)

tk.Frame(root, bg="#333355", height=1).pack(fill="x", padx=20, pady=5)

# Hide Frame
hide_frame = tk.LabelFrame(root,
                            text="  🔒 Hide Message  ",
                            font=("Arial", 11, "bold"),
                            bg="#16213e",
                            fg="#00e676",
                            padx=15, pady=10,
                            relief="groove",
                            bd=2)
hide_frame.pack(fill="x", padx=25, pady=8)

tk.Label(hide_frame,
         text="📁 Select Image:",
         font=("Arial", 10),
         bg="#16213e",
         fg="#cccccc").grid(row=0, column=0, sticky="w", pady=4)

hide_image_entry = tk.Entry(hide_frame,
                             width=28,
                             font=("Arial", 9),
                             bg="#0f3460",
                             fg="white",
                             insertbackground="white",
                             relief="flat",
                             bd=5)
hide_image_entry.grid(row=0, column=1, padx=8)

tk.Button(hide_frame,
          text="Browse",
          command=select_image_hide,
          bg="#333355",
          fg="white",
          font=("Arial", 9),
          relief="flat",
          padx=8).grid(row=0, column=2)

tk.Label(hide_frame,
         text="💬 Secret Message:",
         font=("Arial", 10),
         bg="#16213e",
         fg="#cccccc").grid(row=1, column=0, sticky="nw", pady=4)

hide_text = tk.Text(hide_frame,
                    height=3,
                    width=28,
                    font=("Arial", 9),
                    bg="#0f3460",
                    fg="white",
                    insertbackground="white",
                    relief="flat",
                    bd=5)
hide_text.grid(row=1, column=1, pady=4)

tk.Label(hide_frame,
         text="🔑 Password:",
         font=("Arial", 10),
         bg="#16213e",
         fg="#cccccc").grid(row=2, column=0, sticky="w", pady=4)

hide_password_entry = tk.Entry(hide_frame,
                                width=28,
                                font=("Arial", 9),
                                bg="#0f3460",
                                fg="white",
                                insertbackground="white",
                                relief="flat",
                                bd=5,
                                show="*")
hide_password_entry.grid(row=2, column=1, pady=4)

hide_btn = tk.Button(hide_frame,
                     text="🔒  Hide Message",
                     command=hide,
                     bg="#00e676",
                     fg="#000000",
                     font=("Arial", 11, "bold"),
                     relief="flat",
                     padx=20,
                     pady=8,
                     cursor="hand2")
hide_btn.grid(row=3, column=1, pady=8)
hide_btn.bind("<Enter>", on_enter_hide)
hide_btn.bind("<Leave>", on_leave_hide)

tk.Frame(root, bg="#333355", height=1).pack(fill="x", padx=20, pady=5)

# Reveal Frame
reveal_frame = tk.LabelFrame(root,
                              text="  🔓 Reveal Message  ",
                              font=("Arial", 11, "bold"),
                              bg="#16213e",
                              fg="#1e88e5",
                              padx=15, pady=10,
                              relief="groove",
                              bd=2)
reveal_frame.pack(fill="x", padx=25, pady=8)

tk.Label(reveal_frame,
         text="📁 Select Image:",
         font=("Arial", 10),
         bg="#16213e",
         fg="#cccccc").grid(row=0, column=0, sticky="w", pady=4)

reveal_image_entry = tk.Entry(reveal_frame,
                               width=28,
                               font=("Arial", 9),
                               bg="#0f3460",
                               fg="white",
                               insertbackground="white",
                               relief="flat",
                               bd=5)
reveal_image_entry.grid(row=0, column=1, padx=8)

tk.Button(reveal_frame,
          text="Browse",
          command=select_image_reveal,
          bg="#333355",
          fg="white",
          font=("Arial", 9),
          relief="flat",
          padx=8).grid(row=0, column=2)

tk.Label(reveal_frame,
         text="🔑 Password:",
         font=("Arial", 10),
         bg="#16213e",
         fg="#cccccc").grid(row=1, column=0, sticky="w", pady=4)

reveal_password_entry = tk.Entry(reveal_frame,
                                  width=28,
                                  font=("Arial", 9),
                                  bg="#0f3460",
                                  fg="white",
                                  insertbackground="white",
                                  relief="flat",
                                  bd=5,
                                  show="*")
reveal_password_entry.grid(row=1, column=1, pady=4)

reveal_btn = tk.Button(reveal_frame,
                       text="🔓  Reveal Message",
                       command=reveal,
                       bg="#1e88e5",
                       fg="#ffffff",
                       font=("Arial", 11, "bold"),
                       relief="flat",
                       padx=20,
                       pady=8,
                       cursor="hand2")
reveal_btn.grid(row=2, column=1, pady=8)
reveal_btn.bind("<Enter>", on_enter_reveal)
reveal_btn.bind("<Leave>", on_leave_reveal)

tk.Label(reveal_frame,
         text="🔍 Hidden Message:",
         font=("Arial", 10),
         bg="#16213e",
         fg="#cccccc").grid(row=3, column=0, sticky="nw", pady=4)

reveal_result = scrolledtext.ScrolledText(reveal_frame,
                                          height=3,
                                          width=28,
                                          font=("Arial", 9),
                                          bg="#0f3460",
                                          fg="#00e676",
                                          relief="flat",
                                          bd=5,
                                          state=tk.DISABLED)
reveal_result.grid(row=3, column=1, pady=4)

# About Button
about_btn = tk.Button(root,
                      text="ℹ️  About",
                      command=show_about,
                      bg="#16213e",
                      fg="#888888",
                      font=("Arial", 9),
                      relief="flat",
                      padx=10,
                      cursor="hand2")
about_btn.pack(pady=5)

# Footer
tk.Frame(root, bg="#333355", height=1).pack(fill="x", padx=20, pady=5)
tk.Label(root,
         text="Made with ❤️ | Cybersecurity Internship Project",
         font=("Arial", 8),
         bg="#0f0f1a",
         fg="#555555").pack(pady=5)

root.mainloop()