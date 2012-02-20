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
    	python project/manage.py syncdb --noinput --settings=settings.prod
    	python project/manage.py migrate --noinput --settings=settings.prod
    	python project/manage.py collectstatic --noinput --settings=settings.prod

    style:
    	python project/manage.py make_bookmarklet prod --settings=settings.dev
    	git add project/static/js/bookmarklet.js
    	git commit -m "[CN auto-commit]: rendered bookmarklet.js for production"
    	git push heroku master
    	python project/manage.py collectstatic --noinput --settings=settings.prod
    	python project/manage.py make_bookmarklet dev --settings=settings.dev
    	git add project/static/js/bookmarklet.js
    	git commit -m "[CN auto-commit]: rendered bookmarklet.js back to development"