from django.db import models


class ClientRecommendation(models.Model):
    client_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    recommendation_score = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} for client {self.client_id}"


class ResponseTable(models.Model):
    client_id = models.IntegerField()
    response = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response for client {self.client_id} at {self.created_at}"

