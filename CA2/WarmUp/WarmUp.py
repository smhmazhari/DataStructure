import sys
import re


class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        pass

    def getSize(self):
        return self.tail - self.head 
        pass

    def enqueue(self, value):
        self.queue.append( value )
        self.tail += 1
        pass

    def dequeue(self):
        if self.isEmpty():
            return
        self.head += 1
        return self.queue[self.head - 1]
        pass

    def isEmpty(self):
        return (self.tail - self.head == 0 )
        pass

    def getInOneLine(self):
        if self.isEmpty():
            return
        one_line = ""
        for i in range (self.head , self.tail ):
            one_line += str(self.queue[i]) + " "
            # print(self.queue[i],end = " ")
        return one_line

class Stack:
    def __init__(self, size=10):
        self.size = size
        self.stack = [0] * size
        self.top = -1
        pass

    def isEmpty(self):
        return self.top == -1
        pass

    def push(self, value):
        if self.top == self.size - 1 :
            return
        self.top += 1
        self.stack[self.top] = value
        pass

    def pop(self):
        if self.isEmpty():
            return
        self.top -= 1
        return self.stack[self.top + 1]
        pass

    def put(self, value):
        if self.isEmpty():
            return
        self.stack[self.top] = value
        pass

    def peek(self):
        if self.isEmpty():
            return
        return self.stack[self.top]
        pass

    def expand(self):
        self.size *= 2
        pass

    def getInOneLine(self):
        if self.isEmpty():
            return ""
        one_line = ""
        for i in range(0,self.top + 1):
            one_line += str(self.stack[i]) + " "
            # print(self.stack[i],end= " ")
        pass
        return one_line

    def getSize(self):
        return self.top + 1
        pass

    def getCapacity(self):
        return self.size
        pass


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def getList(self):
        one_line = ""
        current = self.head
        while(current!= None):
            # print(current,end=" ")
            one_line += str(current.value) + " "
            current = current.next
        return one_line

    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head is None :
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        pass

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        current = self.head
        if current is None :
            self.head = new_node
            return
        while(current.next is not None):
            current=current.next
        current.next = new_node
        pass

    def reverse(self):
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
        # if self.head is None or self.head.next is None :
        #     return
        # reverse(self.head.next)
        # self.head.next.next = self.head
        # self.head.next = None
        pass


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
