.. post:: 2024-08-08
   :tags: gsoc, pvlib, python
   :category: GSoC-2024

GSoC progress update: coming to the end
=======================================

Last contributions to pvlib-python have been slow-paced, but that's understandable since the amount of remaining GSoC proposals was decreased to the astonishing number of zero. Nevertheless, there is a small surprise in there.

The proposal of adding 3D shading calculations to pvlib-python was decided not to continue working on it. The main reason was that this kind of procedures don't fit well with the current library purposes and maintenance in the mid- and long-term would be difficult. In the future I may still work on it, as a stand-alone package, possibly on some other programming language, but for now it's not a priority.

And now, let's talk about the surprise; Chris Deline, the first author of a model of power yield correction due to uneven distribution of backside irradiance in bifacial PV modules, has requested to compare his model with the one I implemented - and was already merged. This model is a polynomial fit to the Relative Mean Absolute Difference (RMAD) of the total irradiance, assuming a concrete distribution of the backside irradiance. Now, the surprise: we all know about the difference between "Error" and "Difference", right? Well, mathematicians invented yet another word for a similar concept, "Deviation". I copy-pasted some implementation on the Internet that calculated the RMAD as the "Deviation" of the input data, instead of the "Difference". This big mistake has been fixed in an addendum branch without any further consequences.

Additionally, from the comparison, we have found that the implementation the author asked me to compare with had an issue with the units input and output. I have fixed that too, and now we are waiting for the author to review the changes.

Now I'm using my spare time to maintain SciencePlots thanks to all I learnt through this journey; currently adding a minimal test suite and a documentation webpage in the future.

Regarding pvlib, I'll possibly hunt small issues in the code -with a linter- for the contributing-to-pvlib workshop at PVPMC in Copenhagen, can't wait!
