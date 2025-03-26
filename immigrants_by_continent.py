import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

continents = ['Africa', 'Asia', 'North America', 'South America', 'Europe', 'Australia']

df = pd.read_csv('refuges.csv', skiprows=1)
df = df.drop(['Region/Country/Area', 'Footnotes', 'Source'], axis=1)
print(df.columns)

df = df[df['Series'] == 'International migrant stock: Both sexes (number)']
df = df.drop('Series', axis =1)

df = df.rename(columns={'Unnamed: 1': 'Region'})
df = df[df['Region'].isin(continents)]


df['Value'] = df['Value'].str.replace(',', '').astype(float)
df['Year'] = df['Year'].astype(int)
plt.figure(figsize=(10, 6))

for region in df['Region'].unique():
    region_data = df[df['Region'] == region]
    plt.plot(region_data['Year'], region_data['Value'], label=region)  # Line
    plt.scatter(region_data['Year'], region_data['Value'])             # Points

plt.xlabel('Year')
plt.ylabel('International migrant stock: Both sexes (number)')
plt.title('Value Over Time by Region')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
plt.legend()
plt.grid(True)
plt.tight_layout()


plt.savefig("immigrants.png", dpi=300, bbox_inches='tight')
plt.show()

