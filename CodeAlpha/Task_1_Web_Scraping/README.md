# Book Products Web Scraping Project

## Project Overview

This project was completed as part of the *CodeAlpha Data Analytics Internship*.

The objective of this project is to collect structured book information from a publicly available practice website using Python web-scraping techniques.

The scraped data contains information such as book titles, prices, ratings, availability, and product URLs. The resulting dataset is cleaned and saved as a CSV file, making it suitable for further analysis and visualization.

---

## Project Objective

The main objectives of this project are to:

- Extract book information from a website using Python.
- Understand and navigate HTML webpage structures.
- Use web-scraping libraries to automate data collection.
- Scrape data across multiple pages.
- Store the collected information in a structured format.
- Perform basic data cleaning and validation.
- Export the final dataset to a CSV file.
- Prepare the dataset for further exploratory data analysis and visualization.

---

## Tools and Technologies

The following tools and Python libraries were used:

| Tool / Library | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests to the website |
| BeautifulSoup | Parsing HTML and extracting information |
| Pandas | Data processing and DataFrame creation |
| Jupyter Notebook | Development and testing environment |
| CSV | Storage format for the final dataset |
| GitHub | Project version control and portfolio |

---

##  Data Source

The data was collected from:

*Books to Scrape*

https://books.toscrape.com/

Books to Scrape is a practice website designed for learning and testing web-scraping techniques.

The website contains information about books including their titles, prices, ratings, and availability.

---

## Dataset Description

The final dataset contains approximately *1,000 book records* collected across multiple pages.

The dataset contains the following columns:

| Column | Description |
|---|---|
| Title | Title of the book |
| Price | Price of the book in British Pounds (£) |
| Rating | Customer rating represented from One to Five |
| Availability | Availability status of the book |
| URL | Product page URL |

### Dataset Size

- *Rows:* 1,000
- *Columns:* 5

---

## Methodology

The project followed the following workflow:

### 1. Send HTTP Request

The requests library was used to connect to the website and retrieve its HTML content.

```python```
response = requests.get(url).

The HTTP response was checked to ensure that the webpage was successfully retrieved 

### 2. Parse the HTML 
BeautifulSoup was used to parse the HTML content.

- soup = BeautifulSoup(response.text, "html.parser")

This allowed the required elements of the webpage to be located and extracted.

### 3. Identify Book Products
Book products were identified using their HTML structure:
books = soup.find_all("article", class_="product_pod")

### 4. Extract Relevant Information
For each book, the following information was extracted:
Title
Price
Rating
Availability
Product URL

### 5. Scrape Multiple Pages
The scraper was designed to iterate through 50 catalogue pages.
for page in range(1, 51):
This allowed the project to collect approximately 1,000 book records instead of limiting the dataset to a single webpage.

### 6. Create a DataFrame
The extracted records were stored in a Pandas DataFrame.
df = pd.DataFrame(books_data)

### 7. Clean the Data
The price column originally contained the A£ currency symbol.
The symbol was removed and the values were converted from text to numeric values.
books_data_multipage_df["Price"] = books_data_multipage_df["Price"].str.replace("£", "", regex=False)
books_data_multipage_df["Price"] = books_data_multipage_df["Price"].str.replace("Â", "", regex=False)  # Remove the problematic Unicode character
books_data_multipage_df["Price"] = books_data_multipage_df["Price"].astype(float)
This makes the price column suitable for calculations and future analysis.

### 8. Validate the Dataset
The dataset was checked for missing values and duplicate records.
books_data_multipage_df.isnull().sum()
and:
books_data_multipage_df.duplicated().sum()
The investigation also identified one repeated book title with different prices. Because the records were not identical, they were not automatically removed.
This demonstrates that duplicate records should be investigated before deleting them.

### 10. Export the Dataset
The cleaned dataset was exported to CSV format:
books_data_multipage_df.to_csv("books_dataset.csv", index=False)

---

## Results
The scraping process successfully collected approximately 1,000 book records from 50 catalogue pages.
The final dataset contains:
- 1,000 book records
- 5 columns
- Book titles
- Numeric book prices
- Book ratings
- Availability information
- Product URLs

The dataset was also checked for missing values, duplicate records, and appropriate data types.
The resulting CSV file can be used for further Exploratory Data Analysis (EDA) and Data Visualization.

---

## Project Structure
CodeAlpha_Web_Scraping/
│
├── CodeAlpha_web_scraping.py
├── books_dataset.csv
├── web_scraping.ipynb
└── README.md

---

## File Descriptions
- CodeAlpa_web_scraping.py
  Contains the Python code used to scrape, clean, and save the book data.

- books_dataset.csv
  Contains the final scraped dataset.

- web_scraping.ipynb
  Contains the python step by step processes took to scrape, clean, and save the book data.
  
- README.md
  Contains the project documentation, methodology, results, and instructions.

---

## How to Run the Project
1. Clone the repository
   git clone https://github.com/ifypedro/CodeAlpa-DataAnalytics
2. Navigate into the project folder
   cd CodeAlpha_internship
3. Navigate into the project file
   Task_1_web_scraping
4. Install the required libraries
   pip install requests beautifulsoup4 pandas
5. Run the Python script
   python CodeAlpha_web_scraping.py
   The script will scrape the website, process the data, and create:
   books_dataset.csv

---

## Key Learning Outcomes
Through this project, I gained practical experience in:
- Web scraping with Python
- HTML and webpage structure
- HTTP requests
- BeautifulSoup
- Data extraction
- Pandas DataFrames
- Data cleaning
- Data validation
- CSV data storage
- Preparing datasets for analysis

---

## Future Improvements
Possible improvements to this project include:
- Adding error handling for failed HTTP requests.
- Adding request delays to make the scraper more robust.
- Automatically detecting the final page instead of assuming 50 pages.
- Extracting additional book information.
- Adding logging to track scraping progress.
- Performing Exploratory Data Analysis on the collected dataset.
- Creating visualizations and dashboards from the dataset.

---

## Author
Onwubuya Ifeanyi Pedro (PEDROTECH)
Data Analyst Intern
CodeAlpha Data Analytics Internship

---

## Internship Task
CodeAlpha Data Analytics Internship — Web Scraping Task
This project demonstrates the use of Python to collect, clean, and structure web-based data for analytical purposes.