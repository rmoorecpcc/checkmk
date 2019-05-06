# Stubs for kubernetes.client.apis.authorization_v1_api (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..api_client import ApiClient
from typing import Any, Optional

class AuthorizationV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_namespaced_local_subject_access_review(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_local_subject_access_review_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_self_subject_access_review(self, body: Any, **kwargs: Any): ...
    def create_self_subject_access_review_with_http_info(self, body: Any, **kwargs: Any): ...
    def create_self_subject_rules_review(self, body: Any, **kwargs: Any): ...
    def create_self_subject_rules_review_with_http_info(self, body: Any, **kwargs: Any): ...
    def create_subject_access_review(self, body: Any, **kwargs: Any): ...
    def create_subject_access_review_with_http_info(self, body: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...