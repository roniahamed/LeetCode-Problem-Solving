class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {'a':0}
        partition_sizes = []
        for i,char in enumerate(s):
            last_index[char] = i

        partition_end = 0
        partition_start = 0

        for i, char in enumerate(s):
            partition_end = max(partition_end, last_index[char])

            if i == partition_end:
                partition_sizes.append(i-partition_start + 1)
                partition_start = i + 1
        return partition_sizes
        