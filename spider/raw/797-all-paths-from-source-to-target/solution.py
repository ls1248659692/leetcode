class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        gh,n,paths,tg = graph,len(graph),[[0,e] for e in graph[0]],[]
        while paths:
            _paths,paths =paths[:],[]
            for pa in _paths:
                if pa[-1]==n-1: 
                    tg.append(pa[:])
                else:
                    paths += [pa + [nd] for nd in gh[pa[-1]]]
        return tg