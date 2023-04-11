"""EX08: Data Wrangling!"""


__author__ = "730572335"

from csv import DictReader
DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""

    result: list[dict[str. str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in table:
        sub_list: list[str] = []
        data_to_get: list[str] = table[key]
        idx: int = 0
        while idx < rows:
            sub_list.append(data_to_get[idx])
            idx += 1
        result[key] = sub_list
    return result


def select(user_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns specific column from a table as specified by the user."""
    result: dict[str, list[str]] = dict()
    for i in columns:
        result[i] = user_table[i]
    return result


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenates 2 dictionaries into one new dictionary."""
    result: dict[str, list[str]] = dict()
    for column in dict_1:
        result[column] = dict_1[column]
    for column in dict_2:
        if column in result:
            result[column] += dict_2[column]
        else:
            result[column] = dict_2[column]
    return result



def count(counting_dict: list[str]) -> dict[str, int]:
    """This function returns a dictionary that counts how many times a value appears in the given dictionary."""
    output_dict: dict[str, int] = {}
    for item in counting_dict:
        if item in output_dict:
            output_dict[item] += 1
        else:
            output_dict[item] = 1
    return output_dict