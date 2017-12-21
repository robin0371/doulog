from django.conf.urls import url

from api.views import ChildViewSet, RegisterViewSet


urlpatterns = [
    url(r'^child/$', ChildViewSet.as_view(actions={
        'post': 'create',
        'get': 'list'
    }), name='child'),

    url(r'^child/(?P<pk>[0-9]+)/$', ChildViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
    }), name='child-detail'),

    url(r'^register/$', RegisterViewSet.as_view(actions={
        'post': 'create',
        'get': 'list'
    }), name='register'),
]
