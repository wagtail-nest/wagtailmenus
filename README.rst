.. image:: https://img.shields.io/pypi/v/wagtailmenus.svg
    :alt: PyPI Version
    :target: https://pypi.org/project/wagtailmenus/

.. image:: https://github.com/wagtail-nest/wagtailmenus/actions/workflows/test.yml/badge.svg
    :alt: Build Status
    :target: https://github.com/wagtail-nest/wagtailmenus/actions/workflows/test.yml

.. image:: https://codecov.io/gh/wagtail-nest/wagtailmenus/graph/badge.svg?token=Ijthoeo2P9
    :alt: Code coverage
    :target: https://codecov.io/gh/wagtail-nest/wagtailmenus

.. image:: https://readthedocs.org/projects/wagtailmenus/badge/?version=latest
    :alt: Documentation Status
    :target: https://wagtailmenus.readthedocs.io/en/latest/


============
wagtailmenus
============

wagtailmenus is an extension for `Wagtail CMS <https://github.com/wagtail/wagtail>`_ to help you manage and render multi-level navigation and simple flat menus in a consistent, flexible way.

The current version is tested for compatibility with the following:

- Wagtail versions 7.0, 7.3, 7.4 and 8.0
- Django versions 4.2, 5.2, 6.0 and 6.1
- Python versions 3.10 to 3.14

.. image:: https://raw.githubusercontent.com/wagtail-nest/wagtailmenus/main/docs/source/_static/images/repeating-item.png

New to wagtailmenus?
====================

Start by reading our `Overview and key concepts <https://wagtailmenus.readthedocs.io/en/stable/overview.html>`_ page.
It will give you a better understand of how the app works, and help you decide whether it is a good fit for your project.


Installation
============

1.  Install the package from PyPI:

    .. code-block:: console

        pip install wagtailmenus

2.  Add ``wagtailmenus`` to ``INSTALLED_APPS``, and
    ``wagtailmenus.context_processors.wagtailmenus`` to the
    ``context_processors`` list in your ``TEMPLATES`` setting.

3.  Run migrations:

    .. code-block:: console

        python manage.py migrate wagtailmenus

See the `installation guide <https://wagtailmenus.readthedocs.io/en/stable/installation.html>`_ for the full steps and optional settings.


Useful links
============

- `Documentation <https://wagtailmenus.readthedocs.io/>`_
- `Changelog <https://github.com/wagtail-nest/wagtailmenus/blob/main/CHANGELOG.md>`_
- `Release notes <https://wagtailmenus.readthedocs.io/en/stable/releases/index.html>`_
- `Issue tracker <https://github.com/wagtail-nest/wagtailmenus/issues>`_
- `Source code <https://github.com/wagtail-nest/wagtailmenus>`_


Contributing
============

Instructions on how to contribute can be found `here <https://wagtailmenus.readthedocs.io/en/stable/contributing/index.html>`_.

wagtailmenus is part of `Wagtail Nest <https://github.com/wagtail-nest>`_. All contributors are expected to follow our `Code of Conduct <https://github.com/wagtail-nest/wagtailmenus/blob/main/CODE_OF_CONDUCT.md>`_.
