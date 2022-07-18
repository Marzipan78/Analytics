import pandas as pd

def file_formater(doc):
    """
    reads file into df and then saves as csv
    
    Args:
        doc (_type_): _description_
        
    Returns: csv file
    """
    df = pd.read_excel(doc)
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    
    df.to_csv(doc.replace(".xlsx", ".csv"), index=False)
    
file_formater("covid_analysis/CovidVacinations.xlsx")

