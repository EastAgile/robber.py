from unittest import TestCase

from robber import expect
from tests import must_fail


class TestSimilarToIntegrations(TestCase):
    def test_similar_to_success(self):
        expect('  a  CA t   ').to.be.similar_to('a c A  t')

    @must_fail
    def test_similar_to_failure(self):
        expect('a cat').to.be.similar_to('a dog')

    def test_not_to_similar_to_success(self):
        expect('a cat').not_to.be.similar_to('a dog')

    @must_fail
    def test_not_to_similar_to_failure(self):
        expect('  a  CA t   ').not_to.be.similar_to('a c A  t')
