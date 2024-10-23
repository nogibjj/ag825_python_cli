from extract import extract
from transform_load import load
from query import crud
import sys
import argparse

# @click.command()
# @click.option("--name", default="World", help="Name to greet")
# def run_crud():
#     crud()


# if __name__ == "__main__":
#     url = "https://raw.githubusercontent.com/nogibjj/ag825_sqlite_lab/refs/heads/main/Cancer_Data.csv"
#     file_path = "Cancer_Data.csv"
#     database = "CancerDB.db"

#     # Extract
#     print("Extracting data...")
#     extract(url, file_path)

#     # Transform and load
#     print("Transforming data...")
#     load()

#     # Query
#     print("Querying data...")
#     crud()


# from mylib.extract import extract
# from mylib.transform_load import load
# from mylib.query import (
#     general_query,
# )


def handle_arguments(args):
    """Add action based on initial calls"""
    parser = argparse.ArgumentParser(
        description="CRUD Script", formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "action",
        choices=["extract", "transform_load", "crud"],
        help="""We can perform the following actions (in order):
        - extract: Extract data from the .csv file
        - transform_load: Create the database (.db file) and load data into the database
        - CRUD: Perform all 4 CRUD operations
        """,
    )

    # Add query argument if the action is general_query
    if len(args) > 0 and args[0] == "general_query":
        parser.add_argument("query", help="The SQL query to execute.")

    # Parse arguments
    return parser.parse_args(args)


def main():
    url = "https://raw.githubusercontent.com/nogibjj/ag825_sqlite_lab/refs/heads/main/Cancer_Data.csv"
    file_path = "Cancer_Data.csv"
    # database = "CancerDB.db"

    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract(url, file_path)
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "crud":
        crud()
    # else:
    #     print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
