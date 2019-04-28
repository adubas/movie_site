"""Importação do web browser para abertura da janela do trailer."""
import webbrowser


class Movie(object):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Classe movie que é a base de informação que serão apresentadas 
        dos filmes escolhidos, serão dispostas os seguintes argumentos:
            movie_title (str) = Título do Filme
            movie_storyline (str) = Resumo do filme
            poster_image (str) (url) = A url do poster do filme
            trailer_youtube (str) (url) = A url do youtube do trailer do filme
        Para apresentar:
            Será exposto o poster do filme com o nome e resenha em baixo e ao clicar no
            poster será aberta uma janela com o trailer."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        """Função que faz com que uma janela seja aberta para mostrar o trailer do filme."""
        webbrowser.open(self.trailer_youtube_url)