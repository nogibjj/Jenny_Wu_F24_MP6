import sys
import argparse
from preprocess_SQL_files.extract_data import extract
from preprocess_SQL_files.transform_data import transform
from preprocess_SQL_files.query_data import general_query


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="DE ETL And Query Script")
    parser.add_argument(
        "Functions",
        choices=[
            "extract",
            "transform",
            "general_query",
        ],
    )

    args = parser.parse_args(args[:1])
    print(args.Functions)
    if args.Functions == "extract":
        parser.add_argument("url")
        parser.add_argument("file_path")

    elif args.Functions == "transform":
        parser.add_argument("dataset")
        parser.add_argument("table_name")
        parser.add_argument("table_parameter")

    elif args.Functions == "general_query":
        parser.add_argument("query")

    # parse again
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""

    args = handle_arguments(sys.argv[1:])

    if args.Functions == "extract":
        print("Extracting data...")
        print(extract(args.url, args.file_path))

    elif args.Functions == "transform":
        print("Transforming and loading data...")
        print(transform(args.dataset, args.table_name, args.table_parameter))

    elif args.Functions == "query_create":
        print(general_query(args.query))

    else:
        print(f"Unknown function: {args.action}")


if __name__ == "__main__":
    main()
