# 🎬 IMDb Top 250 Movies Scraper

This project is a web scraping application that collects data from IMDb’s [Top 250 Movies Chart](https://www.imdb.com/chart/top/). The goal is to extract and analyze key information about the most critically acclaimed movies according to IMDb rankings.

---

## 📌 Objective

To programmatically extract data from IMDb’s Top 250 list, including:

- Movie title  
- Release year  
- IMDb rating  
- Director and top stars  
- Movie URL

This data can be used for further analysis, visualization, or as part of a larger data pipeline or portfolio project.

---

## 🔧 Tools & Technologies Used

- **Python**  
- **Libraries:** `requests`, `BeautifulSoup`, `pandas`, `time`  
- **Jupyter Notebook** (for development and exploration)

---

## 🗂️ Features

- Efficient web scraping of all 250 movie entries.
- Stores data in a structured format (CSV or DataFrame).
- Robust against changes in chart position or minor HTML shifts.
- Includes throttling (delays) to avoid overloading the server.

---

## 📈 Sample Data Extracted

| Rank | Title                     | Year | Rating | Director             | Stars                       |
|------|---------------------------|------|--------|----------------------|-----------------------------|
| 1    | The Shawshank Redemption  | 1994 | 9.2    | Frank Darabont       | Tim Robbins, Morgan Freeman |
| 2    | The Godfather             | 1972 | 9.2    | Francis Ford Coppola | Marlon Brando, Al Pacino   |
| ...  | ...                       | ...  | ...    | ...                  | ...                         |

---

## 📁 Output

The final data is saved as:

- `imdb_top_250.csv` – containing all movie details.

---


## 🙋‍♂️ About Me

I'm **Adam Abozaid**, a data analyst passionate about using data to uncover stories and support decisions.  
This project demonstrates my full workflow — from **scraping** and **cleaning data**, to **analysis** and **interactive visualization**.

🔗 [LinkedIn](https://www.linkedin.com/in/adam-abozaid-643877225)  
💻 [GitHub](https://github.com/AdamAozaid)

---

## 📬 Contact

I'm open to feedback, collaborations, and opportunities.  
📧 adamabozaid18@gmail.com

