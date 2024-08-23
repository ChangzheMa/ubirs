import pandas as pd

from types_def import Factor
from utils import load_data
from factor_utils import cal_base_factor


if __name__ == '__main__':
    data_obj: dict[str, dict[int, pd.DataFrame]] = load_data(['UBIQ000'])
    data_list: list[pd.DataFrame] = [df for df_obj in data_obj.values() for df in df_obj.values()]

    cal_base_factor(data_list)
    # factor_name = cal_factor(data_list)
    factor_name = Factor.Vwap_Return3.value
    test_factor(data_obj, factor_name)
    # TODO
