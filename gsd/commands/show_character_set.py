#!/usr/bin/env python

"""cat data/train/text | cut -f 2- -d ' ' | sed 's/./\0\n/g' |  sort -u | uconv -f utf-8 -t utf-8-x Any-Name | sed 's:\\N{<control-000A>}:\n:g' | wc -l"""