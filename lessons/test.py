def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in table:
        sub_list: list[str] = []
        data_get: list[str] = table[key]
        idx: int = 0
        while idx < rows and idx < len(data_get):
            sub_list.append(data_get[idx])
            idx += 1
        result[key] = sub_list
    return result



def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in table:
        sub_list: list[str] = []
        data_get: list[str] = table[key]
        idx: int = 0
        while idx < rows and idx < len(data_get[key]):
            sub_list.append(data_get[key][idx])
            idx += 1
        result[key] = sub_list
    return result