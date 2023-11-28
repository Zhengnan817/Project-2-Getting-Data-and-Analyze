import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.project_source.api import API


class Ferry_EDA:
    """
    A class for conducting exploratory data analysis (EDA) on NYC Ferry data.

    Methods:
    --------
    route_analysis:
        Analyzes NYC Ferry boardings by route and visualizes the results using a bar plot.

    hour_analysis:
        Analyzes hourly patterns of NYC Ferry boardings and visualizes the results using a line plot.

    directional_analysis:
        Analyzes NYC Ferry boardings by direction and visualizes the results using a bar plot.

    stop_specific_analysis:
        Analyzes NYC Ferry boardings by stop and visualizes the results using a bar plot.

    day_of_week:
        Analyzes NYC Ferry boardings by day of the week and visualizes the results using a bar plot.

    overall_trend:
        Analyzes the overall trend of NYC Ferry boardings over time and visualizes the results using a line plot.

    Attributes:
    -----------
    None
    """

    def route_analysis(self):
        """
        Analyze NYC Ferry boardings by route and visualize the results using a bar plot.

        Returns:
        --------
        None
        """

        part_2 = API()
        df = part_2.api_step_1()
        df["date"] = pd.to_datetime(df["date"])
        df["boardings"] = pd.to_numeric(df["boardings"], errors="coerce")
        route_boardings = (
            df.groupby("route")["boardings"].sum().sort_values(ascending=False)
        )
        plt.figure(figsize=(10, 6))
        sns.barplot(x=route_boardings.index, y=route_boardings.values)
        plt.title("NYC Ferry Boardings by Route")
        plt.xlabel("Route")
        plt.ylabel("Total Boardings")
        plt.xticks(rotation=45)
        plt.show()

    def hour_analysis(self):
        """
        Analyze hourly patterns of NYC Ferry boardings and visualize the results using a line plot.

        Returns:
        --------
        None
        """
        part_2 = API()
        df = part_2.api_step_1()
        df["date"] = pd.to_datetime(df["date"])
        df["boardings"] = pd.to_numeric(df["boardings"], errors="coerce")
        hourly_boardings = df.groupby("hour")["boardings"].mean()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=hourly_boardings.index, y=hourly_boardings.values)
        plt.title("Hourly Patterns of NYC Ferry Boardings")
        plt.xlabel("Hour of the Day")
        plt.ylabel("Average Boardings")
        plt.show()

    def directional_analysis(self):
        """
        Analyze NYC Ferry boardings by direction and visualize the results using a bar plot.

        Returns:
        --------
        None
        """
        part_2 = API()
        df = part_2.api_step_1()
        df["date"] = pd.to_datetime(df["date"])
        df["boardings"] = pd.to_numeric(df["boardings"], errors="coerce")
        direction_boardings = df.groupby("direction")["boardings"].sum()
        plt.figure(figsize=(8, 5))
        direction_boardings.plot(kind="bar", color=["skyblue", "lightcoral"])
        plt.title("Directional Analysis of NYC Ferry Boardings")
        plt.xlabel("Direction")
        plt.ylabel("Total Boardings")
        plt.show()

    def stop_specific_analysis(self):
        """
        Analyze NYC Ferry boardings by stop and visualize the results using a bar plot.

        Returns:
        --------
        None
        """
        part_2 = API()
        df = part_2.api_step_1()
        df["date"] = pd.to_datetime(df["date"])
        df["boardings"] = pd.to_numeric(df["boardings"], errors="coerce")
        stop_boardings = (
            df.groupby("stop")["boardings"].sum().sort_values(ascending=False)
        )
        plt.figure(figsize=(12, 6))
        sns.barplot(x=stop_boardings.index, y=stop_boardings.values)
        plt.title("NYC Ferry Boardings by Stop")
        plt.xlabel("Stop")
        plt.ylabel("Total Boardings")
        plt.xticks(rotation=45)
        plt.show()

    def day_of_week(self):
        """
        Analyze NYC Ferry boardings by day of the week and visualize the results using a bar plot.

        Returns:
        --------
        None
        """
        part_2 = API()
        df = part_2.api_step_1()
        df["date"] = pd.to_datetime(df["date"])
        df["boardings"] = pd.to_numeric(df["boardings"], errors="coerce")
        day_of_week_boardings = (
            df.groupby("typeday")["boardings"].mean().sort_values(ascending=False)
        )
        plt.figure(figsize=(8, 5))
        sns.barplot(x=day_of_week_boardings.index, y=day_of_week_boardings.values)
        plt.title("Day of Week Analysis of NYC Ferry Boardings")
        plt.xlabel("Day of Week")
        plt.ylabel("Average Boardings")
        plt.show()

    def overall_trend(self):
        """
        Analyze the overall trend of NYC Ferry boardings over time and visualize the results using a line plot.

        Returns:
        --------
        None
        """
        part_2 = API()
        df = part_2.api_step_1()
        df["date"] = pd.to_datetime(df["date"])
        df["boardings"] = pd.to_numeric(df["boardings"], errors="coerce")
        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)
        daily_boardings = df.resample("D").sum()
        plt.figure(figsize=(12, 6))
        plt.plot(daily_boardings.index, daily_boardings["boardings"], marker="o")
        plt.title("Daily NYC Ferry Boardings Over Time")
        plt.xlabel("Date")
        plt.ylabel("Boardings")
        plt.show()
