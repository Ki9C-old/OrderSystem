from django.contrib import admin
from .models import dish
from .models import category
from .models import user
from .models import authcategory
from .models import order
from .models import status
from .models import taxcategory

admin.site.register(dish)
admin.site.register(category)
admin.site.register(user)
admin.site.register(authcategory)
admin.site.register(order)
admin.site.register(status)
admin.site.register(taxcategory)