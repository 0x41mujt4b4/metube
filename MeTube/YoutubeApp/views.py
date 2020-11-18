from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import pafy, requests
# from pytube import YouTube



def index(request):
    global video, audio
    url = request.POST.get("url")
    try:
        stream = pafy.new(url)
        video = stream.streams
        audio = stream.m4astreams
        context = {'url':url, 'stream':stream, 'video':video, 'audio':audio}
        return render(request, "YoutubeApp/index.html", context)
    except:
        return render(request, "YoutubeApp/index.html", {"url":""})


def download(request):
    vid = video[0]
    filename = vid.generate_filename()
    r = requests.get(vid.url, stream=True)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Disposition'] = f'attachement; filename="{filename}"'
    return response
