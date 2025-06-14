import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Function to get the predicted price
def predict_price():
    brand = brand_var.get()
    display = float(display_var.get())
    storage = int(storage_var.get())
    processor = processor_var.get()

    user_input_df = pd.DataFrame([[brand, display, storage, processor]], columns=['brand', 'display_size', 'primary_storage_capacity', 'processor_brand'])
    user_input_encoded = encoder.transform(user_input_df[categorical_features])

    prediction = model.predict(user_input_encoded)

    predicted_price_var.set("Predicted Price of the Laptop: {:.2f}".format(prediction[0]))

# Load data
data = pd.read_csv('./laptops.csv')

X = data[['brand', 'display_size', 'primary_storage_capacity', 'processor_brand']]
y = data['Price']

categorical_features = ['brand', 'display_size', 'primary_storage_capacity', 'processor_brand']

encoder = OneHotEncoder(handle_unknown='ignore')
X_encoded = encoder.fit_transform(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# GUI setup
root = tk.Tk()
root.title("Laptop Price Predictor")

# Center the window
root.eval('tk::PlaceWindow . center')

# Colors
bg_color = "#f0f0f0"
fg_color = "#333333"
btn_bg_color = "#4caf50"
btn_fg_color = "black"

# Style
style = ttk.Style()
style.configure('TButton', background=btn_bg_color, foreground=btn_fg_color)

# Labels
label_font = ('Arial', 12)
brand_label = ttk.Label(root, text="Brand:", font=label_font)
brand_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

display_label = ttk.Label(root, text="Display Size (in inches):", font=label_font)
display_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

storage_label = ttk.Label(root, text="Storage Capacity (in GB):", font=label_font)
storage_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

processor_label = ttk.Label(root, text="Processor Type:", font=label_font)
processor_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

predicted_price_label = ttk.Label(root, text="Predicted Price:", font=label_font)
predicted_price_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")

# Entry fields
entry_font = ('Arial', 12)
brand_var = tk.StringVar()
brand_entry = ttk.Entry(root, textvariable=brand_var, font=entry_font)
brand_entry.grid(row=0, column=1, padx=5, pady=5)

display_var = tk.StringVar()
display_entry = ttk.Entry(root, textvariable=display_var, font=entry_font)
display_entry.grid(row=1, column=1, padx=5, pady=5)

storage_var = tk.StringVar()
storage_entry = ttk.Entry(root, textvariable=storage_var, font=entry_font)
storage_entry.grid(row=2, column=1, padx=5, pady=5)

processor_var = tk.StringVar()
processor_entry = ttk.Entry(root, textvariable=processor_var, font=entry_font)
processor_entry.grid(row=3, column=1, padx=5, pady=5)

predicted_price_var = tk.StringVar()
predicted_price_var.set("Predicted Price of the Laptop:")
predicted_price_display = ttk.Label(root, textvariable=predicted_price_var, font=label_font)
predicted_price_display.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Predict button
predict_button = ttk.Button(root, text="Predict Price", command=predict_price)
predict_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Set background color
root.configure(background=bg_color)

root.mainloop()
