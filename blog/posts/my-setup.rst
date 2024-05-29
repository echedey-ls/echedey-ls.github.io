.. post:: 2024-05-29
   :tags: gsoc, pvlib, python
   :category: GSoC-2024

My development stack
====================

Hi everyone! I'm going to talk a bit about how I work on the programming projects I'm involved with, and how I plan to continue working on GSoC. I hope this post helps you to improve your workflow, or at least to get to know me a bit better.

After many years trying different IDEs and languages (C/Cpp, VHDL, Matlab/Octave, PowerShell, Makefiles, LaTeX, G-Code, AWL, Go), most of them for university, I can safely state that I hate all and each one of the proprietary development environments I've tried. I'm looking at you, MPLAB X IDE, STMCube, Vivado, Siemens Step 7 and TIA Portal, and Matlab. Visual Studio is fine enough to tolerate it, but I still prefer Visual Studio Code.

I've been using it since 2018 or so, and the amount of extensions it has is just amazing. I've used it for (almost?) all of the mentioned languages and environments, and my go-to is install the propietary IDE only to configure and generate project files, sometimes even build it. Writing the code and formatting is always done in VS Code.

I don't want to be the VS Code fanboy, it still has some drawbacks I dislike, like that it's not fully open-source (Codium is the open-source build of it, thou it won't let you use some Microsoft extensions) and it's a bit slow. But it's the best I've found so far.

And finally, yeah, I use Windows. Believe, if I could switch to Linux permanently I would, but some of the academic software I need is only available for Windows.

The Python stack
----------------

If I had to summarize this section, it would be something along the lines of "There's always an extension for that". This is what I use the most, and what I will be using to develop during my GSoC participation. My current setup is:

- Python / Python debugger from Microsoft
- Pylance
- Ruff (for code formatting, allows formatting selection)
- Jupyter to run interactive code mostly, in early-stage development and develop Sphinx-Gallery examples
- Python Test Explorer for running tests (this is just AMAZING)
- Always using a virtual environment and an editable pip install

  .. code-block:: powershell

     python -m venv .venv
     .venv\Scripts\Activate.ps1
     python -m pip install -e .[test]

You may be wondering about the docs. Aha, I don't use anything for that! The neat part about contributing to well-established projects like pvlib-python is that CI/CD is already set up as another tool of the stack.
At least for me, the time invested and the amount of heat that comes out from my laptop are the two reasons that drive me insane when I try to build them. I only leave an embarrassing snail-trail of docstring commits in the PRs, but it's worth it.

There are a few more regarding Python (like the Jupyter alternative *Marimo*), but I haven't used them enough to have an opinion. I've also omitted some extensions that I recall are dependencies of the others.

Not to brag about it
^^^^^^^^^^^^^^^^^^^^

...but GitHub Copilot is incredible. I'm lucky to be able to use it without limitation, and it boosts my performance both at writing natural language (specially in English!) and code astonishingly. It has its flaws obviously, but once it understands what you're trying to do, it's just amazing. I think it's time to confess that most docstrings I write are done by it, and I just tweak them as I want. Not gonna lie, I end up doing a lot of changes, and missing others, but it's still a huge time saver.

Other tools
-----------

- GitHub Desktop for the win, easy and fast to use.
- Firefox with some bookmarked search engines and reference documentation pages.
- A remote Ubuntu server to test issues, thou I have used WSL2 too.
- Notepad++ for the todo list and some quick notes during meetings.

Handy links for y'all
^^^^^^^^^^^^^^^^^^^^^

- `VS Code <https://code.visualstudio.com/>`_
- Ever needed to write an rST docstring? `Here's a cheatsheet <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

I hope to have given some insight on how I work and help my GSoC colleagues to improve their workflow. I'm always open to suggestions and improvements, so feel free to reach out to me if you have any!


Non-Python development
----------------------
To give credit to all that work behind some software I use, before I can donate to them with my first salary:

- `KiCad <https://www.kicad.org/>`_ for PCB design
- `Microcap <https://web.archive.org/web/20230219052113/http://www.spectrum-soft.com/index.shtm>`_ free although proprietary circuit design and simulator, better than the OrCAD we had to use at university
- `Saber <https://github.com/saber-notes/saber/>`_ for hand-written notes in the tablet
- `RustDesk <https://rustdesk.com/>`_ for IT supporting my family and friends
- Mozilla's Firefox and Thunderbird, the best open-source browser and email client
- `Putty <https://putty.org/>`_ for SSH connections and server management
  Worth to mention the Python telegram and mail bots that send the public IP addresses, just letting that sink in.
- `Simplewall <https://github.com/henrypp/simplewall>`_, a simple and effective firewall
- `Zotero <https://www.zotero.org/>`_, the best bibliographic reference manager
- `SumatraPDF <https://www.sumatrapdfreader.org/free-pdf-reader.html>`_ for reading PDFs
- `GIMP <https://www.gimp.org/>`_ for image editing
- `IrfanView <https://www.irfanview.com/>`_ for quick image viewing

The list goes on, but I owe a lot of thanks to these tools and the people behind them. Thank you very much.
