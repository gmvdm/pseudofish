Title: Java interop with Clojure and Mahout
Date: 2011-08-24 02:13
Author: gmwils
Category: clojure

While porting a simple example of generating a Hadoop file for Mahout, I
came across a number of edge cases of the Clojure [Java interop][].

### Nested Classes

Java allows for classes to be nested. However, Clojure doesn't provide
an obvious way of referencing them.

For example, Hadoop's [SequenceFile][] includes SequenceFile.Writer and
SequenceFile.Reader.

To access these in Clojure, the period is replaced by a dollar sign.

For [example][]:

    :::clojure
    (ns example
      (:import [org.apache.hadoop.io SequenceFile$Writer]))

    ...
      writer (SequenceFile$Writer. fs conf path
                                   (class Text)
                                   (class VectorWritable))
    ...

[This thread][] on the mailing list has some more details.

### Generics

From the Java code, generics add annotations about the type. However, at
the JVM level, generics are nowhere to be seen. It turns out that
generics are a compiler level feature only.

What this means for Clojure is that you can safely ignore them, provided
that you honour the types that are included in the generic.

Thus the following Java:

    :::java
    List<NamedVector> apples = new ArrayList<NamedVector>();

Can be written in Clojure:

    :::clojure
    (def apples (ArrayList.))

The responsibility is then on the programmer to ensure the types put
into the collection.

[This thread][1] on the mailing list has some background.

### Primitive Arrays

I started out looking at how to construct a `double[]` to pass to
[DenseVector][].

Turns out that there are a number of things to be wary of when
constructing primitive arrays. [Bradford Cross][] has written this up
with examples in [a blog post][].

The considerations I took away were:

1.  `double-array` function to migrate a Clojure data structure
2.  `make-array` with `Double/TYPE` to pre-allocate the array
3.  Type hints should be considered
4.  Odd things are likely to be happening with type coercion, so check
    run time performance.

  [Java interop]: http://clojure.org/java_interop
  [SequenceFile]: http://hadoop.apache.org/common/docs/current/api/org/apache/hadoop/io/SequenceFile.html
  [example]: https://github.com/gmwils/mahoutinaction/blob/master/src/mahoutinaction/ch08.clj
  [This thread]: http://groups.google.com/group/clojure/browse_thread/thread/3f86ac8939ef970c
  [1]: http://groups.google.com/group/clojure/browse_thread/thread/39ee5e1c8e9dab44?pli=1
  [DenseVector]: http://search-lucene.com/jd/mahout/math/org/apache/mahout/math/DenseVector.html#DenseVector(double[])
  [Bradford Cross]: http://measuringmeasures.com/bradfordcross/
  [a blog post]: http://measuringmeasures.com/blog/2010/3/27/fast-clojure-vectors-and-multidimensional-arrays.html
