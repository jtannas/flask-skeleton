Formatting
==========

PEP8 is a document that outlines the baseline style for python code.
It seems people are pretty happy with it, so that's what this project
uses.

I am lazy and fallible though, so I avoid formatting by hand. There's
a tool made by Google called YAPF. It formats & beautifies code, with
the default settings corresponding to PEP8. it is configurable via the
[style] section of the setup.cfg file.

For linting (aka automated code review), I use pylint3. It is verbose
and very angry, often giving -13/10 scores to freshly made code. It's
usually right though, catching all the little things that slip past
people.

By YAPF and PyLint3 can be disabled, via flags in the files. Please do
this sparesely though, and not before weighing the costs and benefits.
When disabling them, you can limit the range of code they are disable
for.