from pytube import Playlist, YouTube


def get_urls(playlist_url):
    playlist = Playlist(playlist_url)
    playlist_len = len(playlist)
    for i in range(playlist_len):
        video = YouTube(playlist[i])
        download = video.streams.filter(only_audio=True)
        download[0].download('audios')
        print(f'Audios left {playlist_len - i}')

get_urls(input('Link to youtube playlist\n'))
