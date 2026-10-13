# CodeAlpha Data Analytics Internship Projects

## Overview

Welcome to my **CodeAlpha Data Analytics Internship Projects** repository. This repository contains the projects I completed as part of my Data Analyst Internship, demonstrating practical skills in data collection, data cleaning, exploratory data analysis, data visualization, and sentiment analysis using Python.

The goal of these projects was to apply data analytics techniques to real-world and practice datasets, extract meaningful insights, and present findings through clear visualizations and organized documentation.

## Projects Included

### Task 1: Web Scraping

**Objective:** Collect structured data from a website using Python.

- Used `requests` and `BeautifulSoup` to extract book information from Books to Scrape.
- Collected book titles, prices, ratings, availability, and URLs.
- Used `pandas` to organize and clean the extracted data.
- Exported the collected data into a CSV file.

**Key Skills:** Web scraping, HTML parsing, data extraction, data cleaning, and CSV handling.

### Task 2: Exploratory Data Analysis (EDA)

**Objective:** Explore a dataset to identify patterns, trends, and useful insights.

- Examined dataset structure, data types, and missing values.
- Analyzed book prices and rating distributions.
- Compared average prices across rating categories.
- Identified expensive and inexpensive books.
- Investigated price outliers and relationships between variables.

**Key Skills:** Data exploration, descriptive statistics, data quality assessment, and analytical reasoning.

### Task 3: Data Visualization

**Objective:** Communicate findings through meaningful visualizations.

- Created a histogram to examine book price distribution.
- Visualized book ratings and average prices by rating.
- Identified the most expensive and least expensive books.
- Used a scatter plot to explore the relationship between price and rating.
- Created a box plot to examine price variation and outliers.

**Key Skills:** Matplotlib, Seaborn, chart design, data interpretation, and visual communication.

### Task 4: Sentiment Analysis

**Objective:** Apply Natural Language Processing (NLP) techniques to analyze the sentiment of written reviews.

- Used the Sentiment Labelled Sentences dataset from the UCI Machine Learning Repository.
- Combined 3,000 reviews from Amazon, IMDb, and Yelp.
- Applied NLTK's VADER sentiment analyzer to calculate sentiment scores.
- Classified reviews as positive, negative, or neutral.
- Visualized sentiment distributions overall and across review sources.
- Compared non-neutral sentiment predictions with the dataset's original positive and negative labels.

**Key Skills:** Natural Language Processing, text analysis, sentiment classification, NLTK, and data visualization.

## Technologies and Tools

The following tools and libraries were used throughout the projects:

- **Python** — primary programming language
- **Jupyter Notebook** — interactive development and analysis
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical computing
- **Requests** — HTTP requests for web scraping
- **BeautifulSoup** — HTML parsing
- **Matplotlib** — data visualization
- **Seaborn** — statistical visualization
- **NLTK VADER** — rule-based sentiment analysis

## Repository Structure

The repository is organized into separate folders for each task.

```text
CodeAlpha_Data_Analytics_Internship/
│
├── Task_1_Web_Scraping/
│   ├── web_scraping.ipynb
│   ├── books_data.csv
│   └── README.md
│
├── Task_2_Exploratory_Data_Analysis/
│   ├── eda.ipynb
│   ├── books_data.csv
│   └── README.md
│
├── Task_3_Data_Visualization/
|   ├── BI_Dasboard.pibix
│   ├── books_data.csv
│   ├── Data_visualizations.ipynb
│   └── README.md
│
├── Task_4_Sentiment_Analysis/
│   ├── sentiment_analysis.ipynb
│   ├── output/
│   │   ├── sentiment_analysis_results.csv
│   │   ├── sentiment_summary.csv
│   │   └── compound_sentiment_distribution.png
│   └── README.md
│
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ifypedro/CodeAlpa-DataAnalytics
cd CodeAlpha_DataAnalytics
```

### 2. Install the required libraries

```bash
pip install pandas numpy requests beautifulsoup4 matplotlib seaborn nltk
```

For Task 4, download the VADER lexicon from within Python:

```python
import nltk
nltk.download("vader_lexicon")
```

### 3. Run the notebooks

Open the relevant `.ipynb` file using Jupyter Notebook or JupyterLab and execute the cells in order.

Some tasks require an internet connection to download datasets or retrieve web pages.

## Key Learning Outcomes

Through these projects, I developed practical experience in:

- Collecting data from web pages.
- Cleaning, organizing, and validating datasets.
- Performing exploratory data analysis.
- Creating visualizations to communicate findings.
- Applying NLP techniques to textual data.
- Interpreting analytical results and identifying limitations.
- Documenting Python projects and organizing work for GitHub.

## Data Sources

- **Web Scraping:** [Books to Scrape](https://books.toscrape.com/) — a practice website designed for web scraping.
- **Sentiment Analysis:** [UCI Sentiment Labelled Sentences Dataset](https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences).

The books dataset was collected for the web scraping project. The sentiment dataset was obtained from the UCI Machine Learning Repository.

## Limitations

- Web scraping results may change when the source website is updated.
- Exploratory analysis and visualizations describe the available data and do not necessarily establish causal relationships.
- VADER is a rule-based sentiment analyzer and may misinterpret sarcasm, context, or complex expressions.
- Sentiment predictions may differ from the original dataset labels.

## Conclusion

These projects demonstrate my developing skills in Python-based data analytics, from collecting and preparing data to exploring patterns, building visualizations, and analyzing textual sentiment.

Completing these tasks strengthened my understanding of the data analysis workflow and provided practical experience in using common Python libraries to turn raw data into useful insights.

## Acknowledgment

I would like to thank **CodeAlpha** for providing the internship opportunity and project tasks that supported my learning and practical development in data analytics.

---

**Author:** Onwubuya Ifeanyi Pedro

**Role:** Data Analyst Intern

**Tools:** Python | Pandas | Matplotlib | Seaborn | BeautifulSoup | NLTK | PowerBI

**Repository:** CodeAlpha Data Analytics Internship Projects
