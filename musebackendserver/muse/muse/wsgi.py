import os
import inspect
from django.core.wsgi import get_wsgi_application
from apps.nlp.registry import MLRegistry
from apps.nlp.usencoder.model import UniversalSentenceEncoder

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muse.settings')
application = get_wsgi_application()


try:
    # create ML registry
    registry = MLRegistry() 
    le = UniversalSentenceEncoder()
    # add to ML registry
    registry.add_algorithm(endpoint_name="universal_sentence_encoder",
                            algorithm_object=le,
                            algorithm_name="Universal Sentence Encoder",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Nitish",
                            algorithm_description="Create sentence embeddings",
                            algorithm_code=inspect.getsource(UniversalSentenceEncoder))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))