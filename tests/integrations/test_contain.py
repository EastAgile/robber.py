from unittest import TestCase

from robber import expect
from tests import must_fail


class TestContainIntegrations(TestCase):
    def test_contain_success(self):
        expect([1, 2, 3]).to.contain(2)

    @must_fail
    def test_contain_failure(self):
        expect([1, 2, 3]).to.contain(4)