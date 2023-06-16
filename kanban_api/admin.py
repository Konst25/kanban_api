from django.contrib import admin
from .models import Board
from .models import Admin
from .models import StatusList
from .models import User
from .models import Card

# Register your models here.
admin.site.register(Board)
admin.site.register(Admin)
admin.site.register(StatusList)
admin.site.register(User)
admin.site.register(Card)