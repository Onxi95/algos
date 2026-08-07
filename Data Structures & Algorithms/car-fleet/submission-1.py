class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        zipped = sorted(zip(position, speed), reverse=True)
        stack = [zipped[0]]
        
        for current_car in zipped[1:]:
            prev_car = stack.pop()
            reaches_before = self.reachesBeforeEnd(prev_car, current_car, target)
            if reaches_before:
                stack.append(prev_car)
            else:
                stack.append(prev_car)
                stack.append(current_car)


        return len(stack)

    def reachesBeforeEnd(self, car1: (int, int), car2: (int, int), target) -> bool:
        car1_end_distance = target - car1[0]
        car2_end_distance = target - car2[0]

        car1_end = car1_end_distance / car1[1]
        car2_end = car2_end_distance / car2[1]

        return car1_end >= car2_end