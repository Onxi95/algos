class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed or len(position) != len(speed):
            return 0

        def when_at_target(target, position, speed):
            # v = s / t
            # t = s / v
            left = target - position
            return left / speed

        cars = sorted(zip(position, speed), reverse=True)

        stack = [when_at_target(target, *cars[0])]

        for car in cars[1:]:
            curr_car = when_at_target(target, *car)

            if curr_car > stack[-1]:
                stack.append(curr_car)

        return len(stack)