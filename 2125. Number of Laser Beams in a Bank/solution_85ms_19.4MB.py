class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_row_devices_count = 0
        current_row_devices_count = 0
        beams = 0
        for r in range(len(bank)):
            devices_count = bank[r].count('1')
            if devices_count > 0:
                beams += devices_count * prev_row_devices_count
                prev_row_devices_count = devices_count
        return beams
        
#  Runtime 85 ms Beats 93.55% Memory 19.4 MB Beats 19.52%
