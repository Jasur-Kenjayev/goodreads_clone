from django.core.serializers import serialize
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewSerializer
from books.models import BookReview
from rest_framework import viewsets

class BookReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-create_at')
    lookup_field = 'id'

# class BookReviewDetailAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, id):
#         book_review = BookReview.objects.get(id=id)
#
#         serializer = BookReviewSerializer(book_review)
#         return Response(data=serializer.data)
#
# class BookReviewsAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         book_reviews = BookReview.objects.all().order_by('-create-_at')
#         serializer = BookReviewSerializer(book_reviews, many=True)
#         return Response(data=serializer.data)