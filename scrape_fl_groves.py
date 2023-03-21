# main scraper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# other imports
from selenium.webdriver.common.by import By  # finding elements
import json  # exporting data


# initialize selenium driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def scrape_lineup() -> list[str]:
    """ Scrapes the lineup page and returns a list of all the artist urls. """

    # get lineup webpage
    print('getting webpage...')
    driver.get(lineup_url)
    driver.implicitly_wait(0.5)  # give page time to load

    # get lineup element
    print('finding lineup element...')
    lineup_element_class = "elementor-element-17d792c"
    lineup = driver.find_element(by=By.CLASS_NAME, value=lineup_element_class)

    # get all artist elements
    print('finding artist elements...')
    artist_elements = lineup.find_elements(by=By.XPATH, value=".//a[contains(@href, '/artists/')]")

    # build list of artist links
    print('grabbing artist links...')
    artist_links = []  # tuples of the form (artist link, artist name)

    for a_link in artist_elements:
        artist_links.append((a_link.get_attribute(name='href'), a_link.text))

    return artist_links


def pull_artist_spotify_id(artist_page_url: str, artist_name: str) -> str:
    """ Scrape the Spotify artist ID from the given FloridaGrooves artist page. """

    # switch selenium window to given artist page
    print(f"switching to artist page of {artist_name}...")
    driver.execute_script(f"window.location.href = '{artist_page_url}';")

    # grab Spotify iframe embed
    print('finding spotify embed iframe...')
    spotify_iframe = driver.find_element(by=By.TAG_NAME, value='iframe')
    embed_link = spotify_iframe.get_attribute(name='src')

    # extracting ID from embed link
    if embed_link[13:20] != 'spotify':  # spotify embed not found
        artist_id = 'NOT FOUND: ' + artist_name
    else:  # spotify embed is found
        artist_id = embed_link.split('?')[0].split('/')[-1]

    return artist_id


if __name__ == "__main__":
    # URL of the FloridaGrooves festival lineup page
    lineup_url = "https://floridagrovesfest.com/line-up/"

    # scrapes the lineup page and returns a generator for the artists
    print('scraping lineup page for artists...\n')
    artist_links = scrape_lineup()

    # scrape each page for their Spotify link and append to list
    spotify_artist_ids = []
    for artist_page, artist_name in artist_links:
        print('\nscraping artist page:', artist_name)
        artist_spotify_id = pull_artist_spotify_id(artist_page, artist_name)
        print(artist_name, 'Spotify ID:', artist_spotify_id)
        spotify_artist_ids.append(artist_spotify_id)

    # write artists IDs to JSON
    with open('fl_groves_lineup.json', 'w+') as out_file:
        json.dump({"artists": spotify_artist_ids}, out_file, indent=4)

    # closes selenium
    driver.quit()
