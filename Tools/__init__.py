# -*- coding: utf-8 -*-
# @Time    : 3/3/2025 1:31 PM
# @Author  : Ferdinando Crispino
# @Email   : ferdinando.crispino@usp.br
# @File    : __init__.py.py
# @Software: PyCharm

""""
The __init__.py files are required to make Python treat the directories as containing packages;
this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that
occur later on the module search path. In the simplest case, __init__.py can just be an empty file,
but it can also execute initialization code for the package or set the __all__ variable, described later.
"""