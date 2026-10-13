# Task 4: Sentiment Analysis

## Objective
Analyze customer and movie reviews to identify positive, negative, and neutral sentiment using Natural Language Processing (NLP).

## Dataset
The Sentiment Labelled Sentences dataset from the UCI Machine Learning Repository, containing reviews from Amazon, IMDb, and Yelp.

- Total reviews: 3,000
- Amazon: 1,000
- IMDb: 1,000
- Yelp: 1,000

## Tools and Libraries
- Python
- Pandas
- Matplotlib
- Seaborn
- NLTK VADER

## Methodology
1. Loaded and combined the three review datasets.
2. Checked the dataset structure and sentiment labels.
3. Used NLTK VADER to calculate negative, neutral, positive, and compound sentiment scores.
4. Classified reviews as positive, negative, or neutral.
5. Visualized sentiment distributions overall and by review source.
6. Compared non-neutral VADER predictions with the original binary labels.

## Visualizations
- Overall predicted sentiment distribution
- Sentiment distribution by review source
- Compound sentiment score distribution

## Output Files
- `output/sentiment_analysis_results.csv`
- `output/sentiment_summary.csv`
- `output/compound_sentiment_distribution.png`

## Limitations
VADER is a rule-based sentiment analyzer and may misinterpret sarcasm, context, or complex wording. Its predictions are not guaranteed to match the original dataset labels.

## Conclusion
This project demonstrates how NLP can be used to analyze review sentiment and visualize differences across review sources. Actual sentiment counts and comparison accuracy should be reported from the notebook's results.
