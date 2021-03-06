from unittest import TestCase

from robber import expect
from robber.matchers.contain import Contain


class TestContain(TestCase):
    def test_matches(self):
        expect(Contain({'key': 'value'}, 'key').matches()).to.eq(True)
        expect(Contain([1, 2, 3], 2).matches()).to.eq(True)
        expect(Contain((1, 2, 3), 3).matches()).to.eq(True)

        expect(Contain({'key': 'value'}, 'other').matches()).to.eq(False)
        expect(Contain([1, 2, 3], 4).matches()).to.eq(False)
        expect(Contain((1, 2, 3), 4).matches()).to.eq(False)

    def test_explanation_message(self):
        contain = Contain([1, 2, 3], 4)
        contain.matches()
        message = contain.explanation.message
        expect(message) == """
A = [1, 2, 3]
B = 4
Expected A to contain B
"""

    def test_explanation_message_with_multiple_args(self):
        contain = Contain([1, 2, 3], 4, False, 5)
        contain.matches()
        message = contain.explanation.message
        expect(message) == """
A = [1, 2, 3]
B = 4
Expected A to contain B
"""

    def test_negative_explanation_message(self):
        contain = Contain([1, 2, 3], 2, is_negative=True)
        contain.matches()
        message = contain.explanation.message
        expect(message) == """
A = [1, 2, 3]
B = 2
Expected A to exclude B
"""

    def test_negative_explanation_message_with_multiple_args(self):
        contain = Contain([1, 2, 3], 2, True, 3)
        contain.matches()
        message = contain.explanation.message
        expect(message) == """
A = [1, 2, 3]
B = 2
Expected A to exclude B
"""

    def test_register(self):
        expect(expect.matcher('contain')) == Contain
        expect(expect.matcher('exclude')) == Contain
