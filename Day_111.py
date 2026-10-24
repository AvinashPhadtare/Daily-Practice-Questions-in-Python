# ========================== Question =========================
#
# You are given an XML document of N lines.
#
# Your task is to print the tag name of the root element and the
# number of its direct children, separated by a space.
#
# Example:
#
# Input:
# 6
# <library>
# <book id="1">
# <title>Python</title>
# </book>
# <book id="2"/>
# </library>
#
# Root tag = library
# Direct children = 2 (both <book> elements)
#
# Output:
# library 2
#
# Important Point:
#
# ElementTree.fromstring() returns the root element. root.tag
# gives its name and len(root) gives the number of direct
# children.
#
# ============================================================

# ======================= Solution ==========================
import xml.etree.ElementTree as etree

n = int(input())
xml = "\n".join(input() for _ in range(n))

root = etree.fromstring(xml)
print(root.tag, len(root))
