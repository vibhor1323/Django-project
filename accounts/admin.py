from django.contrib import admin
from accounts.models import userProfile

# Register your models here.
class userProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info', 'city','phone', 'website')

	def user_info(self,obj):
		return obj.description

	def get_queryset(self, request):
		queryset = super(userProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('-phone')
		return queryset

admin.site.register(userProfile,userProfileAdmin)