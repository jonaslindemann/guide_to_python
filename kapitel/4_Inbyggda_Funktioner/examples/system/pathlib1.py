# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import pathlib as pl

p = pl.Path('.')
p = p / "test"
print(p)

print(p.exists())

q = p.resolve()
print(q)


print(q.parts)
print(q.drive)

r = pl.Path.cwd()
print(r)

print(r.exists())
print(r.is_dir())
print(r.is_file())


s = pl.Path.home()
print(s)
