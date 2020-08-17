import heapq


def Node():
    def __init__(self, name, val):
        self.company_name = name
        self.volume = val

    def __lt__(self, other):
        if self.volume < other.volume:
            return True
        return False


def top2Company(lists):
    company_node = {}
    heap = []
    for company, val in lists:
        if company not in company_node:
            company_node[company] = Node(company, -val)
        else:
            node = company_node[company]
            node.val = node.val - val
            company_node[company] = node
        heapq.heappush(heap, node)


lists = [('A', 3), ('B', 5), ('C', 3), ('D', 10), ('E', 8), ('F', 20)]
# lists = [('A', 3), ('B', 5), ('A', 3), ('C', 10), ('D', 8), ('B', 20)]
# A         BA        AB         CA         CD       BC
