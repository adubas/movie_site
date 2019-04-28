# coding: utf-8
from __future__ import print_function, unicode_literals

"""importando os arquivos de python que servem de base para formatação desse projeto."""
import fresh_tomatoes
import media

"""Tema do site de trailers é apresentar os filmes da Marvel em ordem cronológica,
 não na ordem que foram lançados, mas em qual período eles se encontram na timelime do universo Marvel.
 
 Segue a listagem já modelada para uso do media.py."""
cap_1 = media.Movie('Capitão América: o primeiro vingador', 'A história de Steve Rogers, o primeiro vingador.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/d/d8/Capit%C3%A3o_Am%C3%A9rica_O_Primeiro_Vingador_-_Poster.jpg/250px-Capit%C3%A3o_Am%C3%A9rica_O_Primeiro_Vingador_-_Poster.jpg', r'https://www.youtube.com/watch?v=JerVrbLldXw&t=4s')
iron_man = media.Movie('Homen de Ferro', 'Siga a jornada do gênio bilionário Tony Stark, enquanto ele se torna o Homem de Ferro.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/0/00/Iron_Man_poster.jpg/250px-Iron_Man_poster.jpg', r'https://www.youtube.com/watch?v=8hYlB38asDY')
hulk = media.Movie('O Incrível Hulk', 'Veja como o Dr. Bruce Barne lida com sou outra personalidade, o poderoso Hulk.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/1/1b/The_Incredible_Hulk.jpg/250px-The_Incredible_Hulk.jpg', r'https://www.youtube.com/watch?v=xbqNb2PFKKA&t=41s')
iron_man_2 = media.Movie('Homen de Ferro 2', 'Continue a jornada do Tony enquanto outra ameaça surge.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/9/9a/Homem_de_Ferro_2_-_Poster.jpg/250px-Homem_de_Ferro_2_-_Poster.jpg', r'https://www.youtube.com/watch?v=DIfgxIv5xmk&t=54s')
thor_1 = media.Movie('Thor', 'Descubra a existência dos Deus da mitologia nórdica.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/9/9f/Thor_Poster.jpg/250px-Thor_Poster.jpg', r'https://www.youtube.com/watch?v=JOddp-nlNvQ&t=18s')
avengers_1 = media.Movie('Os Vingadores', 'Acompanhe enquanto um grupo de humanos super-poderosos e o Thor enfrentam Loki, o Deus da Trapaça e irmão do Thor.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/6/69/The_Avengers_Cartaz.jpg/250px-The_Avengers_Cartaz.jpg', r'https://www.youtube.com/watch?v=eOrNdBpGMv8')
iron_man_3 = media.Movie('Homem de Ferro 3', 'Veja Tony Stark enfrentar um grupo.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/1/19/Iron_Man_3_poster.jpg/250px-Iron_Man_3_poster.jpg', r'https://www.youtube.com/watch?v=f_h95mEd4TI')
thor_2 = media.Movie('Thor: Mundo Sombrio', 'Acompanhe Thor e Loki enquanto eles tentam vingar a morte da mãe.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/0/00/Thor1.jpg/255px-Thor1.jpg', r'https://www.youtube.com/watch?v=npvJ9FTgZbM')
cap_2 = media.Movie('Capião América: Soldado Invernal', 'Steve descobre que seu amigo "Bucky" está vivo e foi transformado em uma arma nas mãos do inimigo.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/e/e8/Captain_America_The_Winter_Soldier.jpg/250px-Captain_America_The_Winter_Soldier.jpg', r'https://www.youtube.com/watch?v=tbayiPxkUMM&t=11s')
guardians_1 = media.Movie('Guardiões da Galáxia', 'Junte-se à Peter Quill enquanto ele força uma aliança com Rocket, Groot, Gamora e Drax, para impedir que uma jóia do infinito caia nas mãos erradas.', r'https://upload.wikimedia.org/wikipedia/pt/b/b2/Guardiansgalaxyposter.jpg', r'https://www.youtube.com/watch?v=d96cjJhvlMA&t=11s')
guardians_2 = media.Movie('Guardiões da Galáxia, vol. 2', 'Acompanhe os guardiões em sua jornada para descobrir a origem do Star Lord.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/0/07/Guardians_of_the_galaxy_vol_two_poster.jpg/250px-Guardians_of_the_galaxy_vol_two_poster.jpg', r'https://www.youtube.com/watch?v=dW1BIid8Osg&t=8s')
avengers_2 = media.Movie('Os Vingadores: Era de Ultron', 'Os protetores da Terra entram em ação novamente, dessa vez a ameaça é um programa criado pelo próprio Tony.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/2/22/OsVingadores2.jpg/250px-OsVingadores2.jpg', r'https://www.youtube.com/watch?v=tmeOjFno6Do&t=1s')
ant_1 = media.Movie('Homem-Formiga', 'Descobra o mais novo super-heroí Scoot Lang, um ex-presidiário que, com a ajuda de Hank Pym se torna o Homem-Formiga.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/9/90/Ant_Man-Poster.jpg/250px-Ant_Man-Poster.jpg', r'https://www.youtube.com/watch?v=pWdKf3MneyI')
cap_3 = media.Movie('Capitão América: Guerra Civil', 'Os heróis da Terra se dividem após a criação do acordo de Sokovia, veja a guerra entre Homem de Ferro contra o Capitão América.', r'https://upload.wikimedia.org/wikipedia/pt/5/53/Captain_America_Civil_War_poster.jpg', r'https://www.youtube.com/watch?v=dKrVegVI0Us')
panther = media.Movie('Pantera Negra', "Descubra como T'Challa se tornou o Pantera Negra e rei de Wakanda.", r'https://upload.wikimedia.org/wikipedia/pt/thumb/9/90/Pantera_Negra_%28poster%29.jpg/250px-Pantera_Negra_%28poster%29.jpg', r'https://www.youtube.com/watch?v=xjDjIWPwcPU')
strange = media.Movie('Doutor Estranho', 'Descubra como o dourtor Stephen Strange se torna do Doutor Estranho.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/c/c7/Doctor_Strange_poster.jpg/250px-Doctor_Strange_poster.jpg', r'https://www.youtube.com/watch?v=HSzx-zryEgM')
spider = media.Movie('Homem Aranha: de volta ao lar', 'Veja como o jovem Peter Parker está se saindo como mais novo herói', r'https://upload.wikimedia.org/wikipedia/pt/thumb/2/2e/Homecomingposter.png/250px-Homecomingposter.png', r'https://www.youtube.com/watch?v=U0D3AOldjMU')
thor_3 = media.Movie('Thor: Ragnarok', 'Veja Thor, Loki, alguns amigos e todos asgardianos passarem pelo Ragnarok, trazido pela Hella.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/7/7d/Thor_Ragnarok_poster.jpg/250px-Thor_Ragnarok_poster.jpg', r'https://www.youtube.com/watch?v=v7MGUNV8MxU')
avengers_3 = media.Movie('Os Vingadores: Guerra Infinita', 'Veja quando todos os heróis se unem para enfretar Thanos, uma ameaça que pretende acabar com metade da vida do universo.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/9/90/Avengers_Infinity_War.jpg/250px-Avengers_Infinity_War.jpg', r'https://www.youtube.com/watch?v=6ZfuNTqbHE8')
ant_2 = media.Movie('Homen-Formiga e a Vespa', 'Acompanhe Scoot Lang e Hope se unem contra um fantasma.', r'https://upload.wikimedia.org/wikipedia/pt/thumb/5/51/Ant-Man_and_the_Wasp.jpg/250px-Ant-Man_and_the_Wasp.jpg', r'https://www.youtube.com/watch?v=UUkn-enk2RU')

"""Para leitura do fresh_tomatoes foi feito uma lista de todos os filmes. 
Na ordem que devem ser dispostos."""
filmes = [cap_1, iron_man, hulk, iron_man_2, thor_1, avengers_1, iron_man_3, thor_2, cap_2, guardians_1, guardians_2, ant_1, cap_3, panther, strange, spider, thor_3, avengers_3, ant_2]

"""Comando para elaboração do html."""
fresh_tomatoes.open_movies_page(filmes)