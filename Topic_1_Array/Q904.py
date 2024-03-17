class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left_pointer = 0
        right_pointer = 0
        max_length = 0
        basket = collections.defaultdict(int)

        while right_pointer < len(fruits):

            basket[fruits[right_pointer]] += 1

            if len(basket) == 3:
                max_length = max(max_length, right_pointer - left_pointer)

            while len(basket) == 3:
                left_pop = fruits[left_pointer]
                basket[left_pop] -= 1
                left_pointer += 1

                if not basket[left_pop]:
                    basket.pop(left_pop)

            right_pointer += 1

        max_length = max(max_length, right_pointer - left_pointer)

        return max_length