Title: Calculating earlier dates using a shell script
Date: 2011-10-07 01:40
Author: gmwils
Category: Technology

Mongo has a database size limit in 32 bit mode, so I want to purge out
items that are less than a certain date in the past. I decided that it
would be easy to write a simple shell script to run the query.

The tricky part was calculating dates in shell. This is what I ended up
with:

    ::shell
    #!/bin/sh
    MONTHS_AGO=3
    DATE_AGO_EPOCH=$((`date +%s` - $MONTHS_AGO * 31 * 24 * 3600))
    OSTYPE=`uname`
    FORMAT='+%Y-%m-%d'

    if [ "Linux" = $OSTYPE ] ; then
      DATE_AGO_ISO=`date -d "1970-01-01 00:00 UTC + $DATE_AGO_EPOCH seconds"
      $FORMAT`
    else
      DATE_AGO_ISO=`date -r $DATE_AGO_EPOCH $FORMAT`
    fi

    DB_CMD="db.items.find( { publish_date : { \$lt : \"$DATE_AGO_ISO\" } } ).count()"
    # DB_CMD="db.items.remove( { publish_date : { \$lt : \"$DATE_AGO_ISO\" } } )"

    echo $DB_CMD | mongo pz


This now provides a simple way of purging out old items that can be
called from cron.

