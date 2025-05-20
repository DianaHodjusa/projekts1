Finanšu izdevumu analizators

Projekta apraksts
Šis projekts ir paredzēts personīgo finansu pārvaldībai un izdevumu analīzei. Programma apstrādā jUsu izdevumus, sagrupē tos pa kategorijām un mēnešiem, kā arī vizualizē izdevumu sadalījumu izmantojot dažādus grafikus.

Galvenās funkcijas:
- Darījumu ielāde no CSV faila
- Automātiska datu kategorizācija
- Izdevumu analīze pa mēnešiem
- Vizualizācija ar interaktīviem grafikiem
- Detalizēta mēnešu statistika

Izmantotās Python bibliotēkas
1. **Pandas** - galvenā bibliotēka datu analīzei:
   - Datu ielāde no CSV failiem
   - Datu filtrēšana un grupēšana
   - Agregācijas funkcijas (summēšana, vidējā vērtība u.c.)

2. **Matplotlib** - datu vizualizācijai:
   - Kūku diagrammu veidošana
   - Diagrammu formatēšana un pielāgošana
   - Datu attēlošana strukturētā formā

3. **NumPy** - matemātiskām operācijām:
   - Datu masīvu apstrāde
   - Palīgfunkcijas grafiku veidošanai
   - Skaitlisko vērtību ģenerēšana

4. **Math** - pamata matemātiskām funkcijām:
   - Aprēķiniem grafiku izkārtojumam
   - Noapaļošanas operācijām

Projekta datu struktūras
Projekta izstrādē tiek izmantotas šādas galvenās datu struktūras:

1. Pandas DataFrame - galvenā datu struktūra:
   ```python
  df = pd.DataFrame({
       'Datums': ['01-01', '01-02'],
       'Kategorija': ['Pārtika', 'Transports'],
       'Summa': [15.50, 5.20]
   })
2. Vārdnīcas (dictionaries) - kategoriju un krāsu pārvaldībai:
   color_dict = {
    'Pārtika': '#1f77b4',
    'Transports': '#ff7f0e'
}
3. NumPy masīvi - krāsu gradientu veidošanai:
colors = np.linspace(0, 1, num=len(categories))

4. Sarindotas vērtības (Series) - starprezultātu glabāšanai:
monthly_totals = df.groupby('Mēnesis')['Summa'].sum()






