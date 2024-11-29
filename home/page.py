import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de Filmes')
    if len(movie_stats['Movies_by_Genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['Movies_by_Genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['Total_movies'])

    st.subheader('Quantidade de Filmes por Gênero:')
    for genre in movie_stats['Movies_by_Genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_stats['Total_Reviews'])

    st.subheader('Média Geral de Estrelas nas Avaliações:')
    st.write(movie_stats['Avg_stars'])
