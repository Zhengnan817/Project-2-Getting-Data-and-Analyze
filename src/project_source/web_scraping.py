import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


# difine a class called WEB that can import in jupyternootbook
class Web:
    """
    A class for web scraping information about universities.

    Methods:
    --------
    scrap_web:
        Fetches HTML content from a specified URL and returns a BeautifulSoup object.

    convert_df:
        Extracts information about universities from the HTML content and stores it in a Pandas DataFrame.

    Attributes:
    -----------
    None
    """

    def scrap_web(self):
        """
        Fetch HTML content from a specified URL and return a BeautifulSoup object.

        Returns:
        --------
        BeautifulSoup:
            A BeautifulSoup object representing the parsed HTML content of the page.

        Raises:
        -------
        None
        """
        self.url = "https://www.collegeevaluator.com/rankings/new-york-best-colleges/"
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
        else:
            print("The web is scraped successfully")
        soup = BeautifulSoup(response.content, "html.parser")

        # To extract the page content
        school_ranks = soup.find(
            "table", class_="comparison default br tdc ranked dataTable"
        )
        if school_ranks is not None:
            university_table = school_ranks.find("th")
            university_table_titles = [title.text.strip() for title in university_table]

            df = pd.DataFrame(columns=university_table_titles)

            column_data = school_ranks.find("tr")
        else:
            print("Table not found")
        for row in column_data:
            row_data = row.find("td")
            individual_row_data = [data.text.strip() for data in row_data]
            length = len(df)
            df.loc[length] = individual_row_data
        print(df)

        # for row in schools_data:
        #     schools_data = {}
        #     schools_data["rank"] = [
        #         cell.get_text(strip=True)
        #         for cell in school_ranks.find_all(["th", "td"])
        #     ]

        #     # Append dictionary to the list
        #     schools_data.append(schools_data)

        # # Convert the list of dictionaries to DataFrame
