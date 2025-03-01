from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClientRecommendation


class RecommendationView(APIView):
    def get(self, request, client_id):
        recommendations = ClientRecommendation.objects.filter(client_id=client_id).order_by('-recommendation_score')[:3]
        response_data = [{"product_name": rec.product_name, "score": rec.recommendation_score} for rec in
                         recommendations]

        if not response_data:
            return Response({"message": "No recommendations found."}, status=status.HTTP_404_NOT_FOUND)

        return Response(response_data, status=status.HTTP_200_OK)