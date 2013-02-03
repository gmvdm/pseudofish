Title: Target - Finding Letters in Words
Date: 2005-12-07 05:55
Author: gmwils
Category: Haskell, Musings, Python

[Target][] - A simple word puzzle. The beginnings of pain. The basic
problem is a grid of nine letters printed in a newspaper. One of the
aims is to generate words using the central letter from the square. The
sub goal is to find the nine letter word that uses all of the letter.

</p>

The rules of the game are:

</p>

-   See how many words of four letters or more can you make from the
    letters shown in the grids.
-   In making a word, each letter must be used once only.
-   The word must contain the centre letter and there must be at least
    one nine-letter word in the list.
-   No plurals or verb forms ending with "s"; no words with initial
    capitals and no words with a hyphen or apostrophe are permitted. The
    first word of a phrase is permitted (eg inkjet in inkjet printer).
-   Words come from the main body of Chambers 21st Century Dictionary as
    the reference source.

</p>

And an example:

</p>
<!-- TODO: include photo -->

<table align="center" cellspacing="2" cellpadding="2" width="200" height="200" border="1" frame="box">
</p>
<p>
<tr>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">R</font>

</td>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">I</font>

</td>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">C</font>

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">U</font>

</td>
</p>
<p>
<td valign="middle" align="center" bgcolor="#000000">
<font color="#ffffff" face="arial,helvetica" size="+4">H</font>

</td>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">E</font>

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">R</font>

</td>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">N</font>

</td>
</p>
<p>
<td valign="middle" align="center">
<font face="arial,helvetica" size="+4">A</font>

</td>
</p>
<p>
</tr>
</p>
<p>
</table>
</p>

*Target: 15 words, good; 22 very good; 30 excellent.*

</p>

As a programmer, my inclination to solve these kind of problems is quite
low. Scrabble is one of my weaker games. Alas, I am also very
competitive, so when this became popular at a camp I volunteer at I was
motivated to improve.

</p>

The catch is that I'm a little bit lazy. The way to improve at the game
is to do lots of them. That doesn't sound like fun to me.

</p>

Last time, I used a very simple regular expression and scanned the
`words` list. I then manually filtered out the invalid words.

</p>

Having done a bit of Cocoa programming, I want to create a GUI version
of a solver for this puzzle. However, an approximate solver isn't good
enough. I need to be able to exactly solve the word puzzle.

</p>

Sitting around at the OSDC, I took the opportunity to try and write the
engine part.

</p>

A few attempts in Python and I worked out that for an algorithm such as
this, either the language or my understanding of it was insufficient for
experimentation. For this kind of problem, I tend to think of them
mentally in functional style. Fortunately, Haskell is installed on my
computer.

</p>

Firstly, I needed a function to check if a letter exists in a word:

</p>

<p>
    letterInWord :: Eq a => a -> [a] -> BoolletterInWord a [] = FalseletterInWord a (w:ws)    | a == w = True    | otherwise = letterInWord a ws

</p>

Given that a letter can only be used once in a target word, a function
that removes a letter from a word was needed:

</p>

<p>
    removeLetter :: Eq a => a -> [a] -> [a] -> [a]removeLetter l [] wss = wssremoveLetter l (w:ws) wss    | l == w    = ws ++ wss    | otherwise = removeLetter l ws (w:wss)

</p>

The two helper functions can then be glued together to determine if a
given word is contained in the letters of the second word:

</p>

<p>
    lettersInWord :: Eq a => [a] -> [a] -> BoollettersInWord [] [] = TruelettersInWord [] (w:ws) = TruelettersInWord (l:ls) [] = FalselettersInWord (l:ls) (w:ws)    | letterInWord l (w:ws) = lettersInWord ls (removeLetter l (w:ws) [])    | otherwise = False

</p>

This solution came together very quickly, but iterates twice through the
word. A bit more time in Hugs and the two helper functions become one:

</p>

<p>
    lettersInWord :: Eq a => [a] -> [a] -> BoollettersInWord [] [] = TruelettersInWord [] (w:ws) = TruelettersInWord (l:ls) [] = FalselettersInWord (l:ls) (w:ws)    | isInWord = lettersInWord ls remainingLetters    | otherwise = False    where (isInWord, remainingLetters) = removeLetterInWord l (w:ws) []removeLetterInWord :: Eq a => a -> [a] -> [a] -> (Bool, [a])removeLetterInWord l [] wss = (False, wss)removeLetterInWord l (w:ws) wss    | l == w    = (True, ws ++ wss)    | otherwise = removeLetterInWord l ws (w:wss)

</p>

This covers the basic search for words. It just misses a few of the
rules. It doesn't check if the middle letter is used and it doesn't
check word length. Something to add on a rainy day.

</p>

One question I have is whether or not I could do something like this in
Python. It is possible to write Python code to do this, but the more
interesting question is why I had mind block when attempting to use
Python. I suspect this is because I have spent longer using Haskell for
algorithms and tend to use Python as glue. Hopefully, [PyGame][] will
provide enough motivation to improve my Python coding.

</p>

Programmer efficiency aside, the next interesting question is how
efficient the two languages are. Performance will matter, as the intent
is to run this over a large dictionary of words. Interfacing into Python
or Objective C for use in a Cocoa GUI is another question.

</p>

Of course, this is pretty close to being an anagram solver. This is a
solved problem with many [free ones][] on the Internet. Luckily, I get a
kick out of solving the problem using my own program.

</p>

  [Target]: http://www.theage.com.au/entertainment/puzzles/target.html
  [PyGame]: http://www.pseudofish.com/blog/2005/12/06/pygame-on-mac-os-x-with-pyopengl/
  [free ones]: http://www.ssynth.co.uk/~gay/cgi-bin/nph-an?line=RICUHERNA&words=1&dict=antworth&doai=on
