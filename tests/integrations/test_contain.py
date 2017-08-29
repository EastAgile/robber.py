from unittest import TestCase

from robber import expect
from tests import must_fail


class TestContainIntegrations(TestCase):
    def test_contain_success(self):
        expect([1, 2, 3]).to.contain(2)
        expect('abc').to.contain('abc')
        expect('abc').to.contain('ab', 'bc')
        expect([{"test": "test"}]).to.contain({"test": "test"})
        expect([{"test": "test"}]).to.contain({"test": "test"}, {"test": "test"})

    @must_fail
    def test_contain_failure(self):
        expect([1, 2, 3]).to.contain(4)

    def test_not_contain_success(self):
        expect([1, 2, 3]).not_to.contain(4)

    @must_fail
    def test_not_contain_failure(self):
        expect([1, 2, 3]).not_to.contain(2)

    def test_contain_multiple_value(self):
        expect([1, 2, 3]).to.contain(1, 2)

    @must_fail
    def test_contain_multiple_value_failure(self):
        expect([1, 2, 3]).to.contain(1, 4)

    def test_not_contain_multiple_value(self):
        expect([1, 2, 3]).not_to.contain(4, 5)

    @must_fail
    def test_not_contain_multiple_value_failure(self):
        expect([1, 2, 3]).not_to.contain(1, 4)


class TestExcludeIntegrations(TestCase):
    def test_exclude_success(self):
        expect([1, 2, 3]).to.exclude(0)
        expect('abc').to.exclude('abcd')
        expect('abc').to.exclude('abd', 'bcd')
        expect([{"test": "test"}]).to.exclude({"tests": "test"})
        expect([{"test": "test"}]).to.exclude({"tests": "test"}, {"tests": "test"})

    @must_fail
    def test_exclude_failure(self):
        expect([1, 2, 3]).to.exclude(2)

    def test_not_exclude_success(self):
        expect([1, 2, 3]).not_to.exclude(2)

    @must_fail
    def test_not_exclude_failure(self):
        expect([1, 2, 3]).not_to.exclude(0)

    def test_exclude_multiple_value(self):
        expect([1, 2, 3]).to.exclude(4, 5)

    @must_fail
    def test_exclude_multiple_value_failure(self):
        expect([1, 2, 3]).to.exclude(1, 2)

    def test_not_exclude_multiple_value(self):
        expect([1, 2, 3]).not_to.exclude(1, 2)

    @must_fail
    def test_not_exclude_multiple_value_failure(self):
        expect([1, 2, 3]).not_to.exclude(1, 4)
