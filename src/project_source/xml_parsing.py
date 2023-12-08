"""
Module for handling XML parsing and fetching/processing sitemap data.

This module provides two classes:
- XML: A class for parsing XML data from a specified URL.
- XMLname: A class for fetching and processing sitemap data from a base URL.
"""
import pandas as pd
import requests
from urllib.parse import urljoin
from xml.etree import ElementTree


class XML:
    """
    A class for parsing XML data from a specified URL.

    Methods:
    --------
    parse_xml:
        Fetches XML data from a specified URL, parses it, and returns the data as a Pandas DataFrame.

    Attributes:
    -----------
    None
    """

    def parse_xml(self):
        """
        Fetch XML data from a specified URL, parse it, and return the data as a Pandas DataFrame.

        Returns:
        --------
        pd.DataFrame:
            A DataFrame containing the parsed XML data.

        Raises:
        -------
        None
        """
        response = requests.get(
            "https://s3.amazonaws.com/sa-socrata-sitemaps-us-east-1-fedramp-prod/sitemaps/sitemap-data.cdc.gov.xml"
        )
        if response.ok:
            root = ElementTree.fromstring(response.content)
        root = root[0]
        print(root[0].text)
        r_2 = requests.get(root[0].text)

        if r_2.ok:
            root = ElementTree.fromstring(r_2.content)
        root = root

        records = [{field.tag: field.text for field in child} for child in root]
        records[:2]

        df = pd.DataFrame(records)
        return df


class XMLname:
    """
    A class for fetching and processing sitemap data from a base URL.

    Methods:
    --------
    fetch_robots_txt:
        Fetches the robots.txt file from the base URL and extracts sitemap URLs.

    get_sitemap_data:
        Retrieves sitemap URLs from the fetched robots.txt file and returns them as a Pandas DataFrame.

    Attributes:
    -----------
    base_url: str
        The base URL for fetching sitemap data.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_robots_txt(self):
        """
        Fetch the robots.txt file from the base URL and extract sitemap URLs.

        Returns:
        --------
        list:
            A list of sitemap URLs extracted from the robots.txt file.

        Raises:
        -------
        None
        """
        try:
            response = requests.get(urljoin(self.base_url, "robots.txt"))
            # response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching robots.txt: {e}")
            return []

        sitemap_urls = []
        for line in response.text.splitlines():
            if line.startswith("Sitemap:"):
                sitemap_url = line.split(": ")[1].strip()
                sitemap_urls.append(sitemap_url)

        return sitemap_urls

    def get_sitemap_data(self):
        """
        Retrieve sitemap URLs from the fetched robots.txt file and return them as a Pandas DataFrame.

        Returns:
        --------
        pd.DataFrame:
            A DataFrame containing sitemap URLs.

        Raises:
        -------
        None
        """
        # Get sitemap URLs
        sitemap_urls = self.fetch_robots_txt()
        # Create a DataFrame
        sitemap_df = pd.DataFrame({"Sitemap_URLs": sitemap_urls})

        return sitemap_df
