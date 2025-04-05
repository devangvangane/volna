from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ttspeech.views import text_to_speech, delete_audio, home, file_to_speech, image_to_speech, pptx_to_speech, translation,get_supported_languages

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("text-to-speech/", text_to_speech, name="text_to_speech"),
    path("file-to-speech/", file_to_speech, name="file_to_speech"),
    path("image-to-speech/", image_to_speech, name="image_to_speech"),
    path('pptx-to-speech/', pptx_to_speech, name='pptx_to_speech'),
    path('translation/', translation, name="translation"),
    path("delete-audio/", delete_audio, name="delete_audio"),
    path("get-supported-languages", get_supported_languages, name="get_supported_languages"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)