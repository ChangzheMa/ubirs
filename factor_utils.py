import pandas as pd
import numpy as np
import re
from types_def import Factor
from utils import get_base_factor_list


return_pattern = r'^.*_Return\d+$'


def cal_factor_for_df(df: pd.DataFrame, factor: Factor):
    if factor == Factor.Vwap:
        df[Factor.Vwap.value] = (df['TotalTradeValue'] - df['TotalTradeValue'].shift(1)) / (df['TotalTradeVolume'] - df['TotalTradeVolume'].shift(1))

    elif factor == Factor.BalancePrice1:
        df[Factor.BalancePrice1.value] = (df['AskPrice1'] * df['BidVolume1'] + df['BidPrice1'] * df['AskVolume1']) / (df['AskVolume1'] + df['BidVolume1'])

    elif factor == Factor.BalancePrice2:
        total_ask_volume = df['AskVolume1'] + df['AskVolume2']
        total_bid_volume = df['BidVolume1'] + df['BidVolume2']
        df[Factor.BalancePrice2.value] = (((df['AskPrice1'] * df['AskVolume1'] + df['AskPrice2'] * df['AskVolume2']) * total_bid_volume / total_ask_volume +
                                     (df['BidPrice1'] * df['BidVolume1'] + df['BidPrice2'] * df['BidVolume2']) * total_ask_volume / total_bid_volume)
                                    / (total_ask_volume + total_bid_volume))

    elif re.match(return_pattern, factor.value):
        [base_key, pro_key] = factor.value.split('_')
        return_step = int(pro_key[6:])
        df[factor.value] = (df[base_key].shift(-return_step) - df[base_key]) / df[base_key]


def cal_base_factor(data_list: list[pd.DataFrame], factor_list: list[str] = None, filna: bool = True):
    if factor_list is None:
        factor_list = get_base_factor_list()

    for df in data_list:
        for factor in factor_list:
            cal_factor_for_df(df, factor)
            if filna:
                df.replace([np.inf, -np.inf], 0, inplace=True)
                df.fillna(0, inplace=True)


def test_factor(data_obj: dict[str, dict[int, pd.DataFrame]], factor_name: str, base_name: str = "Vwap_Return5"):
    data_list: list[pd.DataFrame] = [df for df_obj in data_obj.values() for df in df_obj.values()]
    # TODO
