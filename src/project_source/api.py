import pandas as pd
import numpy as np
import requests


# difine a class called API that can import in jupyternootbook
class API:
    """
    A class for get data by API.

    Methods:
    --------
    api_step_1:
        Fetches data from the API endpoint and returns it as a Pandas DataFrame.

    Attributes:
    -----------
    None
    """

    def api_step_1(self):
        """
        Fetches data from the API endpoint and returns it as a Pandas DataFrame.

        Returns:
        -------
        pd.DataFrame:
            A DataFrame containing the fetched data with columns:
            ["date", "hour", "route", "direction", "stop", "boardings", "typeday"].

        Raises:
        -------
        Exception:
            Raises an exception if something goes wrong during the API request.
        """
        response = requests.get("https://data.cityofnewyork.us/resource/t5n6-gx8c.json")
        if response.ok:
            data = response.json()
            return pd.DataFrame(
                data,
                columns=[
                    "date",
                    "hour",
                    "route",
                    "direction",
                    "stop",
                    "boardings",
                    "typeday",
                ],
            )
        else:
            raise Exception("Something went wrong")
