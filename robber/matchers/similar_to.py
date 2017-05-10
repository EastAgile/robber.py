import re

from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class SimilarTo(Base):
    """
    expect('a   StRing').to.be.similar_to('a string')
    """

    def matches(self):
        try:
            standardized_actual = re.sub('\s', '', self.actual).lower()
            standardized_expected = re.sub('\s', '', self.expected).lower()
        except TypeError:
            raise TypeError('Expected two strings')

        return standardized_actual == standardized_expected

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'be similar to', self.expected)


expect.register('similar_to', SimilarTo)
