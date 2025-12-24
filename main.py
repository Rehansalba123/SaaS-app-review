
import argparse
from datetime import datetime
from scrapers.g2_scraper import scrape_g2
from scrapers.capterra_scraper import scrape_capterra
from scrapers.getapp_scraper import scrape_getapp
from utils.json_utils import save_to_json

def main():
    parser = argparse.ArgumentParser(description="SaaS Review Scraper")
    parser.add_argument("--company", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--source", required=True, choices=["g2", "capterra", "getapp"])
    args = parser.parse_args()

    start = datetime.strptime(args.start, "%Y-%m-%d").date()
    end = datetime.strptime(args.end, "%Y-%m-%d").date()

    if start > end:
        raise ValueError("Start date must be before end date")

    if args.source == "g2":
        data = scrape_g2(args.company, start, end)
    elif args.source == "capterra":
        data = scrape_capterra(args.company, start, end)
    else:
        data = scrape_getapp(args.company, start, end)

    save_to_json(data)
    print(f"Scraped {len(data)} reviews")

if __name__ == "__main__":
    main()
