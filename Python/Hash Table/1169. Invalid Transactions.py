class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        T = []
        for t in transactions:
            temp = t.split(',')
            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            T.append(temp)

        invalidT = []
        for t in T:
            if t[2] > 1000:
                t[1] = str(t[1])
                t[2] = str(t[2])
                invalidT.append(','.join(t))
                continue
            for x in T:
                if t[0] == x[0] and abs(t[1] - int(x[1])) <= 60 and t[3] != x[3]:
                    t[1] = str(t[1])
                    t[2] = str(t[2])
                    invalidT.append(','.join(t))
                    break

        return invalidT

    def invalidTransactions_need_debug(self, transactions: List[str]) -> List[str]:
        # questions:
        #  1. if last transaction is invalid, could we don't consider it as a transaction for next transaction?
        #       e.g. ["alice,20,800,mtv","alice,50,1200,mtv", "alice,81,200,beijing"]
        #       the second transaction is already invalid, the thrid one should be valid?
        #     A: invalid

        # hash table to store all transaction info, because hash table is convenient to inquery a person name
        # {name: {time: (amount, location)}}
        # {name: largest time}
        # transaction must be sorted
        # time O(n logn)

        trans = [tran.split(',') for tran in transactions]
        # trans = [[tran[0], int(tran[1]), tran[2], tran[3]] for tran in trans]
        # str, int, str, str
        trans.sort(key=lambda x: int(x[1]))
        trans_info = defaultdict(lambda: defaultdict(list))
        largest_time = {}
        invalid = set()
        for tran in trans:
            name, time, amount, location = tran
            # print(tran)
            # if name in trans_info:
            #     print(trans_info[name])
            # if name in largest_time:
            #     print(largest_time[name])
            if int(amount) > 1000:
                invalid.add(','.join(tran))
            if name in largest_time:
                lgt = largest_time[name]
                if int(time) - int(lgt) <= 60 and location != trans_info[name][lgt][1]:
                    invalid.add(
                        ','.join([name] + [str(lgt)] + trans_info[name][lgt]))
                    invalid.add(','.join(tran))
            trans_info[name][time] = [amount, location]
            largest_time[name] = time
            # print(invalid, '\n')
        tmp = []
        # 164, 714, 803
        for i in invalid:
            i = i.split(',')
            if i[0] == 'iris':
                tmp.append(i)
        print(sorted(tmp, key=lambda x: int(x[1])))
        return list(invalid)
