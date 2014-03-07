django-support-pages
====================

Manageable bootstrap tooltips and Support pages

Installation
============

Add `support` to your installated apps:

```python
INSTALLED_APPS = (
    ...
    'support',
    ...
```

If you want to use the Tooltips, be sure to add the processor to your processors:

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'support.processors.tooltips',
)
```