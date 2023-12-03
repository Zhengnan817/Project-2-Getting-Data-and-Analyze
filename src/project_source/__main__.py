"""Enable running `python -m project_package`."""

"""Run Getting data and analyze for part 1 to part 4 """

from .EDA import Ferry_EDA
from .web_scraping import Web
from .xml_parsing import XMLname
from .api import API


def main():
    """
    Run Chip analysis as a script.
    """
    print("------------------------------------------------")
    print("Project_2_Getting_Data_and_Analysis")
    print("------------------------------------------------")
    part1()
    print("------------------------------------------------")
    part2()
    print("------------------------------------------------")
    part4()
    print("------------------------------------------------")
    part3()


def part1():
    xmlname_instance = XMLname(base_url="https://data.cdc.gov")
    # Call the method on the instance
    result_df = xmlname_instance.get_sitemap_data()
    # Print or use the result DataFrame as needed
    print(result_df)

    from src.project_source.xml_parsing import XML

    part_1 = XML()
    part_1.parse_xml()


def part2():
    part_2 = API()
    df = part_2.api_step_1()
    print(df)


def part3():
    from src.project_source.web_scraping import Web

    part_3 = Web()
    print(part_3)

    print(part_3.scrap_web())

    result = part_3.convert_df()

    # Print or use the result as needed
    print(result)


def part4():
    part_4 = Ferry_EDA()
    part_4.route_analysis()
    part_4.hour_analysis()
    part_4.directional_analysis()
    part_4.stop_specific_analysis()


main()
