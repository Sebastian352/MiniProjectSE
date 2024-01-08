from django.shortcuts import render
from django.views.decorators import gzip
from .camera import *

# Create your views here.


@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(
            gen(cam), content_type="multipart/x-mixed-replace;boundary=frame"
        )
    except:  # This is bad!
        pass


def index(request):
    return render(request, "main/index.html", {})
