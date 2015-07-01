MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=commute_together.settings $(MANAGE) test commute_together

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=commute_together.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=commute_together.settings $(MANAGE) migrate --noinput