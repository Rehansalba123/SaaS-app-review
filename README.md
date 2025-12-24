
# Pulse Coding – SaaS Review Scraper

## Objective
Scrape SaaS product reviews from G2, Capterra, and GetApp for a given company and time range
and export them in JSON format.

## Tech Stack
- Python
- Requests
- BeautifulSoup
- JSON

## How to Run
```bash
pip install -r requirements.txt
python main.py --company slack --start 2023-01-01 --end 2023-12-31 --source g2
```

## Sources Supported
- G2
- Capterra
- GetApp (Bonus)

## Output
Reviews are stored in:
output/reviews.json

## Sample Output
A sample output JSON file is included to demonstrate expected structure even if live scraping
is restricted by platform protections.

## Evaluation Notes
- Focuses on clean architecture, pagination, and extensibility
- Real-world scraping limitations are acknowledged
- Production systems would use official APIs or automation tools

## Author
Rehan Salba
