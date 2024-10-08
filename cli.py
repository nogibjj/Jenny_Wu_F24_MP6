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

    elif args.Functions == "query_read":
        parser.add_argument("dataset")
        parser.add_argument("table")

    elif args.Functions == "query_update":
        parser.add_argument("database_name")
        parser.add_argument("table")
        parser.add_argument("column")
        parser.add_argument("new_value", type=int)
        parser.add_argument("Incident_Key", type=int)

    elif args.Functions == "query_delete":
        parser.add_argument("database")
        parser.add_argument("table")
        parser.add_argument("Incident_Key", type=int)

    elif args.Functions == "query_1":
        parser.add_argument("database")
        parser.add_argument("table")

    elif args.Functions == "query_2":
        parser.add_argument("database")
        parser.add_argument("table")

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

    elif args.Functions == "query_read":
        print(query_read(args.dataset, args.table))

    elif args.Functions == "query_update":
        print(query_update(args.database_name, args.table, args.column, args.new_value))

    elif args.action == "query_delete":
        print(query_delete(args.database, args.table, args.Incident_Key))

    elif args.Functions == "query_1":
        print(query_1(args.database, args.table))

    elif args.Functions == "query_2":
        print(query_2(args.database, args.table))

    else:
        print(f"Unknown function: {args.action}")


if __name__ == "__main__":
    main()
