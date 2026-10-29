# Analysis: Stacks and Queues

A linked-list stack adds and removes items at the head because the head can be updated directly in O(1) time. If items were added or removed at the tail of a singly linked list, the program might need to traverse the list, making the operation O(n).

An array queue uses a circular structure so that positions freed by dequeue operations can be reused. The modulo operator wraps the front and rear positions back to the beginning of the array. This avoids shifting the remaining elements and keeps enqueue and dequeue efficient at O(1) time.
