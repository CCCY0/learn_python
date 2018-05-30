
# -*- coding:utf-8 -*-


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

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
            pre = self.__head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count += 1
            new_node = Node(item)
            new_node.next = pre.next
            pre.next = new_node

    def remove(self, item):
        """删除元素"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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

