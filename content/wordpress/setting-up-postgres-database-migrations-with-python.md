Title: Postgres database migrations with Python
Date: 2012-11-18 02:41
Author: gmwils
Category: Python

If you need to setup database migrations that work both locally and on
[Heroku][] in Python, these steps may be helpful.

</p>

For a recent project, I wanted to be able to manage the database schema.
I'm not using an ORM, however the migration features in [SQLAlchemy][]
turn out to be quite useful.

</p>

1.  Install the SQLAlchemy migration package, by adding the following to
    requirements.txt.

    </p>

    <p>
        # Migrationssqlalchemy-migrate>=0.7.2

    </p>

    and update:

    </p>

    <p>
        pip install -r requirements.txt

    </p>
    <p>
2.  Create a repository for database migrations

    </p>

    <p>
        migrate create db "Cihui"

    </p>

    This creates a directory `db/` where the code and migrations will
    reside.

    </p>
    <p>
3.  Update the migrate script to use Heroku DB url

    </p>

    <p>
        #!/usr/bin/env pythonfrom migrate.versioning.shell import mainimport osif __name__ == '__main__':    db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost:5432/cihui')    db_url = db_url.replace('postgres:', 'postgresql:', 1)    main(url=db_url, debug='False', repository='db')

    </p>

    This should allow you to run migrations locally or on Heroku. There
    was a warning message on Heroku for the url starting with postgres
    rather than postgresql, thus the `replace` line.

    </p>
    <p>
4.  Update Procfile

    </p>

    This sets up a few useful targets to run on Heroku and locally using
    [foreman][].

    </p>

    <p>
        db_init:  python db/manage.py version_controldb_version:  python db/manage.py db_versionmigrate: python db/manage.py upgrade

    </p>
    <p>
5.  To migrate locally

    </p>

    <p>
        foreman run init_db # first timeforeman run migrate

6.  To run on Heroku

    </p>

    <p>
        heroku run db_init heroku run migrate

7.  Write migrations as SQL

    </p>

    I prefer to manually write the migrations, and SQLAlchemy has great
    support for this. Refer to their docs for [details][].

    </p>

    <p>
        python db/manage.py script_sql postgresql 'add list table'

    </p>

    This generates an upgrade and downgrade sql script in `db/versions`
    with an appropriate version number.

    </p>

    <p>
8.  Test the migration:

    </p>

    <p>
        python db/manage.py test

    </p>

    Runs upgrade and then downgrade on a single version.

    </p>
    <p>
9.  DB access to Heroku

    </p>

    Console access is available via:

    </p>

    <p>
        heroku pg:psql

    </p>

    Useful for checking specific values or fixing broken migrations.

    </p>
    <p>

</p>

I'm still iterating on this project, so may change some things around as
I go. For the moment, this allowed me to manage the database schema
easily in multiple databases.

</p>

  [Heroku]: https://devcenter.heroku.com/articles/heroku-postgresql
  [SQLAlchemy]: https://sqlalchemy-migrate.readthedocs.org/en/v0.7.2/versioning.html
  [foreman]: http://ddollar.github.com/foreman/
  [details]: https://sqlalchemy-migrate.readthedocs.org/en/v0.7.2/versioning.html#writings-sql-scripts
