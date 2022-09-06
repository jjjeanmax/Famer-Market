import django_tables2 as tables

from .models import *


class FamersInfosTable(tables.Table):
    class Meta:
        model = FamersInfos
        template_name = "django_tables2/bootstrap.html"


class FamersProductsTable(tables.Table):
    class Meta:
        model = FamersProducts
        template_name = "django_tables2/bootstrap.html"


class CommentsUserTable(tables.Table):
    class Meta:
        model = CommentsUser
        template_name = "django_tables2/bootstrap.html"
