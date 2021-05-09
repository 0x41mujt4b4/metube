from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
import pafy, requests, threading, mimetypes
from django.views.generic import TemplateView
# from pytube import YouTube


class Index(TemplateView):

    template_name = 'YoutubeApp/index.html'

    def post(self, request):
        global video, audio
        url = request.POST.get("url")
        # try:
        stream = pafy.new(url)
        video = stream.streams
        vid_name = video[0].generate_filename()
        audio = stream.m4astreams
        context = {'url':url, 'stream':stream, 'video':video, 'audio':audio, 'file_name':vid_name}
        return render(request, self.template_name, context=context)
        # except IOError:
        #     return redirect('YoutubeApp/index.html')
        

    def get(self, request):
        return render(request, self.template_name, context={'url':''})


def download(request, file_name):
    vid = video[0]
    vid_url = vid.url
    r = requests.get(vid_url, stream=True)
    mime_type, _ = mimetypes.guess_type(file_name)
    print('the video type is: ', mime_type)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Type'] = mime_type
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response


# def stream(request, path):
#     range_header = request.META.get('HTTP_RANGE', '').strip()
#     range_match = range_re.match(range_header)
#     size = os.path.getsize(path)
#     content_type, encoding = mimetypes.guess_type(path)
#     content_type = content_type or 'application/octet-stream'
#     if range_match:
#         first_byte, last_byte = range_match.groups()
#         first_byte = int(first_byte) if first_byte else 0
#         last_byte = int(last_byte) if last_byte else size - 1
#         if last_byte >= size:
#             last_byte = size - 1
#         length = last_byte - first_byte + 1
#         resp = StreamingHttpResponse(r, status=206, content_type=content_type)
#         resp['Content-Length'] = str(length)
#         resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
#     else:
#         resp = StreamingHttpResponse(r, content_type=content_type)
#         resp['Content-Length'] = str(size)
#     resp['Accept-Ranges'] = 'bytes'
#     return resp

    