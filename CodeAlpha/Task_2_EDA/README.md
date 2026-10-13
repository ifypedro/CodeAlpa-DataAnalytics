## Key Findings

### 1. Dataset Overview

The dataset contains 1,000 book records collected from Books to Scrape. Each record contains the book title, price, rating, availability status, and product URL.

### 2. Price Analysis

The average and median prices provide an overview of the typical book price in the dataset. The minimum and maximum prices show the overall price range.

### 3. Rating Distribution

The rating distribution shows how the books are distributed across one- to five-star ratings. The most frequently occurring rating represents the dominant rating category in the dataset.

### 4. Rating and Price Relationship

The average price was calculated for each rating category to investigate whether higher-rated books tend to have higher prices.

Correlation was also calculated between rating and price. However, correlation measures association and does not imply causation.

### 5. Outlier Analysis

The Interquartile Range (IQR) method was used to identify unusually high or low book prices. These observations were treated as potential outliers rather than automatically being considered errors.

### 6. Data Quality

The dataset was checked for missing values and duplicate rows. The repeated book title identified during the cleaning process was investigated rather than automatically removed because the records had different prices.

### 7. Availability

The availability column was examined to determine whether the books in the dataset were listed as available or unavailable.