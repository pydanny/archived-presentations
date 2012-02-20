.. sourcecode:: MakeFile

    # Some helpful utility commands.

    all: deploy

    migrate:
    	git push heroku master
    	python project/manage.py syncdb --noinput --settings=settings.prod
    	python project/manage.py migrate --noinput --settings=settings.prod

    deploy:
    	heroku pgbackups:capture --expire
    	git push heroku master
    	heroku run newrelic-admin run-program python cn_project/manage.py syncdb --noinput --settings=settings.prod
    	heroku run newrelic-admin run-program python cn_project/manage.py migrate --noinput --settings=settings.prod
    	heroku run newrelic-admin run-program python cn_project/manage.py collectstatic --noinput --settings=settings.prod

    style:
    	python cn_project/manage.py make_bookmarklet prod --settings=settings.dev
    	git add cn_project/static/js/bookmarklet.js
    	git commit -m "[CN auto-commit]: rendered bookmarklet.js for production"
    	git push heroku master
    	heroku run newrelic-admin run-program python cn_project/manage.py collectstatic --noinput --settings=settings.prod
    	python cn_project/manage.py make_bookmarklet dev --settings=settings.dev
    	git add cn_project/static/js/bookmarklet.js
    	git commit -m "[CN auto-commit]: rendered bookmarklet.js back to development"