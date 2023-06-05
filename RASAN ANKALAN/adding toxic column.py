import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# Load the dataset
df = pd.read_csv('D:\\My Programming\\tox21trainingdata.sdf\\output.csv')

# Define the toxicity model
def toxicity_score(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Descriptors.MolLogP(mol)

# Calculate the toxicity score and add it as a new column
df['toxicity_score'] = df['SMILES'].apply(toxicity_score)

# Save the updated dataset to a new CSV file
df.to_csv('your_updated_dataset.csv', index=False)


