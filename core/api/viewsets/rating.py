from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from ...models import Rating
from ...serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        book_id = self.request.query_params.get('book')

        if book_id:
            return Rating.objects.filter(user=self.request.user, book_id=book_id)
        else:
            return Rating.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()

        if obj.user != self.request.user:
            raise PermissionDenied("Вы не можете изменять или удалять чужие оценки.")

        return obj

    def update(self, request, *args, **kwargs):
        self.get_object()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.get_object()
        return super().destroy(request, *args, **kwargs)
