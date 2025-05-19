import tkinter as tk
from tkinter import ttk

DEFAULT_COLORS = {
    "#FF0000": "Red",
    "#00FF00": "Green",
    "#0000FF": "Blue",
    "#FFFF00": "Yellow",
    "#FF00FF": "Magenta",
    "#00FFFF": "Cyan",
    "#000000": "Black",
    "#FFFFFF": "White",
}

class Model:
    def __init__(self, colors):
        self.colors = colors

    def get_colors(self):
        return self.colors

    def get_color_name(self, hex_code):
        return self.colors.get(hex_code, "Unknown Color")

class ButtonColor(tk.Button):
    def __init__(self, master, color_hex, color_name, command, **kwargs):
        super().__init__(master, bg=color_hex, command=command, **kwargs)
        self.color_hex = color_hex
        self.color_name = color_name
        # Make button visible even if color is dark/light by setting text color
        # Simple contrast check (luminance)
        r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        text_color = "black" if luminance > 0.5 else "white"
        self.config(activebackground=color_hex, fg=text_color, activeforeground=text_color, width=3, relief=tk.RAISED)

    def show_color(self, label_widget, entry_widget):
        label_widget.config(text=f"Color: {self.color_name}")
        entry_widget.config(state=tk.NORMAL) # Allow editing to change color and text
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, self.color_hex)
        if isinstance(entry_widget, tk.Entry): # Check if it's a tk.Entry
            entry_widget.config(fg=self.color_hex)
        entry_widget.config(state='readonly') # Set back to readonly

class CustomCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="white", **kwargs)
        self.drawing_color = "#000000"  # Default to black
        self.last_x = None
        self.last_y = None
        self.bind("<ButtonPress-1>", self.start_paint)
        self.bind("<B1-Motion>", self.paint)
        self.bind("<ButtonRelease-1>", self.reset_last_pos)

    def set_drawing_color(self, color_hex):
        self.drawing_color = color_hex

    def start_paint(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def paint(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.create_line(self.last_x, self.last_y, event.x, event.y,
                               fill=self.drawing_color, width=2, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x = event.x
            self.last_y = event.y

    def reset_last_pos(self, event):
        self.last_x = None
        self.last_y = None

class View:
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.controller = None

        # Main frames
        self.controls_frame = ttk.Frame(master, padding="10")
        self.controls_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas_frame = ttk.Frame(master, padding="10")
        self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Color display widgets
        self.color_info_frame = ttk.LabelFrame(self.controls_frame, text="Selected Color", padding="10")
        self.color_info_frame.pack(pady=10, fill=tk.X)

        self.color_label = ttk.Label(self.color_info_frame, text="Color: None")
        self.color_label.pack(pady=5)

        self.color_entry = tk.Entry(self.color_info_frame, width=10, justify='center') # Changed ttk.Entry to tk.Entry
        self.color_entry.pack(pady=5)
        self.color_entry.insert(0, "#000000")
        self.color_entry.config(state='readonly', fg="#000000")

        # Buttons frame
        self.buttons_frame = ttk.LabelFrame(self.controls_frame, text="Color Palette", padding="10")
        self.buttons_frame.pack(pady=10, fill=tk.X)

        # Canvas for drawing
        self.canvas = CustomCanvas(self.canvas_frame, width=400, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.set_drawing_color("#000000") # Initial drawing color

    def set_controller(self, controller):
        self.controller = controller

    def create_buttons(self, colors_dict):
        # Clear existing buttons if any (for potential future dynamic updates)
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        row, col = 0, 0
        max_cols = 4 # Adjust as needed
        for color_hex, color_name in colors_dict.items():
            button = ButtonColor(self.buttons_frame, color_hex, color_name,
                                 # Pass the button instance itself to the handler
                                 command=lambda b=None, bh=color_hex, bn=color_name: self.controller.handle_button_click(bh, bn))
            # Need to capture button instance for show_color, so we create a new lambda
            # The diagram shows ButtonColor instance passed to handle_button_click, let's adjust controller
            # For now, let's make the button itself responsible for its data for the handler
            button.config(command=lambda b=button: self.controller.handle_button_click(b))
            button.grid(row=row, column=col, padx=2, pady=2, sticky="ew")
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        # Configure columns to expand equally
        for i in range(max_cols):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

    def update_color_display(self, button_widget: ButtonColor):
        button_widget.show_color(self.color_label, self.color_entry)

    def set_drawing_color(self, color_hex):
        self.canvas.set_drawing_color(color_hex)

    def mainloop(self):
        self.master.mainloop()

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_button_click(self, button_widget: ButtonColor):
        # button_widget is an instance of ButtonColor
        self.view.update_color_display(button_widget)
        self.view.set_drawing_color(button_widget.color_hex)

    def start(self):
        colors = self.model.get_colors()
        self.view.create_buttons(colors)
        # Set initial color display based on the first color or black
        first_color_hex = next(iter(colors), "#000000")
        first_color_name = self.model.get_color_name(first_color_hex)
        
        self.view.color_label.config(text=f"Color: {first_color_name}")
        self.view.color_entry.config(state=tk.NORMAL) # Allow editing
        self.view.color_entry.delete(0, tk.END)
        self.view.color_entry.insert(0, first_color_hex)
        if isinstance(self.view.color_entry, tk.Entry):
             self.view.color_entry.config(fg=first_color_hex)
        self.view.color_entry.config(state='readonly')
        self.view.set_drawing_color(first_color_hex)

class App:
    def __init__(self, master):
        self.master = master
        self.model = Model(DEFAULT_COLORS)
        self.view = View(master, "Rainbow MVC App")
        self.controller = Controller(self.model, self.view)
        self.view.set_controller(self.controller)
        self.controller.start() # Initialize buttons and default color

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()