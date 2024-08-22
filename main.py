from utils import load_data
import pandas as pd


if __name__ == '__main__':
    data_obj: dict[str, dict[int, pd.DataFrame]] = load_data(['UBIQ005'], [0, 1])
    data_list: list[pd.DataFrame] = [df for df_obj in data_obj.values() for df in df_obj.values()]

    print(data_list)
