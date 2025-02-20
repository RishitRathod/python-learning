import pandas as pd
from sqlalchemy import create_engine
data = {
    'CHN': {'COUNTRY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96,
            'GDP': 12_234.78, 'CONT': 'Asia'},
    'IND': {'COUNTRY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26,
            'GDP': 2_575.67, 'CONT': 'Asia', 'IND_DAY': '1947-08-15'},
    'USA': {'COUNTRY': 'US', 'POP': 329.74, 'AREA': 9_833.52,
            'GDP': 19_485.39, 'CONT': 'N.America',
            'IND_DAY': '1776-07-04'},
    'IDN': {'COUNTRY': 'Indonesia', 'POP': 268.07, 'AREA': 1_910.93,
            'GDP': 1_015.54, 'CONT': 'Asia', 'IND_DAY': '1945-08-17'},
    'BRA': {'COUNTRY': 'Brazil', 'POP': 210.32, 'AREA': 8_515.77,
            'GDP': 2_055.51, 'CONT': 'S.America', 'IND_DAY': '1822-09-07'},
    'PAK': {'COUNTRY': 'Pakistan', 'POP': 205.71, 'AREA': 881.91,
            'GDP': 302.14, 'CONT': 'Asia', 'IND_DAY': '1947-08-14'},
    'NGA': {'COUNTRY': 'Nigeria', 'POP': 200.96, 'AREA': 923.77,
            'GDP': 375.77, 'CONT': 'Africa', 'IND_DAY': '1960-10-01'},
    'BGD': {'COUNTRY': 'Bangladesh', 'POP': 167.09, 'AREA': 147.57,
            'GDP': 245.63, 'CONT': 'Asia', 'IND_DAY': '1971-03-26'},
    'RUS': {'COUNTRY': 'Russia', 'POP': 146.79, 'AREA': 17_098.25,
            'GDP': 1_530.75, 'IND_DAY': '1992-06-12'},
    'MEX': {'COUNTRY': 'Mexico', 'POP': 126.58, 'AREA': 1_964.38,
            'GDP': 1_158.23, 'CONT': 'N.America', 'IND_DAY': '1810-09-16'},
    'JPN': {'COUNTRY': 'Japan', 'POP': 126.22, 'AREA': 377.97,
            'GDP': 4_872.42, 'CONT': 'Asia'},
    'DEU': {'COUNTRY': 'Germany', 'POP': 83.02, 'AREA': 357.11,
            'GDP': 3_693.20, 'CONT': 'Europe'},
    'FRA': {'COUNTRY': 'France', 'POP': 67.02, 'AREA': 640.68,
            'GDP': 2_582.49, 'CONT': 'Europe', 'IND_DAY': '1789-07-14'},
    'GBR': {'COUNTRY': 'UK', 'POP': 66.44, 'AREA': 242.50,
            'GDP': 2_631.23, 'CONT': 'Europe'},
    'ITA': {'COUNTRY': 'Italy', 'POP': 60.36, 'AREA': 301.34,
            'GDP': 1_943.84, 'CONT': 'Europe'},
    'ARG': {'COUNTRY': 'Argentina', 'POP': 44.94, 'AREA': 2_780.40,
            'GDP': 637.49, 'CONT': 'S.America', 'IND_DAY': '1816-07-09'},
    'DZA': {'COUNTRY': 'Algeria', 'POP': 43.38, 'AREA': 2_381.74,
            'GDP': 167.56, 'CONT': 'Africa', 'IND_DAY': '1962-07-05'},
    'CAN': {'COUNTRY': 'Canada', 'POP': 37.59, 'AREA': 9_984.67,
            'GDP': 1_647.12, 'CONT': 'N.America', 'IND_DAY': '1867-07-01'},
    'AUS': {'COUNTRY': 'Australia', 'POP': 25.47, 'AREA': 7_692.02,
            'GDP': 1_408.68, 'CONT': 'Oceania'},
    'KAZ': {'COUNTRY': 'Kazakhstan', 'POP': 18.53, 'AREA': 2_724.90,
            'GDP': 159.41, 'CONT': 'Asia', 'IND_DAY': '1991-12-16'}
}
columns = ('COUNTRY', 'POP', 'AREA', 'GDP', 'CONT', 'IND_DAY')

engine =create_engine('sqlite:///data2.db',echo=False)
dtype={'POP':'float64','AREA':'float64','GDP':'float64','IND_DAY':'datetime64[ns]'}
df=pd.DataFrame(data=data,index=columns).T.astype(dtype=dtype)
# print(df.dtypes)
# df.to_sql('data.db',con=engine,index_label='ID')

# df = pd.DataFrame(data=data).T
# print(df)

# df = pd.DataFrame(data=data, index=columns).T
# print(df)

# df.to_csv('data.csv')


# # df = pd.read_csv('data.csv', index_col=0)
# # print(df)

df.to_excel("data.xlsx")

df = pd.read_excel('data.xlsx', index_col=0)
print(df)



# s = df.to_csv()
# print(s)

# df.loc['RUS', 'CONT']

# df.to_csv('new-data.csv', na_rep='(missing)')

# a=pd.read_csv('new-data.csv', index_col=0, na_values='(missing)')
# print(a)

# df = pd.read_csv('data.csv', index_col=0)
# df.dtypes



# df = pd.DataFrame(data=data).T
# df.to_json('data-columns.json')
# df.to_json('data-index.json', orient='index')
# df.to_json('data-records.json', orient='records')
# df.to_json('data-split.json', orient='split')
# df = pd.DataFrame(data=data).T
# df['IND_DAY'] = pd.to_datetime(df['IND_DAY'])
# print(df.dtypes)
# df = pd.DataFrame(data=data).T
# df['IND_DAY'] = pd.to_datetime(df['IND_DAY'])
# df.to_json('new-data-time.json', date_format='iso', date_unit='s')
# df = pd.read_json('data-index.json', orient='index',convert_dates=['IND_DAY'])

# df = pd.DataFrame(data=data).T
# # df.to_html('data.html')
# df = pd.read_html('data.html', index_col=0, parse_dates=['IND_DAY'])




# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///data.db', echo=False)
# dtypes = {'POP': 'float64', 'AREA': 'float64', 'GDP': 'float64','IND_DAY': 'datetime64'}
# df = pd.DataFrame(data=data).T.astype(dtype=dtypes)
# print(df.dtypes)
# df.to_sql('data.db', con=engine, index_label='ID')