from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

print('********************************************')

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.popleft()
q.pop()
print(q)

print('********************************************')

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值

print('********************************************')

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict的Key是有序的

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


q = LastUpdatedOrderedDict(5)
q['1'] = 'l'
q['2'] = 'u'
q['3'] = 'o'
q['4'] = 'j'
q['5'] = 'i'
q['6'] = 'n'
print(len(q))

print('********************************************')

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
