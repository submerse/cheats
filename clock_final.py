import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
import os

class TimeDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("clocky tick tack <3")
        self.geometry("400x200")
        
        # Load the background image
        self.bg_image_path = self.get_image_path("background3.png")
        self.bg_image = Image.open(self.bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self, width=self.bg_photo.width(), height=self.bg_photo.height())
        self.canvas.pack(fill="both", expand=True)
        
        # Add the background image to the canvas
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Create a label to display time, placed on top of the background image
        self.time_label = tk.Label(self, font=("Helvetica", 24), bg="pink", fg="black")
        self.time_label_id = self.canvas.create_window(self.bg_photo.width()//2, self.bg_photo.height()//2, window=self.time_label)
        
        # Update the time every second
        self.update_time()
        
        # Make the window adjustable
        self.bind("<Configure>", self.on_resize)
        
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.after(1000, self.update_time)  # Schedule the next update after 1000ms (1 second)
    
    def on_resize(self, event):
        # Update the canvas size
        self.canvas.config(width=event.width, height=event.height)
        self.canvas.coords(self.bg_image_id, 0, 0)
        # Reposition the time label to the center
        self.canvas.coords(self.time_label_id, event.width//2, event.height//2)
    
    def get_image_path(self, filename):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, filename)

if __name__ == "__main__":
    app = TimeDisplayApp()
    app.mainloop()