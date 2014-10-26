Title: Downloading Google Analytics data from a Python script
Date: 2014-09-22
Author: gmwils
Summary: Making use of Python to extract data from Google Analytics for further analysis

If you want to regularly extract data from Google Analytics, it is worthwhile
scripting the process. However, it was more complex than I expected.

I started with jaco's
[post](http://www.jaco.it/blog/2013/05/31/google-api-oauth-2-dot-0-the-short-way),
and then added some detail from there.

## Setting up your Google account
Since Google has moved to OAuth2, you need a
[service account](https://developers.google.com/accounts/docs/OAuth2ServiceAccount)
to get a script to work.

There are a few steps to do from the
[Google Developers Console](https://console.developers.google.com/project):

1. Create a project (eg. GAStatistics). This step may take a minute or two.
2. From the project page, go to _APIs & auth -> APIs_, and add permissions for
   the Analytics API (accepting the T&Cs)
3. From the Credentials section of _APIs & auth_, create a new client ID, and pick
   Service Account when prompted. You should now automatically download a .p12
   file that includes your client ids and secret keys.
4. For your service account, save the email address that is generated. You'll
   use in a few places.

Next you need grant your service account access to your Google Analytics
account.

1. From [Google Analytics](https://www.google.com/analytics/web), pick the web
   property you want to gather data from.
2. Navigate to the Admin tab at the top, and then to the User Management
   section (you need to have permissions, otherwise ask your site admin)
3. Add your service account email to _Add permissions for:_, and choose the
   type of permissions. I usually pick _Read & Analyze_, as I'm paranoid about
   messing data up with a malformed script.

From Google's side of things, you're ready to go.

## Starting a Python project
First, you need to install the
[Google API Python client](https://developers.google.com/api-client-library/python/). I
use [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
for scripts so I can package dependencies, so my requirements.txt looks like:

    pyopenssl
    google-api-python-client

For service accounts, you need to use SignedJwtAssertionCredentials, which
needs pyopenssl to work. For details, see
[this](http://stackoverflow.com/questions/14063124/importerror-cannot-import-name-signedjwtassertioncredentials),
or just include it.

My script isn't too different from jaco's example, however I added a few
more things to get you started.

```
#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
"""
Extract a snapshot of Google Analytics data.
"""

from apiclient.discovery import build

from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.file import Storage

import httplib2

PRIVATE_KEY = '<...>.p12'  # where you store your private key
GSERVICE_EMAIL = '<...>@developer.gserviceaccount.com'
SITE = 'ga:<...>'  # eg. ga:1234

SCOPE_FEEDS = 'https://www.google.com/analytics/feeds/'
CREDENTIALS_STORE = 'credentials.dat'  # credentials cache file


def authorize(private_key_filename,
              service_email,
              scope,
              credentials_store=CREDENTIALS_STORE):
    """Authorise a service account against Google APIs"""
    http = httplib2.Http()
    storage = Storage(credentials_store)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        key = None
        with open(private_key_filename, 'rb') as f:
            key = f.read()

            credentials = SignedJwtAssertionCredentials(service_email,
                                                        key,
                                                        scope=scope)
            storage.put(credentials)
    else:
        credentials.refresh(http)

    http = credentials.authorize(http)
    return http


def print_data_table(results, trim=True):
    """Given the results from a query, print to screen."""
    if trim:
        format_str = '%25.24s'
    else:
        format_str = '%25s'

    if results.get('rows', []):
        # Print headers.
        output = []
        for header in results.get('columnHeaders'):
            output.append(format_str % header.get('name'))
        print ''.join(output)

        # Print rows.
        for row in results.get('rows'):
            output = []
            for cell in row:
                output.append(format_str % cell)
            print ''.join(output)
    else:
        print 'No Results Found'

def print_top_pages(service, site, start_date, end_date, max_results=10):
    """Print out top X pages for a given site."""
    query = service.data().ga().get(
        ids=site,
        start_date=start_date,
        end_date=end_date,
        dimensions='ga:hostname,ga:pagePath',
        metrics='ga:pageviews',
        sort='-ga:pageviews',
        filters='ga:hostname!=localhost',
        max_results=max_results).execute()

    print_data_table(query)


if __name__ == '__main__':
    http = authorize(PRIVATE_KEY, GSERVICE_EMAIL, SCOPE_FEEDS)
    service = build(serviceName='analytics', version='v3', http=http)

    # TODO(gmwils): check if service is valid before continuing
    start = '31daysAgo'
    end = 'yesterday'

    print 'Top 10 pages'
    print_top_pages(service, SITE, start, end, 10)
```

This structure gives a good starting point for playing around with different
queries.

I did run into an issue where credentials wouldn't refresh from the
cache. This has been
[fixed](https://code.google.com/p/google-api-python-client/issues/detail?id=328),
but may need to patch manually.


## Calling Google Analytics from the API
There is a lot of different things you can extract from GA [Core Reporting API](https://developers.google.com/analytics/devguides/reporting/core/v3/). I found it
very helpful to start with the
[common queries](https://developers.google.com/analytics/devguides/reporting/core/v3/common-queries)
provided as examples.

There are also some
[API](https://developers.google.com/apis-explorer/#p/analytics/v3/)
[explorers](http://ga-dev-tools.appspot.com/explorer/) that help with trying
queries out.

For extracting data out of the results, there is [example code](https://developers.google.com/analytics/devguides/reporting/core/v3/coreDevguide#working),
and details on the [response fields](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#response_fields).

I found that I was often using filters to get at the data I wanted, and the
filter syntax is [documented](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#filters).

Some examples I found useful:

    filters='ga:hostname!=localhost'  # exclude development data
    filters='ga:source=~email'  # only email campaigns
    filters='ga:source=~email;ga:campaign=~^\w'  # email campaigns, with a non-blank campaign tag

To avoid date arithmetic in Python, the API also allows
[relative dates](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#q_details),
so you can write things like:

    start = '31daysAgo'
    end = 'yesterday'

You can use the dimensions tag to split by additional fields, such as
`ga:campaign` or `ga:date`.

There are various selectors that can be used in queries, including ones for
custom variables, goals and dimensions. Our conversion team has several custom
goals setup, so I can query for the results using:

    metrics='ga:goal07Completions,ga:goal07Starts,ga:goal07ConversionRate'

I feel like I'm only scratching the surface with Google Analytics every time I
use it. Figuring out scripting allows me to dig into further integrations for
our normal workflows.
