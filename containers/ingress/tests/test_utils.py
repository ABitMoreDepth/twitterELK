"""Unit tests for the ingress.utils module."""

import logging
import inspect

import attr
import pytest
import elasticsearch_dsl as es

import ingress.utils as iu

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


@attr.s
class SampleHappy:  # pylint: disable = too-few-public-methods
    """Simple data-structure class to use when testing the singleton method."""

    word = attr.ib()
    number_list = attr.ib()


@attr.s
class SampleSad:  # pylint: disable = too-few-public-methods
    """Simple data-structure class to use when testing the singleton method."""

    word = attr.ib()
    number_list = attr.ib()


def test_get_singleton_happy_case():
    """Verify the correct behaviour of the get_singleton_instance function with valid input."""
    obj_one = iu.get_singleton_instance(SampleHappy, 'Hello, World!', (1, 2))
    obj_two = iu.get_singleton_instance(SampleHappy, 'Hello, World!', (1, 2))
    obj_three = iu.get_singleton_instance(SampleHappy)
    # Whilst retrieving the same instance of something, there's no actual issue
    # with changing that instances state.
    obj_four = iu.get_singleton_instance(SampleHappy, 'something else')

    assert obj_one is obj_two is obj_three is obj_four


@pytest.mark.parametrize(
    'expected_error,input_class,input_args',
    [
        (TypeError,
         None,
         None),
        (ValueError,
         int,
         'a'),
        (TypeError,
         SampleSad,
         (1,
          2,
          3,
          4,
          5,)),
    ],
)
def test_singleton_invalid_inputs(expected_error, input_class, input_args, caplog):
    """Verify correct errors when passing nonsensical inputs to our singleton factory."""
    caplog.set_level(logging.DEBUG)
    with pytest.raises(expected_error):
        iu.get_singleton_instance(input_class, input_args)


def test_find_subclasses_happy_case():
    """Verify that we get expected output from find_subclasses given correct input."""
    # pylint: disable = too-few-public-methods, missing-docstring
    class Base:  # noqa
        pass

    class Sub1(Base):  # noqa
        pass

    class Sub2(Base):  # noqa
        pass

    class SubSub1(Sub2):  # noqa
        pass

    class SubSub2(Sub2):  # noqa
        pass
    # pylint: enable = too-few-public-methods, missing-docstring

    assert inspect.isgenerator(iu.find_subclasses(Base))
    all_subclasses = list(iu.find_subclasses(Base))

    assert all_subclasses == [Sub1, Sub2, SubSub1, SubSub2]


def test_find_subclasses_raises():
    """Verify find_classes appropriately raises a TypeError given improper input."""
    def dummy():
        pass

    with pytest.raises(TypeError):
        list(iu.find_subclasses(dummy))


def test_aggregate_data_schema():
    """Verify the behaviour of the ingress.utils.aggregate_data_schema function."""
    class Base:  # noqa
        data_schema = {}

    class Sub1(Base):  # noqa
        data_schema = {'Sub1': True}

    class Sub2(Base):  # noqa
        data_schema = {'Sub2': True}

    class SubSub1(Sub2):  # noqa
        data_schema = {'SubSub1': True}

    class SubSub2(Sub2):  # noqa
        data_schema = {'SubSub2': True}

    aggregated_schema = iu.aggregate_data_schema(Base, include_defaults=True)

    assert aggregated_schema == {
        'Sub1': True,
        'Sub2': True,
        'SubSub1': True,
        'SubSub2': True,
        '_raw': es.Object(dynamic=True),
        'timestamp': es.Date()
    }
