Title: Deleting Google Mail
Date: 2008-02-09 11:41
Author: gmwils
Category: Musings, Technology

Of late I've noticed that deleting mail on my GMail account doesn't
always work. Delete a message, check mail, and there it is back again.
Very frustrating.

Google took some time to actually add the ability to delete mail. Their
theory was that if you had enough storage, you shouldn't need to delete
mail. And to find anything, you can just search.

In theory, that works just fine. In practice, users like being able to
delete some mails. The ones I like to delete, aside from junk, are the
notification [mails][] from on-line services. I want to receive them, I
don't want to keep them.

In actual fact, most of the email I receive in my Google account are
specifically these mails. I don't pollute my normal email address with
them. Thus, the deleting issue causes me some problems.

It does make sense why Google struggles with deleting mail. Their
servers are massively redundant, housed in farms. To my understanding
their mail store is built on the same platform as their search tool.
This would mean that multiple copies are kept of all your mail.

When you ask to retrieve mail, a parallel query would be issued to the
farm. The results would then be collated and returned to you in the
GMail user interface. Simple enough.

Except, when you delete a mail, it now needs to be deleted in multiple
locations. So if you hit delete, it sends out the delete command to the
parallel server farm. Being a delete, it may take a bit longer to
process than a query, as the farm is optimized for queries. They are a
search company after all.

So while the delete command is being run, my refresh command is run to
find any new mail. Unfortunately, it would find some of the mail I had
asked to be deleted, but had yet to actually delete.

At least this is my theory on why deleted mail keeps popping back into
my Inbox. Even if my theory is right, it doesn't make it less annoying.

</p>

  [mails]: http://en.wikipedia.org/wiki/Bacn_(electronic)
