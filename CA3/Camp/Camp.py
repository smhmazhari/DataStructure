INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'

class MaxHeap:
    def __init__(self):
        self.heap = list()
    
    def bubble_up(self, index):
        while (index > 0):
            index_parent = (index - 1) // 2
            if (self.heap[index_parent].value < self.heap[index].value):
                self.heap[index], self.heap[index_parent] =  self.heap[index_parent], self.heap[index]
                index = index_parent
            else:
                break

    def bubble_down(self, index):
        while True:
            index_bigest = index
            index_right = 2*(index + 1)
            index_left = 2*(index + 1) - 1

            if (index_left < len(self.heap)):
                if (self.heap[index_bigest].value < self.heap[index_left].value):
                    index_bigest = index_left

            if (index_right < len(self.heap)):
                if (self.heap[index_bigest].value < self.heap[index_right].value):
                    index_bigest = index_right

            if  (index != index_bigest):
                self.heap[index], self.heap[index_bigest] = self.heap[index_bigest], self.heap[index]
                index = index_bigest
            else:
                break



    def find_max_child(self, index):
        index = self.evaluate_index(index)
        left_child = 2*(index + 1) -1
        right_child = 2*(index + 1)

        if (left_child >= len(self.heap_list)):
            raise Exception(EMPTY)
        elif (right_child >= len(self.heap_list)):
            return left_child
        else:
            if (self.heap_list[left_child].key >= self.heap_list[right_child].key):
                return right_child
            else:
                return left_child     


    def heapify(self, *args):
        for i in args:
            self.heap_push(i)


    def heap_push_node(self, node):
        self.heap.append(node)
        self.bubble_up(len(self.heap) - 1)
    
    def heap_pop_node(self):
        if (len(self.heap) == 0):
            return None
        elif (len(self.heap) == 1):
            out = self.heap.pop()
            return out
        
        out = self.heap[0]
        last_child = self.heap.pop()
        self.heap[0] = last_child
        self.bubble_down(0)
        return out
                        
class Teacher:
    def __init__(self,t,a,s) -> None:
        self.teaching_days = t
        self.start_day = a
        self.value = s

teachers, days = list(map(int,input().split()))
sum = 0
teach_list = []
for teacher in range(teachers):
    a, t, s = list(map(int,input().split()))
    sum += t*s
    teach_list.append(Teacher(t,a-1,s))

anger_heap = MaxHeap()
teach_list.sort(key=lambda x: x.start_day)
index = 0

for day in range(days):
    while(index < teachers):
        if(teach_list[index].start_day != day):
            break
        anger_heap.heap_push_node(teach_list[index])
        index += 1

    angriest = anger_heap.heap_pop_node()
    if(angriest is None):
        continue
    
    sum -= angriest.value
    angriest.teaching_days -= 1
    if(angriest.teaching_days > 0):
        anger_heap.heap_push_node(angriest)

print(sum)