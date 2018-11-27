"""
Unit tests for the ingress.data_processing.processing module.
"""
import inspect
import pytest

import ingress.data_processing.processing as idp


def test_find_subclasses_happy_case():
    """
    Verify that we get a generator object that returns the correct set of sub
    classes for a given input.
    """
    # pylint: disable = too-few-public-methods, missing-docstring
    class Base:
        pass

    class Sub1(Base):
        pass

    class Sub2(Base):
        pass

    class SubSub1(Sub2):
        pass

    class SubSub2(Sub2):
        pass
    # pylint: enable = too-few-public-methods, missing-docstring

    assert inspect.isgenerator(idp.find_subclasses(Base))
    all_subclasses = list(idp.find_subclasses(Base))

    assert all_subclasses == [Sub1, Sub2, SubSub1, SubSub2]


def test_find_subclasses_raises():
    """
    Verify that we see a TypeError when passing anything other than a class
    into the find_subclasses function.
    """
    def dummy():
        pass

    with pytest.raises(TypeError):
        list(idp.find_subclasses(dummy))


def test_plugin_base_raises_process_tweet():
    """
    Ensure that PluginBase.process_tweet is a pure function, i.e. that it will
    raise a NotImplementedError if called directly.
    """
    with pytest.raises(NotImplementedError):
        sample = idp.PluginBase()
        sample.process_tweet()
