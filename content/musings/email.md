Title: Rethinking how I handle email
Date: 2013-05-12
Author: gmwils
Summary: After being swamped with 3x previous email, looking at how to cope.

Email started to take too long, so I recently changed my approach.

At work, we try to avoid unbounded queues. In a distributed service
architecture, they can be toxic and swamp otherwise well behaving services.

Email had become an unbounded queue. It kept piling up and swamping my
day. Time for a change.

### My new process

I adapted
[the](http://www.manager-tools.com/2013/03/email-three-times-a-day-part-1)
[recommendations](http://www.manager-tools.com/2013/03/email-three-times-a-day-part-2)
from Manager Tools, and I now follow these guidelines:

1. Schedule 30mins in the morning for email.
2. No more than three time periods of up to 30mins during a day for email.
3. If I start processing email, I must finish (empty INBOX)

The key for me has been pushing myself to finish if I start. This means that a
spare five minutes cannot be spent _doing email_.

For things that I need to do, either I book time in my calendar or put an
entry in my [task list](http://culturedcode.com/things/), possibly with a
reminder.

When I end up with something that I want to come back to later, I'll create a
task to refer back to it, and park the email in a "Follow-up" folder.

For random notes to self, I now add a task. Previously, I was cluttering
my inbox and compounding my mail problem.

I also switched to using [Instapaper](http://www.instapaper.com/) for saving
articles from Twitter, also reducing emails to myself.

### Results

The last two weeks were a big improvement.

I am feeling less stressed by email, and more focused on important
activites. I also feel like I have more time to handle unexpected events and
to chat with colleagues.

I still catch myself checking email on occasion, however often my inbox is
empty, so I'm slowly weaning myself of the habit.

For personal email accounts, I'm using a similar approach, although with a
lower frequency of checking.

For my phone, I will occasionally check email there, and am a bit more relaxed
about the process. I also set all mail applications to only check mail when
manually asked.

### Measuring email volume

Below is a chart of the email volume over the last two years for my work
account. I was curious how much email I was receiving, and how much I sent.

For the last few months, I received around 3 times the number of emails as the
same period last year. This is a factor of being involved in more projects,
and the growth of the company. November last year was during a major project,
and spiked in the number of emails I received.

I was surprised to find that I still send the same number of emails (~10-15
per day).

![Email volume](|filename|/images/email-volume.png)

The chart was generated via the IMAP interface to Gmail, and this Python
script:

    :::python
    #!/usr/bin/env python

    import imaplib

    def count_of_search(M, query, mailbox='INBOX'):
        M.select(mailbox_name)

        status, email_ids = M.uid('search', None, r'(X-GM-RAW "%s")' % query)
        return len(email_ids[0].split(' '))

    mailbox_name = '[Gmail]/All Mail'
    user, passwd = 'user@example.com', 'secret'

    M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    M.login(user, passwd)

    print "Date,All Mail,Sent,Received"
    for year in [2012, 2013]:
        for month in xrange(1,13):
            date_query = 'after: %d/%d/1 before:%d/%d/31' % (year, month, year, month)
            all_mail_count = count_of_search(M, date_query, mailbox_name)

            sent_query = '%s from:%s' % (date_query, user)
            sent_mail_count = count_of_search(M, sent_query, mailbox_name)

            received_query = '%s to:%s' % (date_query, user)
            received_mail_count = count_of_search(M, received_query, mailbox_name)

            print "%d/%d/1, %d, %d, %d" % (year, month,
                                           all_mail_count,
                                           sent_mail_count,
                                           received_mail_count)

The tricky part was finding a way to pass the X-GM-RAW parameter through to
IMAP to enable Gmail
[search criteria](https://developers.google.com/google-apps/gmail/imap_extensions#extension_of_the_search_command_x-gm-raw). This
allows you to use the same search expressions as from within Gmail.
