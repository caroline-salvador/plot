import csv
import pandas as pd
import matplotlib.pyplot as plt

class Plot():
	def __init__(self):
		self.df = pd.read_csv('sms_senior.csv', encoding='ISO-8859-1')  
		
		self.plot1()
		self.plot2()
		self.plot3()
		self.plot4()

	def plot1(self):
		sum_words=self.df.sum()
		words=sum_words[1:len(sum_words)-5].sort_values(ascending=False)
		words[0:20].plot.bar()
		plt.savefig('palavras_mais_frequentes.png')
		print("O gráfico palavras mais frequentes foi gerado com sucesso")
		#plt.show()
		return

	def plot2(self):
		self.df["Month"]=self.df['Date'].astype('datetime64')
		self.df['Month']=self.df['Month'].map(lambda x: str(x.year) +"/"+ str(x.month))
		self.df.groupby(['Month','IsSpam']).size().unstack().plot.bar(rot=0)
		plt.savefig('quantidade_mensal_mensagens.png')
		print("O gráfico quantidade mensal de mensagens foi gerado com sucesso")
		#plt.show()
		return
		
	def plot3(self):
		group=self.df.groupby(['Month'])[['Word_Count']].mean().rename(columns={'Word_Count': 'Mean'})
		group['Median']=self.df.groupby(['Month'])['Word_Count'].median()
		group['Standard Deviation']=self.df.groupby(['Month'])['Word_Count'].std()
		group['Variance']=self.df.groupby(['Month'])['Word_Count'].var()
		group['Max']=self.df.groupby(['Month'])['Word_Count'].max()
		group['Min']=self.df.groupby(['Month'])['Word_Count'].min()
		group.plot.bar(rot=0)
		plt.savefig('estatistica_total_palavras_mensal.png')
		print("O gráfico estatísticas com o total de palavras foi gerado com sucesso")
		#plt.show()
		return
		
	def plot4(self):
		self.df['Days']=self.df['Date'].astype('datetime64')
		self.df['Days']=self.df['Days'].map(lambda x: str(x.day) +"/"+ str(x.month))

		self.df['Month']=self.df['Date'].astype('datetime64')
		self.df['Month']=self.df['Month'].map(lambda x: str(x.month))

		df1=self.df[self.df['IsSpam'] == 'no']
		group=df1.groupby(['Month', 'Days'])[['IsSpam']].count().rename(columns={'IsSpam': 'Amount e-mail'})
		group=group.groupby('Month')[['Amount e-mail']].max()

		group.plot.bar(rot=0)
		plt.savefig('quantidade_mensagens_comum.png')
		print("O gráfico quantidade mensagens comuns foi gerado com sucesso")
		#plt.show()
		return

if __name__ == '__main__':
	try:
		Plot()
		print("Gráficos gerados. As imagens estão salvas na pasta do script Python")
	except Exception as error:
		print("Erro ao gerar os gráficos: {0}".format(str(error)))
		

