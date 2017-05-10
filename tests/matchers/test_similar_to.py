from unittest import TestCase

from robber import expect
from robber.matchers.similar_to import SimilarTo


class TestSimilarTo(TestCase):
    def test_matches(self):
        expect(SimilarTo('  a  CA t   ', 'a c A  t').matches()).to.eq(True)
        expect(SimilarTo('a cat', 'a dog').matches()).to.eq(False)

    def test_explanation_message(self):
        similar_to = SimilarTo('a cat', 'a dog')
        message = similar_to.explanation.message
        expect(message).to.be.similar_to("""
A = a cat
B = a dog
Expected A to be similar to B
""")

    def test_negative_explanation_message(self):
        similar_to = SimilarTo('  a  CA t   ', 'a c A  t', is_negative=True)
        message = similar_to.explanation.message
        expect(message).to.be.similar_to("""
A =   a  CA t
B = a c A  t
Expected A not to be similar to B
""")

    def test_not_strings(self):
        self.assertRaises(TypeError, SimilarTo(1, '1').matches)
        self.assertRaises(TypeError, SimilarTo('1', [1]).matches)

    def test_register(self):
        expect(expect.matcher('similar_to')) == SimilarTo
