import uuid
from django.db import models


class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represent the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        description: The short description of how the algorithm works.
        code: Code for the model implementation
        version: The version of the algorithm similar to software versioning.
        owner: The name of the owner.
        created_at: The date when MLAlgorithm was added.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-v{self.version} | {self.created_at}'


class NLPRequest(models.Model):
    '''
    The NLPRequest will keep information about all requests to NLP algorithms.

    Attributes:
        input_data: The input data to algorithm in JSON format.
        full_response: The response of the algorithm.
        response: The response of the algorithm in JSON format.
        created_at: The date when request was created.
    '''
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    request = models.CharField(max_length=10000, blank=True)
    response = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)