    from ast import Add
    from ckeditor.fields import RichTextField
    from core import serializers
    from core.asgi import get_asgi_application
    from core.management import execute_from_command_line
    from core.wsgi import get_wsgi_application
    from db import migrations
    from db import transaction
    from http import HttpResponse
    from http import JsonResponse
    from shortcuts import redirect, render
    from shortcuts import redirect, render, get_object_or_404
    from shortcuts import render, get_object_or_404
    from shortcuts import render, redirect
    from template.loader import render_to_string
    from urls import path
    from urls import path, include
    from urls import reverse
    from utils import timezone
    from utils.html import mark_safe
    from django_ckeditor_5.fields import CKEditor5Field
    from enum import unique
    from pathlib import Path
    from paypal.standard.forms import PayPalPaymentsForm
    from requests import session
    from shortuuid.django_fields import ShortUUIDField
    from stripe import Review
    from taggit.managers import TaggableManager
    from taggit.models import Tag
    from useradmin.forms import AddProductForm
    import calendar
    import ckeditor.fields
    import ckeditor_uploader.fields
    import core.models
    import datetime
    import contrib.auth.models
    import db.models.deletion
    import utils.timezone
    import django_ckeditor_5.fields
    import pyperclip
    import pyperclip as p
    import shortuuid.django_fields
    import taggit.managers



Pillow==10.1.0
Django==4.2.2
djangorestframework==3.12.4
cookiecutter-django==2.0.8
django-import-export==2.7.0
django-tenants==3.0.0
django-debug-toolbar==3.2.2
django-extensions==3.1.3
django-cors-headers==3.10.1
django-allauth==0.44.0
