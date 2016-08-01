# Pseudofish blog

My blog, using Pelican, a static site generator.

https://github.com/getpelican/pelican

## Setup
First, get python, virtualenv, autoenv, etc working.

Then:

```
pip install pelican markdown typogrify
make devserver
...
./develop_server.sh stop
```

Then open the [dev blog](http://localhost:8000/), changes are updated
automatically when editing local files.

## Writing
Some useful articles:

* [How to write a good blog post](http://om.co/2016/03/26/how-to-write-a-good-blog-post/}

## Images
Images optimised using [ImageOptim](https://imageoptim.com/command-line.html):

```
open -a ImageOptim content/images
```

## Drafts
Drafts can be viewed on: http://localhost:8000/drafts
