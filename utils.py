import pandas as pd

def export_to_csv(leads, filename="leads.csv"):
    df = pd.DataFrame(leads)
    df.to_csv(filename, index=False)
    return filename
