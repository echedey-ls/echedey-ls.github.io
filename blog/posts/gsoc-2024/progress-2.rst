.. post:: 2024-06-27
   :tags: gsoc, pvlib, python
   :category: GSoC-2024

GSoC progress update: dependencies rant
=======================================

I was going to contribute my biggest PR, the direct beam shading factor via 3d
spatial calculus. I developed an OOP approach that uses `shapely` for the
geometric operations. However, thanks to an user thread on the mailing list, I
found that `solarfactors`, a dependency of `pvlib`, has pinned the maximum
version of `shapely` to anything lesser than 2.0.

This is a problem because I always try to use the latest versions of the
libraries I depend on. I have been developing on `shapely` all that code, and
now I have to refactor it to use the older version. Or, address an open issue
on `pvfactors` (the original repo of `solarfactors`) to remove the dependency.

What's more, nobody is able to install `solarfactors` on python 3.12 because of
the `setuptools` maximum pinned version of *that* `shapely` version.
Damn, wasn't python the perfect language to surf on the latest trends?
