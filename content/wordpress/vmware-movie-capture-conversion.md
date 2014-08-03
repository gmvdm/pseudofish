Title: VMWare Movie Capture & Conversion
Date: 2008-08-01 10:11
Author: gmwils
Category: technology

On a PC, I want to be able to easily capture screencasts for the
products we use at work. The ulterior motive is to be able to show a
video rather than repeat the demo hundreds of times.

VMWare gives a tantalizing option: *Capture Movie*

It is under the VM menu in the menu bar. Prompts for a filename and
you're away.

Slight catch. Playing back the movie that is recorded leads to not much
but trouble. Turns out that VMWare encodes the movie into a non-standard
video format. Details of it are [here][]. (It is using the VNC protocol
to encode the video with some VM specific headers)

If you've installed Workstation, the decoder for the codec is included.
Otherwise, you can download the codec [here][1]. I found you need to use
Microsoft Media Player to actually play back.

That still leaves the problem of editing the video. With the video
recorded and the codec installed, you can convert the video into a
suitable format. I used Prism's [conversion program][] to produce an AVI
that can be read by Final Cut Pro.

Final Cut Pro took a bit of effort, but produced a very slick result.
You can use simpler options for the video editing piece.

The result is that I can now capture video of demonstrations that are
run in a VMWare environment, and re-mix them into various screencasts.

  [here]: http://wiki.multimedia.cx/index.php?title=VMware_Video
  [1]: http://www.moviecodec.com/downloads/400d.html
  [conversion program]: http://www.nchsoftware.com/prism/index.html
