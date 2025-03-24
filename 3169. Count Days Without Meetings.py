class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = 0
        track = 0
        for meet in meetings:
            if track > meet[1]:
                continue
            if meet[0] > track:
                count += meet[0] - (track+1)
            track = meet[1]
        count += days - track
        return count