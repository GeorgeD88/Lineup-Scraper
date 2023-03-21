# Lineup Scraper

**Lineup Scraper** is a Python and Selenium web scraper that extracts artist information and names, including Spotify artist IDs, from music festival websites. Currently, the scraper is only configured to scrape the Florida Groves festival lineup, but the code can be easily adapted to support other festival websites.   
_For those who may not know, a lineup is the list of performers scheduled to perform at an event, such as a music festival or concert. For example, the lineup for Coachella might include popular music acts like Beyonce, The Weeknd, and Eminem._

## Dependencies

To use the scraper, you'll need to have Selenium and a compatible web driver installed on your machine. If you're not sure how to get started with Selenium, check out this [simple tutorial](https://selenium-python.readthedocs.io/installation.html).


## Usage

To use the scraper, simply run the following command in your terminal:

```bash
python scrape_fl_groves.py
```

This command will execute the Python script and scrape the Florida Groves festival lineup, saving the artists' Spotify IDs to a JSON file.

The JSON file will look something like this:

```json
{
    "artists": [
        "7BGR8y1VZAWK2oR4zD9COr",
        "5Ayl2bJtN5mdCsxZoxs9n1",
        "53eTH57OzNJCKOohjcWMoB",
        "NOT FOUND: the resolvers",
        "7olPZFkqjZyoBY6Jxase3b"
    ]
}
```

_Artists whose Spotify ID was not found will be indicated as "NOT FOUND" instead of storing their ID._


### Future Adaptation
In the future, I plan to add scripts to support other festival lineups. Currently, the script works by scraping the lineup page for the hyperlink of every artist's name. Then it goes to every scraped link (which is the artist's page on the FL Groves site), and extracts the Spotify artist ID through the Spotify embed on the page. However, this method is fairly specific to FL Groves' site, so I plan to adapt it to just scrape every artist's name from the lineup. That way, the user will only have to set the lineup link and modify the XPATH expression for that specific page.
