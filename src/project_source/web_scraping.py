"""
Module for web scraping information about universities.

This module provides a class, `Web`, that encapsulates methods for fetching HTML content
from a specified URL, creating a BeautifulSoup object, and converting the extracted
information about universities into a Pandas DataFrame.
"""
import pandas as pd
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

    def scrap_university_web(self):
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

        response = requests.get(
            "https://www.collegeevaluator.com/rankings/new-york-best-colleges/"
        )
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"id": "new-york-best-colleges-table"})
        header = table.find("thead")
        head = [x.text.strip() for x in header.find_all("th")]
        df = pd.DataFrame(columns=head)
        rows = table.find("tbody").find_all("tr")
        for r in rows:
            rank, school = [x.text.strip() for x in r.find_all("th")]
            columns = [x.text.strip() for x in r.find_all("td")]
            row_data = [rank, school] + columns
            length = len(df)
            df.loc[length] = row_data
        return df
