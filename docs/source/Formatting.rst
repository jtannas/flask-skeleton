Formatting
==========

PEP8 is a document that outlines the baseline style for python code.
It seems people are pretty happy with it, so that's what this project
uses.

I am lazy and fallible though, so I avoid formatting by hand. I use a
tool called YAPF that formats & beautifies code, with the default
settings corresponding to PEP8. It is configurable via the [style]
section of the setup.cfg file.

For linting (aka automated code review), I use pylint3. It is verbose
and very angry, often giving -13/10 scores to freshly made code. It's
usually right though, catching all the little things that slip past
people.

Both YAPF and PyLint3 can be selectively disabled via flags in the
files. When disabling them, you can limit the range of code they are
disabled for. Please disable sparesely though, and not before weighing
the  costs and benefits. Consistent with the standard is better than
your personal opinion of perfection.

