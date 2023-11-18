from rest_framework import viewsets
from libraryapp.models import Author, Book
from libraryapp.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    #region ViewSet Func
        # def get_queryset(self):
    #     firstName = self.request.query_params.get('firstName',None)
    #     secondName = self.request.query_params.get('secondName',None)
    #     birthDate = self.request.query_params.get('birthDate',None) 
    #     queryset = Author.objects.all()

    #     if firstName:
    #         queryset = queryset.filter(firstName = firstName)
        
    #     if secondName:
    #         queryset = queryset.filter(secondName = secondName)

    #     if birthDate:
    #         queryset = queryset.filter(birthDate = birthDate)


    #     return queryset

    # def put(self, request, pk, format=None):
    #     try:
    #         author = self.get_object(pk)
    #     except Author.DoesNotExist:
    #         return Response( data = {"Hata":"Böyle bir nesne bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = AuthorSerializer(author, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     try:
    #         author = self.get_object(pk)
    #     except Author.DoesNotExist:
    #         return Response(data = {"Hata":"Böyle bir nesne bulunamadı."}, status=status.HTTP_404_NOT_FOUND)
        
    #     author.delete()
    #     return Response({'success':'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    #endregion

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer