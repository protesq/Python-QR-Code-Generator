import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

def qr_generate():
    data = root_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("example_qr.png")
    
    
    qr_image = Image.open("example_qr.png")
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo  

def qr():
    global root_entry, qr_label
    root = tk.Tk()
    root.geometry("900x600")
    root.title("QR Generator")
    
    frame = ttk.Frame(root)
    frame.pack(pady=20)
    
    root_label = ttk.Label(frame, text="Site adını giriniz: ")
    root_label.grid(row=0, column=0, padx=10)
    
    root_entry = ttk.Entry(frame, width=40)
    root_entry.grid(row=0, column=1, pady=10)
    
    root_button = ttk.Button(frame, text="Oluştur", command=qr_generate)
    root_button.grid(row=1, column=0, columnspan=2, pady=10)
    

    qr_label = ttk.Label(root)
    qr_label.pack(pady=10)
    
    root.mainloop()

if __name__ == '__main__':
    qr()
