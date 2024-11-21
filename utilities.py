import os
import pandas as pd
from cognitives import determine_sentiment, determine_category
import datetime
import tempfile

gen_start =datetime.datetime.now()

def process_data(source,texts,categories):
    start = datetime.datetime.now()
    print("start: ",start)
    data = []
    for text in texts:
        platform = source
        sentiment = determine_sentiment(text)
        category = determine_category(text,categories)
        data.append([platform,text,sentiment,category])
    end = datetime.datetime.now()
    print("end: ", end)
    print(data)

    print("duration: ",end-start)
    return data

def create_excel_report(data):
    df = pd.DataFrame(data, columns=["Platform","Text", "Sentiment","Category"])
    
    df.to_excel("results.xlsx", index=False)
    print("File saved")
    with open("results.xlsx", "rb") as f:
        file_data = f.read()
    return file_data

def create_excel_report_api(results):
    temp_dir = tempfile.gettempdir()
    file_name = "results.xlsx" + gen_start
    file_path = os.path.join(temp_dir, file_name)
    df = pd.DataFrame(results)

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Report")

    # Ensure the file was saved
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Failed to create file at {file_path}")
    return file_path
