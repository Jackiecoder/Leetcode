class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_map = {}
        res = []
        for name in names:
            if name in name_map:
                # update name: (k + 1)
                # update name[:-3] : (k + 1)
                # k + 1 is the first available number for file name

                k = name_map[name] + 1
                while f'{name}({k})' in name_map:
                    k += 1
                name_map[name] = k
                name = f'{name}({k})'
            name_map[name] = 0
            res.append(name)
        return res
