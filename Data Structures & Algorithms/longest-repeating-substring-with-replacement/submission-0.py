class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_output = 0
        freq_dict = {}

        for i in range(len(s)):
            freq_dict[s[i]] = freq_dict.get(s[i], 0) + 1
            window_size = i - left + 1
            max_freq = max(freq_dict.values())

            while window_size - max_freq > k:
                freq_dict[s[left]] -= 1
                left += 1
                window_size = i - left + 1

            max_output = max(max_output, i - left + 1)


        return max_output
        