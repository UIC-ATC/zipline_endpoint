from datetime import datetime

import numpy as np
import pandas as pd
import pandas_datareader.data as pd_reader
from dateutil.relativedelta import relativedelta


def get_benchmark_returns(symbol):
    """
    Get a Series of benchmark returns from Yahoo associated with `symbol`.
    Default is `SPY`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.

    The data is provided by Yahoo Finance
    """
    data = pd_reader.DataReader(
        symbol,
        'yahoo',
        datetime.now() - relativedelta(years=5),
        datetime.now()
    )

    data = data['Close']

    data = data.fillna(method='ffill')

    return data.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
