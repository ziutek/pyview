## kview counterpart for web.py templates

It is probably the simplest useful module I have written in Python. It contains
only 21 lines of code.

I created it for my first Python application written after a long time working
with Go exclusively. Previously I haven't thought that I need something like this
for my web coding in Python, but after I was using
[kview](https://github.com/ziutek/kview) a lot in my previous work, it became
natural to create web page using small and reusable modules in simple and clean
way.

Previously, when I've used *web.py* templates, I usually used *base* attribute
of *web.template.render* function to define layout of the page. But defining
the layout of the whole web site in separate Python file seems to be more
elegant. Additionally, thanks to *pyview* I can decide myself when exactly to
read my templates from disk (it is virtually impossible with
*render* function - you must use *frender* function but it doesn't accept *base*
attribute).
