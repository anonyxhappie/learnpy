import pandas as pd
import math


def get_required_dataframe(url):
    tables = pd.read_html(url)
    
    df = tables[0]
    df = df.rename(columns={0: 'iata', 2: 'airport', 3: 'locations'})
    
    del df[1]
    if url[-1] < 'N':
        del df[4]
        del df[5]
    for index, i in enumerate(df['locations']):
        if type(i) == float and math.isnan(i):
            df.drop(index, inplace=True)

    cities = []
    countries = []
    for index, i in enumerate(df['locations']):
        location_array = i.split(',')
        cities.append(location_array[0])
        if len(location_array) == 2:
            countries.append(location_array[1])
        elif len(location_array) == 3:
            countries.append(location_array[2])
        else:
            countries.append(location_array[0])
    df = df.assign(city=cities, country=countries)

    del df['locations']
    df.drop(df.index[:1], inplace=True)
    return df

def get_airport_dataframe():
    final_df = None
    for i in range(65, 91):
        print(chr(i))
        url = r'https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_' + chr(i)

        df_a = get_required_dataframe(url)
        if i > 65:
            final_df = pd.concat([final_df, df_a])
        else:
            final_df = df_a

    final_df = final_df.reset_index(drop=True)
    
    return final_df

def get_df_from_csv():
    return pd.read_csv('air_df.csv')

# print(get_airport_dataframe())

# df = get_airport_dataframe()
# df.to_csv('air_df.csv', sep='\t', encoding='utf-8')

print(get_df_from_csv())
