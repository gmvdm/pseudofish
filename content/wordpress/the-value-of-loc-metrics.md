Title: The Value of LOC Metrics
Date: 2007-02-13 15:06
Author: gmwils
Category: Technology

Two interesting things turned up for me around the same time that have
ended up linked. The first is the concept of using Lines of Code (LOC)
to improve [estimates][]. There are a bunch of things you can use LOC as
a proxy for during the estimation process.

The second area is using LOC analysis to improve QA time spent.
Microsoft has been doing a bunch of research that culminated in a
[paper][] that uses the relative change in LOC (churn) of a software
project to determine the most likely place bugs will occur.

> A case study performed on Windows Server 2003 indicates the validity
> of the relative code churn measures as early indicators of system
> defect density. Furthermore, our code churn metric suite is able to
> discriminate between fault and not fault-prone binaries with an
> accuracy of 89.0 percent.

The counting of LOC should be entirely possible. The analysis of that
data may take a bit more fiddling, but is work that needs to be done
once. It can then be built into the configuration management process for
the development team. The next step is then integration of the data into
a task/bug/issue tracking system to link in with estimates.

Microsoft has found a strong correlation between relative code churn and
where bugs appear. Industry research backs up using LOC for estimation.
Definitely an interesting thing to start experimenting with.

If I manage to stay in one place for long enough, stay tuned for my
experiences with this in practice. Reality may struggle to meet my
current levels of excitement, but if the results are even a small
improvement I'll be happy.

  [estimates]: http://pseudofish.com/blog/2007/01/23/the-black-art-of-software-estimation/
  [paper]: http://research.microsoft.com/research/pubs/view.aspx?type=Publication&id=1359
