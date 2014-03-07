django-tooltips
====================

Manageable bootstrap tooltips


Requirements
============

- Django (duh)
- Bootstrap
- Jquery

Installation
============

Install the app via pip:

    $ pip install django-tooltips

Add `tooltips` to your installated apps:

```python
INSTALLED_APPS = (
    ...
    'tooltips',
    ...
```

Add the processor to your `TEMPLATE_CONTEXT_PROCESSORS`:

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'tooltips.processors.tooltips',
)
```

Include this in your templates (eg, `base.html`):

{% include "tooltips/tooltips.html" %}

And run the migrations:

    $ manage.py migrate

Now, whenever you add a tooltip via the admin, it will appear on your pages just after the element you provided via the javascript selector:


Preview
=======
Clientside:

![adming](https://raw.github.com/svdgraaf/django-tooltips/master/preview.png)

Admin:

![adming](https://raw.github.com/svdgraaf/django-tooltips/master/admin.png)



Caveats
=======

As the selectors are plain javascript selectors, you can use all the magic you want. But don't use very wide selectors like `div` or `div:contains("")`, those will probably bring your browser to a standstil :) YMMV