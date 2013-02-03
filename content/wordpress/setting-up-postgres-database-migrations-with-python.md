Title: Postgres database migrations with Python
Date: 2012-11-18 02:41
Author: gmwils
Category: Python

If you need to setup database migrations that work both locally and on
[Heroku][] in Python, these steps may be helpful.

For a recent project, I wanted to be able to manage the database schema.
I'm not using an ORM, however the migration features in [SQLAlchemy][]
turn out to be quite useful.

1.  Install the SQLAlchemy migration package, by adding the following to
    requirements.txt.

        :::python
        # Migrations
        sqlalchemy-migrate>=0.7.2

    and update:

        pip install -r requirements.txt

2.  Create a repository for database migrations

        migrate create db "Cihui"

    This creates a directory `db/` where the code and migrations will
    reside.

3.  Update the migrate script to use Heroku DB url

        :::python
        #!/usr/bin/env python

        from migrate.versioning.shell import main
        import os

        if __name__ == '__main__':
            db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost:5432/cihui')
            db_url = db_url.replace('postgres:', 'postgresql:', 1)
            main(url=db_url, debug='False', repository='db')

    This should allow you to run migrations locally or on Heroku. There
    was a warning message on Heroku for the url starting with postgres
    rather than postgresql, thus the `replace` line.

4.  Update Procfile

    This sets up a few useful targets to run on Heroku and locally using
    [foreman][].

        db_init:  python db/manage.py version_control
        db_version:  python db/manage.py db_version
        migrate: python db/manage.py upgrade

5.  To migrate locally

        foreman run init_db # first time
        foreman run migrate

6.  To run on Heroku

        heroku run db_init
        heroku run migrate

7.  Write migrations as SQL

    I prefer to manually write the migrations, and SQLAlchemy has great
    support for this. Refer to their docs for [details][].

        python db/manage.py script_sql postgresql 'add list table'

    This generates an upgrade and downgrade sql script in `db/versions`
    with an appropriate version number.

8.  Test the migration:

        python db/manage.py test

    Runs upgrade and then downgrade on a single version.

9.  DB access to Heroku

    Console access is available via:

        heroku pg:psql

    Useful for checking specific values or fixing broken migrations.

I'm still iterating on this project, so may change some things around as
I go. For the moment, this allowed me to manage the database schema
easily in multiple databases.

  [Heroku]: https://devcenter.heroku.com/articles/heroku-postgresql
  [SQLAlchemy]: https://sqlalchemy-migrate.readthedocs.org/en/v0.7.2/versioning.html
  [foreman]: http://ddollar.github.com/foreman/
  [details]: https://sqlalchemy-migrate.readthedocs.org/en/v0.7.2/versioning.html#writings-sql-scripts
