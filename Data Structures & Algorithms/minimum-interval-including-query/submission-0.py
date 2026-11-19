class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        ordered_queries = []
        for index, query in enumerate(queries):
            ordered_queries.append((query,index))
        
        ordered_queries.sort()

        answers = [-1] * len(queries)
        heap = []
        next_interval = 0

        for query, original_index in ordered_queries:
            while next_interval < len(intervals) and intervals[next_interval][0] <= query:
                left, right = intervals[next_interval]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                next_interval += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            if heap:
                answers[original_index] = heap[0][0]
        return answers

        