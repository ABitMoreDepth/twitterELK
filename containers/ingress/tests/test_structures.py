"""
Unit tests for the ingress.elastic module.
"""
import attr
import pytest

import ingress.structures as IS


@attr.s
class Sample:  # pylint: disable = too-few-public-methods
    """
    Simple data-structure class to use with the singleton method to retrieve the same instance.
    """
    word = attr.ib()
    number_list = attr.ib()


def test_get_singleton_happy_case():
    """
    Verify that we actually get the same instance of a class back when
    requesting an instance of the same type twice.
    """

    obj_one = IS.get_singleton_instance(Sample, 'Hello, World!', (1, 2))
    obj_two = IS.get_singleton_instance(Sample, 'Hello, World!', (1, 2))
    obj_three = IS.get_singleton_instance(Sample)
    # Whilst retrieving the same instance of something, there's no actual issue
    # with changing that instances state.
    obj_four = IS.get_singleton_instance(Sample, 'something else')

    assert obj_one is obj_two is obj_three is obj_four


@pytest.mark.parametrize(
    'expected_error,input_class,input_args',
    [
        (TypeError, None, None),
        (TypeError, int, 1),
        (TypeError, Sample, (1,2,3,4,5)),
    ],
)
def test_singleton_invalid_inputs(expected_error, input_class, input_args):
    """
    Verify that we get the correct errors when passing nonsensical inputs to
    our singleton factory.
    """

    with pytest.raises(expected_error):
        IS.get_singleton_instance(input_class, input_args)
