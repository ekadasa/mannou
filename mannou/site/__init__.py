# -*- coding: utf-8 -*-

"""Main parser package for parsing sites.

Every class in this package will be responsible for specific manga site.

Note
----
Parser class **MUST** be inherit `mannou.parser.Manga` to ensure every parser
have the same functionality.

Guideline
---------
* Make sure parser class inherit `mannou.parser.Manga`.
* Implement all abstract method.
* All implemented abstract method **MUST** return.
  an expected object specified in `super().__doc__`.
* It strongly recommended if `number` attribute.
  from :obj:`mannou.parser.Chapter` is a cardinal number.
* You must override `super().filter_chapters()` if the parse do not adhere
  rule above.

"""
