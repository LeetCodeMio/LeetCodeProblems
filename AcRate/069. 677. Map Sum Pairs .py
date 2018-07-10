# 前缀树
class MapSum :
    def __init__(self) :
        self.root = {'val':None}
    def insert(self, key, val) :
        node = self.root
        for i in key : node = node.setdefault(i, {'val':None})
        node['val'] = val
    def sum(self, prefix) :
        node = self.root
        for i in prefix :
            if i not in node : return 0
            node = node[i]
        stack = [node]
        ret = 0
        while stack :
            node = stack.pop()
            if node['val'] : ret += node['val']
            stack.extend(v for k, v in node.items() if k != 'val')
        return ret