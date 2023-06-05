import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd
# Load the saved model
filename = ("D:\\My Programming\\tox21trainingdata.sdf\\xgboost3_model.pkl")
loaded_model = pickle.load(open(filename, 'rb'))

# Print the loaded model
print(loaded_model)

# Print the loaded model
print(loaded_model)
window = tk.Tk()
window.title("RASAN ANKALAN")
window.geometry("400x300")
window.configure(bg='light blue')
label_molweight = tk.Label(window, text="Molecular Weight:", fg="blue")
entry_molweight = tk.Entry(window)

label_numatoms = tk.Label(window, text="Number of Atoms:", fg="green")
entry_numatoms = tk.Entry(window)

label_numheavyatoms = tk.Label(window, text="Number of Heavy Atoms:", fg="purple")
entry_numheavyatoms = tk.Entry(window)

label_numrotatablebonds = tk.Label(window, text="Number of Rotatable Bonds:", fg="red")
entry_numrotatablebonds = tk.Entry(window)

def predict_toxicity():
    # Get the user input values
    molweight = float(entry_molweight.get())
    numatoms = int(entry_numatoms.get())
    numheavyatoms = int(entry_numheavyatoms.get())
    numrotatablebonds = int(entry_numrotatablebonds.get())

    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'MolWeight': [molweight],
        'NumAtoms': [numatoms],
        'NumHeavyAtoms': [numheavyatoms],
        'NumRotatableBonds': [numrotatablebonds]
    })

    # Make the prediction using the loaded model
    prediction =loaded_model.predict(input_data)

    # Show the prediction in a message box
    messagebox.showinfo("Toxicity Prediction", f"The predicted toxicity score is: {prediction[0]}")
button_predict = tk.Button(window, text="Predict", command=predict_toxicity)
label_molweight.grid(row=0, column=0)
entry_molweight.grid(row=0, column=1)
label_numatoms.grid(row=1, column=0)
entry_numatoms.grid(row=1, column=1)
label_numheavyatoms.grid(row=2, column=0)
entry_numheavyatoms.grid(row=2, column=1)
label_numrotatablebonds.grid(row=3, column=0)
entry_numrotatablebonds.grid(row=3, column=1)
button_predict.grid(row=4, column=0, columnspan=2)
window.mainloop()


