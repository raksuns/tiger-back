import pytest

from django.core.urlresolvers import reverse

from tiger.base.utils import json

from .. import factories as f


def test_users_create_through_standard_api(client):
    user = f.UserFactory.create(is_superuser=True)

    url = reverse('users-list')
    data = {}

    response = client.post(url, json.dumps(data), content_type="application/json")
    assert response.status_code == 405

