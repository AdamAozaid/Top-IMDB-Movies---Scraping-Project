import requests
from bs4 import BeautifulSoup
import csv

# IMDb Top 250 URL
url = "https://www.imdb.com/chart/top/"

# Headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

# Make the request
response = requests.get(url, headers=headers)
print(f"Response status code: {response.status_code}")

def main(page):
    soup = BeautifulSoup(page.content, "lxml")
    top_movies = []

    # Select movie containers
    movies = soup.find_all("li", {"class": "ipc-metadata-list-summary-item"})
    print(f"Found {len(movies)} movies")

    for movie in movies:
        try:
            # Title
            title = movie.find("h3", class_="ipc-title__text").text.strip()

            # Year and Duration
            metadata = movie.find_all("span", class_="cli-title-metadata-item")
            year = metadata[0].text.strip() if len(metadata) > 0 else "N/A"
            duration = metadata[1].text.strip() if len(metadata) > 1 else "N/A"

            # Rating
            rating = movie.find("span", class_="ipc-rating-star--rating")
            rate = rating.text.strip() if rating else "N/A"

            # Add each movie as a row (list of values)
            top_movies.append([title, year, duration, rate])
            print(f"{title} ({year}) - {duration} - Rating: {rate}")

        except Exception as e:
            print(f"Error processing a movie: {e}")
            continue

    # Write to CSV correctly
    with open("Top-Movies.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Year', 'Duration', 'Rate'])
        writer.writerows(top_movies)

main(response)
