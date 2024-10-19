import sys
import argparse
from preprocess_SQL_files.extract_data import extract
from preprocess_SQL_files.transform_data import transform
from preprocess_SQL_files.query_data import (
    query_create,
    query_read,
    query_update,
    query_delete,
    query_1,
    query_2,
)


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="DE ETL And Query Script")
    parser.add_argument(
        "Functions",
        choices=[
            "extract",
            "transform",
            "query_create",
            "query_read",
            "query_update",
            "query_delete",
            "query_1",
            "query_2",
        ],
    )

    args = parser.parse_args(args[:1])
    print(args.Functions)
    if args.Functions == "extract":
        parser.add_argument("url")
        parser.add_argument("file_path")

    elif args.Functions == "transform":
        parser.add_argument("dataset")
        parser.add_argument("db_name")
        parser.add_argument("table_name")

    elif args.Functions == "query_create":
        parser.add_argument("dataset")
        parser.add_argument("table")
        parser.add_argument("colnames")
        parser.add_argument("values")


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
        print(transform(args.dataset, args.db_name, args.table_name))

    elif args.Functions == "query_create":
        print(query_create(args.database, args.table, args.colnames, args.values))

    else:
        print(f"Unknown function: {args.action}")


if __name__ == "__main__":
    main()
