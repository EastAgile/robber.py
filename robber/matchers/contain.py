from robber import expect
from robber.explanation import Explanation
from robber.matchers.base import Base


class Contain(Base):
    """
    expect({'key': value}).to.contain('key 1', 'key 2', 'key n')
    expect([1, 2, 3]).to.contain(1, 2, 3)
    """

    def matches(self):
        expected_list = list(self.args)
        expected_list.insert(0, self.expected)
        self.expected_arg = None

        if not self.is_negative:
            for expected in expected_list:
                if expected not in self.actual:
                    self.expected_arg = expected
                    break

        else:
            for expected in expected_list:
                if expected in self.actual:
                    self.expected_arg = expected
                    break

        existed = self.expected_arg is not None
        return existed is self.is_negative

    @property
    def explanation(self):
        return Explanation(self.actual, self.is_negative, 'contain', self.expected_arg, negative_action='exclude')


expect.register('contain', Contain)
expect.register('exclude', Contain, is_negative=True)
