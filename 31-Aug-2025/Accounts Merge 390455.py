# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N  = len(accounts)
        uf = UnionFind(N)
        email_gp_map = {}

        for i in range(N):
            for j in range( 1, len( accounts[i] ) ):
                if accounts[i][j] in email_gp_map:
                    uf.union( i, email_gp_map[ accounts[i][j] ] )
                else:
                    email_gp_map[ accounts[i][j] ] = i

        merged_accounts: List[List[str]] = [ [] for _ in range(N) ]

        for email, gp in email_gp_map.items():
            merged_accounts[ uf.find(gp) ].append( email )

        return [
            [ accounts[i][0] ] + sorted( merged_accounts[i] )
            for i in range(N)
            if merged_accounts[i]
        ]

class UnionFind:
    def __init__(self, N: int):
        self.parents = [-1] * N

    def union( self, src: int, dest: int ) -> bool:
        p_src, p_dest = self.find(src), self.find(dest)

        if p_src == p_dest:
            return False

        if abs(self.parents[p_src]) < abs(self.parents[p_dest]):
            p_src, p_dest = p_dest, p_src

        self.parents[p_src] += self.parents[p_dest]
        self.parents[p_dest] = p_src

        return True

    def find( self, node: int ) -> int:
        root = node

        while self.parents[root] > 0:
            root = self.parents[root]

        while self.parents[node] > 0:
            cur_parent = self.parents[node]
            self.parents[node] = root
            node = cur_parent
        
        return root