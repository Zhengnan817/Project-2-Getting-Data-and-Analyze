import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
# difine a class called WEB that can import in jupyternootbook
class Web:
    '''
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
    '''
    def scrap_web(self):
        '''
        Fetch HTML content from a specified URL and return a BeautifulSoup object.

        Returns:
        --------
        BeautifulSoup:
            A BeautifulSoup object representing the parsed HTML content of the page.

        Raises:
        -------
        None
        '''        
        url = "https://www.cars.com/shopping/jaguar/"
        
        r = requests.get(url) 
       
        c = r.content
        if r.status_code == 200:
                
        # Parse the HTML content of the page
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                return soup
        else:
                 print ("Fail")
                 return None
            # To extract the first and last page numbers
        paging = soup.find("div",{"id":"placardContainer"}).find("div",{"id":"paging"}).find_all("a")
        start_page = paging[1].text
        last_page = paging[len(paging)-2].text
    def convert_df(self):
        '''
        Extract information about universities from the HTML content and store it in a Pandas DataFrame.

        Returns:
        --------
        pd.DataFrame:
            A DataFrame containing information about universities.

        Raises:
        -------
        None
        '''
    # To extract the page content
        car = self.scrap_web().find_all ("div",{"class" :"vehicle-card-main js-gallery-click-card search-slugs"})


        car_dict = {}
        car_dict["store"] = car.find("h2",{"class" :"title"}).text
        car_dict["price"] = car.find("span",{"class" :"primary-price"}).text
        car_dict["mile"] = car.find("div",{"class" :"mileage"}).text
        
        # To store the dictionary to into a list
        car_dict.append(car_dict)
        df = pd.DataFrame(car_dict)


