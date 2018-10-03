"""
Author  => v1siuol
Date    => 2018.06.01

"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        search_index = 0
        n = len(S)
        part = [0]  # 0:
        shuzi = [0 for _ in S]
        done_list = []


        while search_index < n:
            while search_index < n-1 and S[search_index] in done_list:
                search_index += 1


            search_key = S[search_index]
            done_list.append(search_key)
            i = search_index

            

            while i < n and S[:].find(search_key, i+1) != -1:
                # wei
                part.append(i)
                i = S[:].find(search_key, i+1)
            else:
                
                temp = i

            for i in part:
                shuzi[i] = temp
                print(temp)

            part = []
            search_index += 1

        print(shuzi)
        print(S)

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
