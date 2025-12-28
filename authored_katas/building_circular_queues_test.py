import codewars_test as test
import random


class ReferenceQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def enqueue(self, x):
        if len(self.data) < self.capacity:
            self.data.append(x)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def is_full(self):
        return len(self.data) == self.capacity

    def is_empty(self):
        return len(self.data) == 0


@test.describe("Randomized Circular Queue Tests")
def _():

    @test.it("Random operation sequences")
    def _():
        for _ in range(50):  # 50 independent runs
            cap = random.randint(1, 10)
            q = CircularQueue(cap)
            ref = ReferenceQueue(cap)

            for _ in range(200):  # 200 random operations per run
                op = random.choice(["enqueue", "dequeue", "check"])

                if op == "enqueue":
                    value = random.randint(0, 100)
                    if not ref.is_full():
                        ref.enqueue(value)
                        q.enqueue(value)

                elif op == "dequeue":
                    if not ref.is_empty():
                        expected = ref.dequeue()
                        actual = q.dequeue()
                        test.assert_equals(actual, expected)

                else:
                    test.assert_equals(q.is_full(), ref.is_full())
                    test.assert_equals(q.is_empty(), ref.is_empty())