# **WEB SCRAPPING PROJECT - FLIPKART REVIEWS** 

This is a Python project for web scraping Flipkart reviews for a searched product. It demonstrates how to extract customer reviews from Flipkart using Python and the BeautifulSoup library.


## **Table of Conents**

1. Overview
2. Installation
3. Usage
4. Dependencies

## **Overview**

Web scraping is the process of extracting data from websites automatically. The *Flipkart Reviews Web Scraping* project allows you to retrieve customer reviews for a specific product from the Flipkart website. It utilizes web scraping techniques to extract the review details, such as the reviewer's name, ratings, and comments, for analysis or further processing.

## **Installation**

To use this project, follow these steps:

1. Clone the repository.

`git clone https://github.com/Ansh1999/Web_Scrapping_Flipkart_Reviews.git`

2. Change directory to the project directory.
3. Install the dependencies from requirements.txt file.

`pip install -r requirements.txt`

## **Usage**

1. Open the app.py file.
2. Run the script using the following command:

`python app.py`

3. Access the API endpoints and HTML page by opening a web browser and navigating to `http://localhost:5000`.
4. Enter a search query for the desired product in the search bar.
5. The page will display the first 10 reviews for the searched product, scraped from Flipkart.

## **Logging**

This project includes logging functionality to record important events and information during the web scraping process. The logs are saved with {time,date}.log file in the LOGS directory.

## **Data Saving in CSV Format** 

The project saves the scraped reviews as CSV files in the data directory. Each search query will result in a separate {ProductName}.csv file containing the name,ratings and reviews for that specific product.

## **Dependencies**

The project relies on the following Python libraries:

1. `flask` : For API development and serving the HTML page.
2. `beautifulsoup4 (bs4)` : For parsing the HTML structure and extracting the review data from the Flipkart web page.
3. `requests` : For sending HTTP requests to the Flipkart website and fetching the page content.

All the dependencies are listed in the `requirements.txt` file.

# HAPPY CODING



