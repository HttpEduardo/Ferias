import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACdb615e894e5ca87d26246797f8707d4e"
# Your Auth Token from twilio.com/console
auth_token  = "45f31103954859dfa4a0c6f1f96163e6"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            #to="tirar o comentario e colocar o seu numero ou um numero valido",
            from_="+14156341438",
            body=f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

