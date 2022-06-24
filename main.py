from datetime import datetime
import instaloader
from getpass import getpass
l = instaloader.Instaloader()
nome = input('Digite seu Login: ')
psw = getpass('Digite sua Senha: ')

l.login(nome, psw)
perfil = input('Digite o nome do perfil: ')
posts = instaloader.Profile.from_username(l.context, perfil).get_posts()
print('Selecione um periodo entre as datas: ')
diai = int(input('De dia: '))
mesi = int(input('Mês: '))
anoi = int(input('Ano: '))
diaf = int(input('Até dia: '))
mesf = int(input('Mês: '))
anof = int(input('Ano: '))
since = datetime(anoi, mesi, diai)
until = datetime(anof, mesf, diaf)

for posts in posts:
        if(posts.date >= since) and (posts.date <= until):
            print(posts.date)
            l.download_post(posts, 'insta-posts-downloads')

