from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from utilities import create_excel_report_api, process_data
from linkedin import scrape_linkedin
from twitter import scrape_twitter
from reddit import scrape_reddit
from fastapi.responses import FileResponse

# Initialize FastAPI app
app = FastAPI(title = "Virtual Pulse Analyzer")

# Define request schema
class AnalysisRequest(BaseModel):
    keyword: str
    platforms: List[str]
    categories: List[str]

@app.post("/generate_report/")
async def generate_daily_report(request: AnalysisRequest):
    keyword = request.keyword
    platforms = request.platforms
    categories = request.categories

    # Scrape data
    twitter_results, linkedin_results, reddit_results = [], [], []

    if "Twitter" in platforms:
        twitter_results = scrape_twitter(keyword)
    if "Linkedin" in platforms:
        linkedin_results = scrape_linkedin(keyword)
    if "Reddit" in platforms:
        reddit_results = scrape_reddit(keyword)

    # Process data
    processed_twitter_results = process_data("Twitter", twitter_results, categories)
    processed_linkedin_results = process_data("LinkedIn", linkedin_results, categories)
    processed_reddit_results = process_data("Reddit", reddit_results, categories)

    results = processed_twitter_results + processed_linkedin_results + processed_reddit_results

    # Create Excel report
    file_path = create_excel_report_api(results)

    # Return the file as a response
    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename="results.xlsx")

