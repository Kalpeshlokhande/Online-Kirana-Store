from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.addresses.models import Address
from apps.addresses.serializers.address import AddressSerializer

class UpdateAddressView(APIView):
    def put(self, request):
        try:
            address, created = Address.objects.get_or_create(user=request.user)
            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'detail': str(e)}, status=400)