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

1. Pandas DataFrame - primārā datu struktūra, kas glabā visus darījumu ierakstus ar kolonnām:
Datums
Kategorija
Summa

2. Vārdnīcas (dictionaries) - kategoriju un krāsu pārvaldībai:
   color_dict = {
    'Pārtika': '#1f77b4',
    'Transports': '#ff7f0e'
}
3. NumPy masīvi - krāsu gradientu veidošanai:
colors = np.linspace(0, 1, num=len(categories))

4. Grupēti dati (GroupBy objekti) - starprezultātu glabāšanai:
month_group = month_data.groupby('Kategorija')['Summa'].sum()

   Algoritmiski projekts izmanto:
- Datumu parsēšanu un grupēšanu pa mēnešiem
- Automātisku grafiku izkārtojuma aprēķinu
- Procentuālo daļu aprēķinu izdevumu kategorijām

   Lietošanas instrukcija
1. Sagatavot darījumu datus CSV failā ar kolonnām:
- Datums (formātā MM-DD)
- Kategorija
- Summa (EUR)

2. Palaist skriptu, kas:
Ielādē datus, analizē izdevumu sadalījumu pa mēnešiem, ģenerē kūku diagrammas katra mēneša izdevumiem, izvada kopsavilkuma statistiku.

   Rezultāti:
- Vizualizācija izdevumu sadalījumam
- Mēneša kopējo izdevumu summa
- Vidējā darījuma summa
- Dārgākā mēneša identificēšana
