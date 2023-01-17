import heapq

def merge_lists(lists):
    merged_list = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        merged_list.append(val)
        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print(merge_lists(lists))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]