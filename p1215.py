# -*- coding: utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict

q=deque(['a','b','c','d'])

q.append('M')
q.appendleft('L')
print(q[3])

Point=namedtuple('Point21M',('x','y'))
p=Point(2,6)
print(p.x)

dd=defaultdict(lambda: 'N/A')
#dd={'k1':90,'k2':21,'k3':'mpt8'}
print(dd['key2'])

print("LPE")
print("lpe2")
print("lpe3")