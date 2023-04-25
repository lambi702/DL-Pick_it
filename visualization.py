import tkinter as tk
from PIL import Image, ImageTk
import pickle

# Define the function to update the image
data = pickle.load(open("data\original\dataset_3d_vnir_xrt.pkl", "rb"))

def update_image():
    # Get the selected number and layer from the buttons
    number = int(number_var.get())
    layer = int(layer_var.get())

    # Load the image corresponding to the selected number and layer
    image = data["data_cube"][number][layer]


# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Create the number button
number_var = tk.StringVar()
number_var.set("0")
number_btn = tk.OptionMenu(root, number_var, "0", "1",
                           "2", "3", "4", "5", "6", "7", "8", "9")
number_btn.pack()

# Create the layer button
layer_var = tk.StringVar()
layer_var.set("0")
layer_btn = tk.OptionMenu(root, layer_var, "0", "1",
                          "2", "3", "4", "5", "6", "7", "8", "9")
layer_btn.pack()

# Create the update button
update_btn = tk.Button(root, text="Update", command=update_image)
update_btn.pack()

# Start the main event loop
root.mainloop()
