# სავარჯიშო 1 

def constant(items):
    steps = 0
    for item in items:
        steps += 1
        break  
    return steps


def linear(items):
    steps = 0
    for item in items:
        steps += 1
    return steps


def quadratic(items):
    steps = 0
    for a in items:
        for b in items:
            steps += 1
    return steps


# სავარჯიშო 2 — Stack (LIFO)

class Stack:
    def __init__(self):
        self._items = []

    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack ცარიელია")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


def reverse_text(text):
    stack = Stack()
    for char in text:
        stack.push(char)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())
    return "".join(result)


def is_palindrome(text):

    cleaned_text = "".join(text.lower().split())
    return cleaned_text == reverse_text(cleaned_text)


if __name__ == "__main__":
    print("სავარჯიშო 1")
    for n in (10, 100, 1000):
        data = list(range(n))
        print(f"n = {n}: O(1) = {constant(data)}, "
              f"O(n) = {linear(data)}, O(n²) = {quadratic(data)}")

    print("\nსავარჯიშო 2")
    print(reverse_text("Python"))
    print(reverse_text("გამარჯობა"))
    print(is_palindrome("Radar"))
    print(is_palindrome("Never odd or even"))
    print(is_palindrome("Python"))
