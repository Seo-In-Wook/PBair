import streamlit as st
import pandas as pd

st.set_page_config(
	page_title='Streamlit 프로토타입 만들기',
	page_icon='🎈',
	layout='wide'
)

st.text('🎈서인욱 : Streamlit 프로토타입 만들기')

st.title('📌PB 리포트 업무 자동화 프로그램 인공지능 리테일 AIR.')

st.header('Header(머리글)을 입력하세요.')
st.subheader('Subheader(세부 머리글)을 입력하세요.')

st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')

st.markdown('1. 하나')
st.markdown('2. 둘')
st.markdown('3. 셋')

st.caption('이것은 Caption 입니다.')

st.text('기본 텍스트를 입력합니다.')
st.code('코드 블록 표시가 가능합니다.')


stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)

st.dataframe(df_stocks)
st.dataframe(df_index.style.highlight_max(axis=0))

#Select_list

symbol = st.selectbox('AAPL', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

#multiselect('AAPL', (df_stocks['Symbol'].unique()))
#stokcs[df_stocks['Symbol'].isin(symbol_list)))

st.line_chart(df_index, x='Date')

df_chart = pd.DataFrame(columns=['Date'])
df_chart['Date'] = df_stocks['Date'].unique()

for symbol in df_stocks['Symbol'].unique():
	df_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)
#reset index ?

st.line_chart(df_chart, x='Date')

#st_bar_chart(df_chart.tal(30), x='data')

symbol_list = st.multiselect('AAPL', (df_stocks['Symbol'].unique()), default='AAPL')
symbol_list.insert(0, 'Date')

st.line_chart(df_chart[symbol_list], x='Date')

