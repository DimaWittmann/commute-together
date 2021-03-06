from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'commute_together.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^meeting/new/', 'commute_together.views.new_meeting', name='new_meeting'),
    url(r'^meeting/(\d+)/$', 'commute_together.views.meeting', name='meeting'),
    url(r'^meeting/$', 'commute_together.views.home', name='home'),
	url(r'^meeting/schedule/', 'commute_together.views.schedule', name='schedule'),
	url(r'^meeting/vklogin/$', 'commute_together.views.vklogin', name='vklogin'),
    url(r'^meeting/logout/$', 'commute_together.views.logout_view', name='logout'),


    url(r'^meeting/api/station_name_hints/', 'commute_together.views.station_name_hints_JSON', name='station_name_hints'),
    url(r'^meeting/api/get_schedule/', 'commute_together.views.get_schedule_JSON', name="get_schedule"),
    url(r'^meeting/api/board/', 'commute_together.views.get_board_JSON', name="get_meetings"),
)
