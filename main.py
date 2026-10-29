from array_structures import ArrayStack, ArrayQueue
from linked_structures import LinkedStack, LinkedQueue


def is_balanced(expression):
    stack = LinkedStack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


def simulate_print_queue():
    queue = LinkedQueue()
    print("\\n--- Print Queue Simulation ---")
    queue.enqueue({"id": "JOB1", "pages": 2})
    queue.enqueue({"id": "JOB2", "pages": 5})
    queue.enqueue({"id": "JOB3", "pages": 1})

    position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Wait position {position}: Job {job['id']} ({job['pages']} pages)")
        position += 1


def test_structure(structure, kind):
    while True:
        print(f"\\nCurrent structure: {structure}")
        if kind == "stack":
            print("1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  0. Back")
        else:
            print("1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  0. Back")

        choice = input("Choose operation: ").strip()
        try:
            if choice == "0":
                break
            elif choice == "1":
                value = input("Enter value: ")
                structure.push(value) if kind == "stack" else structure.enqueue(value)
                print("Operation successful.")
            elif choice == "2":
                value = structure.pop() if kind == "stack" else structure.dequeue()
                print("Removed:", value)
            elif choice == "3":
                value = structure.peek() if kind == "stack" else structure.peek_front()
                print("Top/front value:", value)
            elif choice == "4":
                print("Is empty:", structure.is_empty())
            elif choice == "5":
                print("Is full:", structure.is_full())
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def main():
    while True:
        print("\\n--- Stacks and Queues Laboratory ---")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Check Balanced Parentheses")
        print("6. Simulate Print Queue")
        print("0. Exit")
        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                test_structure(ArrayStack(int(input("Stack capacity: "))), "stack")
            elif choice == "2":
                test_structure(LinkedStack(), "stack")
            elif choice == "3":
                test_structure(ArrayQueue(int(input("Queue capacity: "))), "queue")
            elif choice == "4":
                test_structure(LinkedQueue(), "queue")
            elif choice == "5":
                expression = input("Enter expression: ")
                if is_balanced(expression):
                    print("The parentheses are balanced.")
                else:
                    print("The parentheses are not balanced.")
            elif choice == "6":
                simulate_print_queue()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid selection.")
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
