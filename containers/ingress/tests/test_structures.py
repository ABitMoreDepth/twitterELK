"""Unit tests for the ingress.structures module."""

from unittest.mock import create_autospec, call

import pytest

import ingress.structures as is_


def test_plugin_base_import_subclasses(monkeypatch):
    """Verify that we attempt to import the correct files when importing plugins.

    We should correctly ignore files that start with `__`, or the `processing.py` file.
    """
    mock_os_walk = create_autospec(is_.walk)
    sample_files = [
        (
            None,
            None,
            [
                "__nothing.py",
                "thing1.py",
                "thing1.py.something",
                "thing1.py@something",
                "geocode.py@neomake_32242_610",
                "thing2.py",
                "thing3.py",
                "thing4.py",
            ],
        )
    ]
    mock_os_walk.return_value = iter(sample_files)
    monkeypatch.setattr('ingress.structures.walk', mock_os_walk)

    mock_import_module = create_autospec(is_.import_module)
    monkeypatch.setattr('ingress.structures.import_module', mock_import_module)

    is_.PluginBase.import_subclasses()

    print(mock_import_module.call_args_list)
    expected_call_list = [
        call('ingress.data_processing.{}'.format(filename))
        for filename in ('thing1',
                         'thing2',
                         'thing3',
                         'thing4')
    ]

    assert mock_import_module.call_args_list == expected_call_list


def test_plugin_base_raises_process_tweet():
    """Ensure that PluginBase.process_tweet is a pure function.

    i.e. that it will raise a NotImplementedError if called directly.
    """
    with pytest.raises(NotImplementedError):
        sample = is_.PluginBase()
        sample.process_tweet('')
