import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle

class InputGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Input to Produce Application")  # Title for the window
        self.use_default_var = tk.BooleanVar()
        self.use_default_var.set(False)
        self.commands = ""
        self.url = ""

        # Set window size and position
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Apply the Clearlooks theme
        self.root.configure(bg="white")
        style = ThemedStyle(self.root)
        style.set_theme("adapta")

        # Heading Title
        heading_label = ttk.Label(self.root, text="Input to Produce Application", font=("Helvetica", 16, "bold"))
        heading_label.pack(pady=10)

        # Create a frame for command input
        self.command_frame = ttk.Frame(self.root)
        self.command_frame.pack(pady=10, padx=10)

        self.command_label = ttk.Label(self.command_frame, text="Enter commands or choose a file:")
        self.command_label.grid(row=0, column=0, padx=5, pady=5)

        self.command_entry = ttk.Entry(self.command_frame, width=50)
        self.command_entry.grid(row=1, column=0, padx=5, pady=5)

        # Create a button to browse for a file containing commands
        self.browse_button = ttk.Button(self.command_frame, text="Browse File", command=self.browse_file)
        self.browse_button.grid(row=1, column=1, padx=5, pady=5)

        # Create a frame to display commands from file
        self.file_commands_frame = ttk.Frame(self.root)
        self.file_commands_frame.pack(pady=10, padx=10)

        self.file_commands_label = ttk.Label(self.file_commands_frame, text="", font=("Helvetica", 10, "bold"))
        self.file_commands_label.pack()

        self.file_commands_text = ttk.Label(self.file_commands_frame, text="", wraplength=300)
        self.file_commands_text.pack()

        # Create a check button to toggle command entry
        self.use_default_check = ttk.Checkbutton(self.root, text="Use default commands", variable=self.use_default_var,
                                                 command=self.toggle_command_entry)
        self.use_default_check.pack(pady=10)

        # Create a frame for URL input
        self.url_frame = ttk.Frame(self.root)
        self.url_frame.pack(pady=10, padx=10)

        self.url_label = ttk.Label(self.url_frame, text="Enter Discord Webhook URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5)

        self.url_entry = ttk.Entry(self.url_frame, width=50)
        self.url_entry.grid(row=1, column=0, padx=5, pady=5)

        # Button to print values
        self.print_button = ttk.Button(self.root, text="Commit Changes!", command=self.print_values)
        self.print_button.pack(pady=10)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                contents = file.read()
                if contents:
                    self.command_entry.delete(0, tk.END)
                    self.command_entry.insert(tk.END, contents)
                    self.command_entry.config(state=tk.DISABLED)
                    self.file_commands_label.config(text="Commands from file:")
                    self.file_commands_text.config(text=contents)
                    self.use_default_var.set(False)
                else:
                    self.command_entry.config(state=tk.NORMAL)
                    self.file_commands_label.config(text="")
                    self.file_commands_text.config(text="")
                    self.use_default_var.set(True)
                self.root.update()

    def toggle_command_entry(self):
        if self.use_default_var.get():
            self.command_entry.config(state=tk.DISABLED)
            self.file_commands_label.config(text="Using default commands")
            self.file_commands_text.config(text="")
            self.browse_button.config(state=tk.DISABLED)
        else:
            self.command_entry.config(state=tk.NORMAL)
            self.file_commands_label.config(text="")
            self.file_commands_text.config(text="")
            self.browse_button.config(state=tk.NORMAL)

    def print_values(self):
        self.commands = self.command_entry.get()
        self.url = self.url_entry.get()
        if self.use_default_var.get():
            self.commands = "systeminfo,tree C:"
        #print("Commands:", self.commands)
        #print("URL:", self.url)
        self.root.destroy()  # Close the window

    def run(self):
        self.root.mainloop()

# Example usage:
if __name__ == "__main__":
    input_gui = InputGUI()
    input_gui.run()
    commands = input_gui.commands
    url = input_gui.url 
    print("Commands:", commands)
    print("URL:", url)
    
