import math
class Node():
    '''
    Node of BinaryTree. Stores value, links to two descendants, and to ancestor.
    '''
    def __init__(self, value=0):
        '''
        :param value: value of Node (default 0)
        :L, R: Nodes, descendants
        :anc: ancestor
        '''
        self.value = value
        self.L = None
        self.R = None
        self.anc = None


class BinaryTree():
    '''
    Binary Tree.
    Each leaf has two None descendants, root have a None ancestor.
    The class stores additional attributes for LCA requests.
    _order: list of keys in traversal order.
    _heights: list of heights in traversal order.
    _first_meeting: dict stores first meeting in _order list for each key.
    _rmq: Sparse Table for the _heights list.
    '''
    def __init__(self, a=[]):
        '''
        :param a: list (default [])
            List with initial values which are contained in binary tree firstly.
            a[0] is a root value
            a[2*i+1], a[2*i+2] are values of i_th node's descendants, None is used for missing values
        '''
        self.root = self._build_tree(Node(), None, 0, a)
        # BinaryTree attribute list of keys in traversal order
        self._heights = []
        # BinaryTree attribute list of heights in traversal order
        self._order = []
        # BinaryTree method computes _heights and _order
        self._dfs(self.root, 0)
        self._first_meeting = {self._order[i].value: i for i in range(len(self._order))}
        self._rmq = SparseTable(self._heights)

    def _build_tree(self, T, anc, i, a=[]):
        '''
        Recursive build binary tree function.
        :param T: current Node
        :param anc: ancestor of the current Node
        :param i: index of current Node in the list
        :param a: list (default [])
            List with initial values
            a[0] is a root value
            a[2*i+1], a[2*i+2] are values of i_th node's descendants
        :return:
            Root of the result binary tree.
        '''
        if i >= len(a) or a[i] is None:
            return None
        T.value = a[i]
        T.anc = anc
        T.L = self._build_tree(Node(), T, 2*i+1, a) #left descendant
        T.R = self._build_tree(Node(), T, 2*i+2, a) #right descendant
        return T

    def _dfs(self, T, h):
        '''
        Depth first search. Precomputing for LCA queries.
        :param T: current Node
        :param h: current height
        :return:
        '''
        if T is None:
            return
        self._dfs(T.L, h+1)
        self._order.append(T)
        self._heights.append(h)
        self._dfs(T.R, h+1)

    def _find_ancestors(self, T):
        '''
        Recursive find ancestors function.
        :param T: current Node
        :return: list of ancestors values
        '''
        if T is None:
            return []
        return [T.value] + self._find_ancestors(T.anc)

    def LCA(self, U, V):
        '''
        Find LCA of two Nodes
        :param U, V: Nodes
        :return: Node, least common ancestor of U and V
        '''
        if U is None:
            return None
        if V is None:
            return None
        i = self._first_meeting[U.value]
        j = self._first_meeting[V.value]
        return self._order[self._rmq.get_min(min(i, j), max(i, j))]

    def LCA_value(self, U, V):
        '''
        Find LCA of two Nodes
        :param U, V: Nodes
        :return: value of Node - least common ancestor of U and V
        '''
        if U is None:
            return None
        if V is None:
            return None
        return self.LCA(U, V).value

class SparseTable():
    '''
    Sparse table.  Data structure allows answering range minimum queries.
    Memory: O(N log N)
    Precomputing: O(N log N)
    Query: O(1)
    '''
    def __init__(self, a=[]):
        '''
        Build sparse table.
        :param a: list (default [])
            List with initial values.
        '''
        self._values = a
        self._st = [list(range(len(a)))]
        self.N = len(a)
        self.K = math.ceil(math.log(len(a))) #max power
        for j in range(1, self.K + 1): #currency power
            #print(self._st[-1])
            self._st.append([])
            for i in range(self.N - 2**j + 1):
                #print(i, i + 2**(j-1))
                if a[self._st[j-1][i]] <= a[self._st[j-1][i + 2**(j-1)]]:
                    self._st[j].append(self._st[j-1][i])
                else:
                    self._st[j].append(self._st[j-1][i + 2**(j-1)])
        #print(self._st)

    def get_min(self, l, r):
        '''
        Index of min value in sequence [l, r]
        :param l: left border
        :param r: right border
        :return: index of min
        '''
        k = math.floor(math.log(r - l + 1, 2))
        if self._values[self._st[k][l]] < self._values[self._st[k][r - 2**k + 1]]:
            return self._st[k][l]
        else:
            return self._st[k][r - 2**k + 1]