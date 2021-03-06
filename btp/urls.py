from django.conf.urls import url
from btp import views , git_views
from django.conf import settings
from django.contrib.auth.views import password_reset, logout
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^git/commands/$', git_views.GitCommand.as_view()),
	url(r'^$', login_required(views.BTPIndexView.as_view()),name='btphomepage'),
	url(r'^post/report/$', views.submit_report, name='submitreport'),
	url(r'^add-project/$', login_required(views.AddProject.as_view())),
	url(r'^edit-project/$', login_required(views.EditProject.as_view())),
	url(r'^edit-submit-project/$', login_required(views.editSubmitProject)),
	url(r'^edit-project/(?P<id>[0-9]+)/$', login_required(views.EditProjectInstance.as_view())),
	url(r'^submit-project/$', login_required(views.SubmitProject)),
	url(r'^add-students/(?P<id>[0-9]+)/$', login_required(views.addStudentsToProject)),
	url(r'^get-current-students/$', login_required(views.getCurrentStudents)),
	url(r'^upload-project-file/(?P<id>[0-9]+)/$', login_required(views.uploadProjectFileFaculty)),
	url(r'^file-delete/(?P<id>[0-9]+)/$', login_required(views.deleteUploadedProjectMedia)),
	url(r'^move-to-archives/(?P<id>[0-9]+)/$', login_required(views.moveProjectToArchives)),
	url(r'^archive-restore/(?P<id>[0-9]+)/$', login_required(views.restoreFromArchives))
]
if settings.SERVE_MEDIA:
    urlpatterns += (
        url(r'media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        url(r'static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, }),
)
