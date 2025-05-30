from fastapi import FastAPI, Request,Form 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from transformers import pipeline
import feedparser

def fetch_rss_headlines(url, limit=5):
    feed = feedparser.parse(url)
    return [entry['title'] for entry in feed['entries'][:limit]]

summerize = pipeline("summarization", model="facebook/bart-large-cnn")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    # Fetch headlines from different sites
    bbc = fetch_rss_headlines("http://feeds.bbci.co.uk/news/world/rss.xml")
    ekantipur = fetch_rss_headlines("https://ekantipur.com")  # Example Nepali feed
    news24= fetch_rss_headlines("https://www.news24nepal.com")
    headlines = bbc + ekantipur + news24
    joined_text = " ".join(headlines)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "headlines": headlines,
        "summary": "",
        "original": joined_text
    })
@app.post("/")
async def summarize(request: Request, text: str = Form(...)):
    bbc = fetch_rss_headlines("http://feeds.bbci.co.uk/news/world/rss.xml")
    ekantipur = fetch_rss_headlines("https://ekantipur.com")
    news24= fetch_rss_headlines("https://www.news24nepal.com")
    headlines = bbc + ekantipur + news24
    
    summary_output = summerize(text, max_length=100, min_length=30, do_sample=False)

    
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary_output[0]["summary_text"], "orginal": text,"headlines": headlines})
