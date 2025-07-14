import pandas as pd
import toolz as fp


@fp.curry
def filter_columns_by_correlation_threshold(
    df: pd.DataFrame,
    ref_col: str,
    method_type: str = "person",
    lower_threshold: float = 0.001,
    higher_threshold: float = 0.999,
):
    corr = df.corr(method=method_type)
    corr_ref = corr[ref_col].abs().sort_values(ascending=False)
    col_list = corr_ref[
        (corr_ref <= lower_threshold) | (corr_ref >= higher_threshold)
    ].index.to_numpy()

    col_list = [i for i in col_list if ref_col != i]

    df = df.drop(columns=col_list)

    return df
