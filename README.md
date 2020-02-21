ANÁLISE BASE DE DADOS - INTRODUÇÃO
1. O projeto foi desenvolvido utilizando o Python 3.7 no Windows 10 (64 bits)
2. Os dados analisados foram extraídos do arquivo sms_senior.csv

REQUISITOS
python 3.7
pip 19.3.1
virtualenv 16.7.9
matplotlib 3.1.3
pandas 1.0.1

INSTALANDO O PYTHON
1. Guias de instalação:
	Windows: https://python.org.br/instalacao-windows/
	Linux: https://python.org.br/instalacao-linux/
	MAC OS: https://python.org.br/instalacao-mac/
	
2. Instalação Virtualenv: 
	pip install virtualenv

DOWNLOAD DO CÓDIGO
 git clone https://github.com/caroline-salvador/plot.git

AMBIENTE VIRTUAL
1. No terminal, navege até a pasta do projeto
2. Crie um ambiente virtual na pasta raiz do projeto executando o comando:
	virtualenv venv
3. Ative o ambiente virtual usando o comando:
	souce venv/bin/activate (Linux ou macOS)
	venv/Scripts/activate (Windows)
4. Instale as dependências:
	pip install -r requirements.txt

EXECUTANDO O PROJETO
1. Com a venv ativada, execute o script:
	python plot.py
2. O script vai gerar arquivos de imagens com os gráficos na pasta do script
