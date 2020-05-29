import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1lec9VOr8N3kHUlUFCbAdO3PKGhk_i62Myw_B6N4c3jk/export?gid=0&format=csv', names=['Source', 'Date', 'Amount'])
groups = df.groupby('Source')

# fig, ax = plt.subplots(figsize=(20,5))
# for name, group in groups:
    # ax.plot(pd.to_datetime(group['Date']), group['Amount'], marker='o', linestyle='', label=name)
# ax.legend()
# plt.show()

total_by_group = df.groupby('Source').sum()

total = df['Amount'].sum()

f = open('README.md', 'w')
f.write('# AmazonGC\n')
f.write('\n```\n')
f.write(f'{total_by_group.to_string()}')
f.write('\n```\n\n')
f.write(f'${total}\n\n')
f.write(f'https://stackoverflow.com/questions/19611729/getting-google-spreadsheet-csv-into-a-pandas-dataframe\n')
f.write(f'https://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category\n')
f.write(f'https://stackoverflow.com/questions/38256750/make-a-scatter-plot-in-matplotlib-with-dates-on-x-axis-and-values-on-y\n')
f.close()
