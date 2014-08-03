Title: Target (redux)
Date: 2005-12-18 14:31
Author: gmwils
Category: haskell

After having spent some of [last week][] solving the Target word problem
using Haskell, I thought I might try another language.

C++ is one of those languages that retains low level control and simple
machine semantics while providing high abstraction levels. The first
language I learnt, it is also the one I've used the most. I usually skip
it for attempting to understand an algorithmic problem, but once the
algorithm is well understood it can make a big speed difference.

As I've been pondering this from a productivity point of view, the
interesting bit is how I approached the problem. Fortunately, C++
includes pseudo functional constructs via the STL. This meant that I
could keep a reasonable level of abstraction. Loops replaced recursion,
as it is technically possible to use recursion in C++, it just doesn't
*feel* right.

The time spent building the C++ version was around the same time as for
the Haskell version. When run against a large dictionary of words
(234937), the Haskell version took around 4.5 seconds, with the C++
version taking just less than a second.

I believe there is still some optimisation space left in both programs.

Given a similar problem, I would pick Haskell to explore, even with a
slower result. For some reason, it was more fun to program against.

To continue this, I'm going to pick a trickier problem and try
implementation in multiple languages. In theory, there is a Cocoa to
Haskell binding ...

For future reference, my code looks like:

    :::c++
    #include <iostream>
    #include <iterator>
    #include <fstream>
    #include <vector>
    #include <set>

    using namespace std;

    bool containsWord(char const&, string const&, string const&);
    bool includesAllLetters(string const &, string const &);

    int main(int argc, char** argv) {
        string from, word;
        char letter;

        if(argc < 4) {
            cout << "usage: mainChar allLetters wordList\n";
            return 0;
        }

        letter = argv[1][0];
        word = argv[2];
        from = argv[3];

        ifstream is(from.c_str());
        istream_iterator<string> ii(is), eos;

        int count = 0;
        vector<string> targets;
        cout << "Words: ";
        for( ; ii != eos; ++ii)
            if(containsWord(letter, word, *ii)) {
                cout << *ii << " ";
                ++count;
                if(word.length() == (*ii).length())
                    targets.push_back(*ii);
            }

        cout << "\n";
        cout << "Found " << count << " words.\n";

        cout << "Targets: ";
        for(vector<string>::iterator p = targets.begin(); p!=targets.end(); ++p)
            cout << *p << " ";
        cout << "\n";

        return !is.eof();
    }

    bool containsWord(char const& c, string const &word, string const &testWord) {
        if(testWord.length() < 4 || testWord.length() > word.length() || testWord.find(c) == testWord.npos) return false;

        if(includesAllLetters(word, testWord)) return true;

        return false;
    }

    bool includesAllLetters(string const &word, string const &testWord) {
        string letters(word);
        for(string::const_iterator p = testWord.begin(); p !=testWord.end(); ++p) {
            size_t loc = letters.find(*p);
            if(loc == letters.npos)
                return false;
            else
                letters.erase(loc, 1);
         }

         return true;
     }

  [last week]: http://www.pseudofish.com/blog/2005/12/07/target-finding-letters-in-words/
