from sqlalchemy import select, column
from sqlalchemy.orm import Session
from src.utils.BoolConvert import strtobool
from src.utils.SortParams import SortDataList

# for pagination purposes
def get_the_pagination(
    object_name: object, query_of: list[str], query_by: list[str]
) -> object:
    query_check = select(object_name)
    if query_of != None:
        for idx in range(len(query_of)):
            if query_by[idx] == "is_active":
                query_check = query_check.where(
                    column(query_by[idx]).contains(strtobool(query_of[idx]))
                )
            query_check = query_check.where(
                column(query_by[idx]).contains(query_of[idx])
            )
    return query_check


def get_the_pagination_with_join(
    query_set: object, query_of: list[str], query_by: list[str]
) -> object:
    query_check = query_set
    if query_of != None:
        for idx in range(len(query_of)):
            if query_by[idx] == "is_active":
                query_check = query_check.where(
                    column(query_by[idx]).contains(strtobool(query_of[idx]))
                )
            query_check = query_check.where(
                column(query_by[idx]).contains(query_of[idx])
            )
    return query_check


def get_the_pagination_search(query_str: object, all_params: dict()) -> object:
    query_check = query_str
    n = len(all_params)
    idx = []
    for i in range(0, n):
        if list(all_params.values())[i] != None:
            idx.append(i)
    if idx != None:
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            query_check = query_check.where(column(key) == value)
    return query_check


def get_the_pagination_search_list(
    query_str: object,
    all_params: dict(),
    sort_params: dict(),
    default_sort_value: any,
) -> object:
    query_check = query_str
    n = len(all_params)
    idx = []
    for i in range(0, n):
        if list(all_params.values())[i] != None:
            idx.append(i)
    if idx != None:
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            if key != "is_active":
                query_check = query_check.where(column(key).contains(value))
            else:
                query_check = query_check.where(column(key)==value)  
    query_check =SortDataList(query_check,sort_params,default_sort_value)
    return query_check


# catatan untuk function get_the_pagination_search_with_join:
# di join_tables nya di dalam listnya main table harus di index pertama
def get_the_pagination_search_with_join(
    query_str: object, all_params: dict, main_table: object, join_tables: list
) -> object:
    query_check = query_str
    n = len(all_params)
    idx = []
    for i in range(n):
        if all_params.get(list(all_params.keys())[i]) is not None:
            idx.append(i)
    if idx != None:
        for j in idx:
            key = list(all_params.keys())[j]
            value = list(all_params.values())[j]
            key_column = None
            for table in join_tables:
                if key in [column.name for column in table.__table__.columns]:
                    key_column = getattr(table, key)
                    break
            if not key_column:
                key_column = getattr(main_table, key)
            query_check = query_check.where(key_column == value)
    return query_check


def get_the_pagination_search_list_with_join(
    db: Session, query_str: object, all_params: dict, tables: list
) -> object:
    query_check = query_str
    counter = len(db.scalars(query_check).all())
    n = len(all_params)
    idx = []
    for i in range(0, n):
        if list(all_params.values())[i] != None:
            idx.append(i)
    if idx != None:
        for j in range(len(idx)):
            key = list(all_params.keys())[idx[j]]
            value = list(all_params.values())[idx[j]]
            key_column = None
            for table in tables:
                if key in [column.name for column in table.__table__.columns]:
                    key_column = getattr(table, key)
                    break
            if not key_column:
                key_column = getattr(table, key)

            if key != "is_active":
                query_check = query_check.where(key_column.contains(value))
            else:
                query_check = query_check.where(key_column == value)
    return query_check, counter