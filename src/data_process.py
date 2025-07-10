import pandas as pd
import toolz as fp


@fp.curry
def filter_columns_by_correlation_threshold(
    df: pd.DataFrame,
    ref_col: str,
    method: str = "person",
    lower_threshold: float = 0.999,
    higher_threshold: float = 0.001,
):
    corr = df.corr(method=method)
    corr_ref = corr[ref_col].abs().sort_values(ascending=False)
    col_list = corr_ref[
        (corr_ref <= lower_threshold) | (corr_ref >= higher_threshold)
    ].index.to_numpy()

    df = df.drop(columns=col_list)

    return df
