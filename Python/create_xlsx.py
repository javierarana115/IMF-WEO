import sdmx
import pandas as pd
from openpyxl import Workbook
import io

BASE_ULR = "https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.RES/WEO/6.0.0/"

IMF_DATA = sdmx.Client("IMF_DATA")
data_msg = IMF_DATA.data("WEO", key="USA+BRA+DEU+ZAF+IND.PCPIPCH+NGDP_RPCH", params={"startPeriod": 2015, "endPeriod": 2024})

weo_series  = sdmx.to_pandas(data_msg)
weo_df = weo_series.reset_index()


# weo_df = weo_df.drop(columns=['LATEST_ACTUAL_ANNUAL_DATA', 'OVERLAP', 'METHODOLOGY_NOTES', 'METHODOLOGY'])

weo_df.columns = weo_df.columns.str.lower()

df_wide = weo_df.pivot_table(
    index=['country', 'time_period'],
    columns='indicator',
    values='value'
).reset_index()

country_name_map = {
    'USA': 'United States',
    'BRA': 'Brazil',
    'DEU': 'Germany',
    'ZAF': 'South Africa',
    'IND': 'India'
}

df_wide['country'] = df_wide['country'].replace(country_name_map)
df_wide = df_wide.rename(columns={
    'NGDP_RPCH': 'GDP_Growth',
    'PCPIPCH': 'Inflation',
    'time_period': 'Year'
})

df_wide['Year'] = df_wide['Year'].astype(int)

df_wide.to_excel('IMF_WEO_data.xlsx', index=False)