# from bs4 import BeautifulSoup
# import requests
#
#
# url = "https://acme-test.uipath.com/login"
#
# page = requests.get(url)
# print(page)
#
# soup = BeautifulSoup(page.text,'html.parser')
#
# # print(soup.find('div'))
#
# print(soup.find_all('div',class_ = 'col-md-6'))

import requests
from bs4 import BeautifulSoup
import pandas as pd




# Function to scrape all selectors from a webpage
def scrape_selectors(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return None

    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to hold tag data
    tag_data = []

    # Loop through all tags and collect their names and attributes
    for tag in soup.find_all(True):  # True finds all tags
        tag_name = tag.name
        attributes = tag.attrs

        # Store the tag name and attributes in a dictionary
        tag_data.append({
            'tag': tag_name,
            'attributes': attributes
        })

    # Create a DataFrame from the collected tag data
    df = pd.DataFrame(tag_data)
    df.to_csv('selectors.csv', index=False)
    return df


# URL to scrape
url = 'https://acme-test.uipath.com/login'  # Replace with your target URL

# Scrape the selectors and store in a DataFrame
selectors_df = scrape_selectors(url)

# Display the DataFrame
if selectors_df is not None:
    print(selectors_df)

# Optionally, save the DataFrame to a CSV file
