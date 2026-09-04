class Solution:
    def leastInterval(self, tasks, n):
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] += 1

        max_freq = max(count)

        max_tasks = count.count(max_freq)

        result = (max_freq - 1) * (n + 1) + max_tasks

        return max(result, len(tasks))