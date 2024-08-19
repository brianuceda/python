from pytube import YouTube

# Crear objeto YouTube
yt = YouTube('https://www.youtube.com/watch?v=6-YPVUgAO3I&')

# Obtener información del video
titulo = yt.title
duracion = yt.length  # duración en segundos
vistas = yt.views
descripcion = yt.description
autor = yt.author

# Imprimir información
print(f'Título: {titulo}')
print(f'Duración: {duracion} segundos')
print(f'Vistas: {vistas}')
print(f'Descripción: {descripcion}')
print(f'Autor: {autor}')
