import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
df = pd.read_csv('MoneyTracker/transactions_latvia.csv')

categories = df['Kategorija'].unique()
print(f"Kopā kategorijas: {len(categories)}")
print("Kategoriju saraksts:", ', '.join(categories))

n_categories = len(categories)
colors = plt.cm.tab20(np.linspace(0, 1, n_categories))
color_dict = dict(zip(categories, colors))

months = df['Datums'].str.split('-').str[0].unique()
n_months = len(months)

n_cols = math.ceil(math.sqrt(n_months))
n_rows = math.ceil(n_months / n_cols)

plt.figure(figsize=(5 * n_cols, 5 * n_rows))

for i, month in enumerate(months, 1):
    month_data = df[df['Datums'].str.startswith(month)]
    month_total = month_data['Summa'].sum()
    
    plt.subplot(n_rows, n_cols, i)
    
    month_group = month_data.groupby('Kategorija')['Summa'].sum()
    current_colors = [color_dict[cat] for cat in month_group.index]
    
    month_group.plot(
        kind='pie',
        autopct=lambda p: f'{p:.1f}% ({p*month_total/100:.2f}€)',
        colors=current_colors,
        startangle=90,
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
    )
    plt.title(f'Izdevumi par {month}. mēnesi (Kopā: {month_total:.2f}€)')
    plt.ylabel('')

plt.tight_layout()
plt.show()

monthly_stats = df.copy()
monthly_stats['Month'] = monthly_stats['Datums'].str.split('-').str[0]
monthly_stats = monthly_stats.groupby('Month').agg(
    Total_Spending=('Summa', 'sum'),
    Avg_Transaction=('Summa', 'mean'),
    Transaction_Count=('Summa', 'count')
).reset_index()

max_month = monthly_stats.loc[monthly_stats['Total_Spending'].idxmax()]
print("\nMēnešu statistika:")
print(monthly_stats.to_string(index=False))
print(f"\nDārgākais mēnesis: {max_month['Month']} (Kopējie izdevumi: {max_month['Total_Spending']:.2f}€)")