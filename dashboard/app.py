import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

day_df = pd.read_csv('../dataset/day.csv')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

st.title('Bike Rentals Dashboard')

st.subheader('Bike Rentals Over Time')

# Mengelompokkan data berdasarkan tanggal dan menghitung total peminjaman (cnt)
time_series_df = day_df.groupby('dteday')['cnt'].sum().reset_index()
time_series_df.columns = ['Date', 'Total Bike Rentals']

st.write('Tabel Perkembangan Peminjaman Sepeda:')
st.dataframe(time_series_df)

st.line_chart(data=time_series_df.set_index('Date')['Total Bike Rentals'], width=0, height=0)

st.subheader('Average Bike Rentals by Weather Condition')

weather_labels = {
    1: 'Partly Cloudy',
    2: 'Mist + Cloudy',
    3: 'Light Rain / Light Snow',
    4: 'Heavy Rain'
}

# Mengelompokkan data berdasarkan kondisi cuaca dan menghitung rata-rata peminjaman sepeda
weather_avg = day_df.groupby('weathersit')['cnt'].mean()

weather_avg_complete = pd.DataFrame({
    'Weather Condition': ['Partly Cloudy', 'Mist + Cloudy', 'Light Rain / Light Snow', 'Heavy Rain'],
    'Average Bike Rentals': [weather_avg.get(i, 0) for i in range(1, 5)]
})

st.write('Tabel Rata-rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca:')
st.dataframe(weather_avg_complete)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(weather_avg_complete['Weather Condition'], weather_avg_complete['Average Bike Rentals'], color='#D53A94')

ax.set_title('Average Bike Rentals by Weather Condition')
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Average Bike Rentals')
plt.xticks(rotation=45)

st.pyplot(fig)
