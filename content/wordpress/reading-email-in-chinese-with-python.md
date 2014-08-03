Title: Reading email in Chinese with Python
Date: 2012-10-15 16:41
Author: gmwils
Category: python

Read email from a mailbox, in Chinese, with Python. Sounded easy.

After playing at the python prompt and many Google searches later, still
no success. Then, I found [two][] [articles][] that helped.

Turns out that there are a few tricks to getting email parsing to work
properly for multi-byte languages.

So, if you end up with strings something like:

    =?GB2312?Q?Qingwen_Word_List:_=D3=D0=D2=E2=CB=BC=B5=C4=B4=CA?=

Or:

    =CA=AF[=CA=AF] sh=A8=AA =A2=D9 rock =A2=DA stone =A2=DB stone inscription =A2==DC one of the eight ancient musical instruments =B0=CB=D2=F4[ba1 yin1]=20=C0=BC=BB=A8[=CCm=BB=A8] l=A8=A2nhu=A8=A1 =A2=D9 cymbidium =A2=DA orchid=20


Then, you'll need two different approaches. One for the header strings,
and one for the body text.

Given an [email][] message, either from a string or file:

    :::python
    from email import header
    import email
    msg = email.message_from_string(str_msg)


Then, headers can be read using something like:

    :::python
    subject, encoding = header.decode_header(msg['Subject'])[0]
    print subject.decode(encoding)

Which gives:

    :::python
    Qingwen Word List: 有意思的词

In this case, the encoding can be read from the email message and is
'gb2312'.

The body text needs a slightly different approach:

    :::python
    print unicode(msg.get_payload(decode=True), msg.get_content_charset(), 'replace')

For:

    石[石] shí ① rock ② stone ③ stone inscription ④ one of the eight ancient musical instruments 八音[ba1 yin1]
    兰花[?花] lánhuā ① cymbidium ② orchid...


The ['replace'][] option will mark unknown characters using U+FFFD,
rather than throw an exception.


This approach should work for most languages. Getting the various
decodings sorted out allowed me to move forward on a project I'm working
on. Now to re-implement it test first.


I know the format of the emails coming in, so can ignore multi-part MIME
messages. If you are looking for some more details on how to handle
them, check out [this article][two].

If you were curious about the =DA encoding, it is called
[quoted-printable][] ([RFC][]).


  [two]: http://ginstrom.com/scribbles/2007/11/19/parsing-multilingual-email-with-python/
  [articles]: http://lobstertech.com/python_unicode.html#hands_on_with_asian_spam
  [email]: http://docs.python.org/library/email.html
  ['replace']: http://docs.python.org/library/functions.html?highlight=unicode#unicode
  [quoted-printable]: http://en.wikipedia.org/wiki/Quoted-printable
  [RFC]: http://tools.ietf.org/html/rfc2045#section-6.7
