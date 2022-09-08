import numpy as np
import pandas as pd

def adjust_df_for_inflation(df, column, new_column_name, inflation_index):
    """
    Takes a pandas dataframe containing two columns: one with values to be adjusted and another one containing the inflation index and applie a correction for inflation.
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    column : str
        The name of the column containing the values to be adjusted.
    new_column_name : str
        The name for the newly created column
    inflation_index : str
         The name of the column containing the inflation index.
    Returns
    -------
    pandas.core.frame.DataFrame
        Returns a dataframe with a new column containing the adjusted value.
    Example
    -------
    import numpy as np
    import pandas as pd
    historical_salary =np.random.normal(loc = 50000, scale=2.0, size=10)
    cpi_index = np.array([96.1, 98.5, 100.0, 100.0, 100.7,
                 103.4, 105.9, 107.8, 108.7, 111.6])
    df = pd.DataFrame({'historical_salary': historical_salary, 'cpi_index':cpi_index})
    df_adjusted = adjust_df_for_inflation(df, 'historical_salary', 'adjusted_salary', 'cpi_index')
    """
    df[new_column_name] = df[column] * df[inflation_index] / 100
    return df









