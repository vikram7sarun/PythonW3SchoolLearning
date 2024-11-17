from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union
from scraper import scrape_active_tab_with_playwright

app = FastAPI()


class ScrapeElement(BaseModel):
    id: Union[str, None]
    name: Union[str, None]
    class_: Union[str, None]  # Renamed `class` to `class_` to avoid conflict with Python keyword
    tag: str
    xpath: str


class ScrapeResponse(BaseModel):
    url: str
    elements: List[ScrapeElement]  # List of ScrapeElement models


@app.get("/scrape-active-functional/", response_model=ScrapeResponse)
def scrape_active_functional_elements():
    """
    API endpoint to scrape functional elements using Playwright and return their selectors.
    """
    try:
        data = scrape_active_tab_with_playwright()

        # Format the response to align with the model
        elements = []
        for el in data["elements"]:
            elements.append({
                "id": el.get("id"),
                "name": el.get("name"),
                "class_": " ".join(el.get("class", [])),  # Convert class list to space-separated string
                "tag": el.get("tag"),
                "xpath": el.get("xpath"),
            })

        return {
            "url": data["url"],
            "elements": elements
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Scraping failed: {str(e)}")
