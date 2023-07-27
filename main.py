from pytube import Playlist, YouTube


def get_urls(playlist_url):
    playlist = Playlist(playlist_url)
    for i in range(len(playlist)):
        video = YouTube(playlist[i]).streams.filter(only_audio=True)
        video[0].download('audios')
        print(f'Audios left {len(playlist) - i}')


get_urls(input('Link to youtube playlist\n'))
