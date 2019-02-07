from django.conf.urls import url, include
from django.urls import path  
from valores_banco.models import valorModel 
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class valorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = valorModel
        fields = ('valor_banco_brasil', 'valor_banco_bradesco')

# ViewSets define the view behavior.
class valorModelViewSet(viewsets.ModelViewSet):
    queryset = valorModel.objects.all()
    serializer_class = valorModelSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'valor', valorModelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
