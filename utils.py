import pandas as pd
from types_def import Factor


def get_all_instrument_name_list() -> list[str]:
    return [f"UBIQ{str(idx).zfill(3)}.csv" for idx in range(0, 50)]


def get_all_day_index_list() -> list[int]:
    return [i for i in range(0, 60)]


def get_base_factor_list() -> list[Factor]:
    return [f for f in Factor]


def load_data(instrument_name_list: list[str] = None, day_index_list: list[int] = None) -> dict[str, dict[int, pd.DataFrame]]:
    if instrument_name_list is None:
        instrument_name_list = get_all_instrument_name_list()
    if day_index_list is None:
        day_index_list = get_all_day_index_list()

    result = {}
    for instrument_name in instrument_name_list:
        result[instrument_name] = {}
        for day_index in day_index_list:
            result[instrument_name][day_index] = pd.read_csv(f"data/snapshots/{day_index}_{instrument_name}.csv", sep='|')
    return result
