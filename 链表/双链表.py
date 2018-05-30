
# coding=utf-8


class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, headnode=None):
        self.__head = headnode

    def is_empty(self):
        """是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur 用来移动遍历节点
        cur = self.__head
        # count 记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("\n")

    def add(self, item):
        """头部添加元素"""
        new_node = Node(item)
        new_node.next = self.__head
        self.__head = new_node
        new_node.next.prev = new_node

    def append(self, item):
        """尾部添加元素"""
        new_node = Node(item)
        if self.is_empty():
            self.__head = new_node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        :param item elem
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            new_node = Node(item)
            new_node.next = cur
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node

    def remove(self, item):
        """删除元素"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                    # 判断链表是否只有一个节点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 尾节点的时候
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    pass

