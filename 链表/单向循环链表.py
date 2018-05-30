
# -*- coding:utf-8 -*-


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""

    def __init__(self, headnode=None):
        self.__head = headnode
        if headnode:
            headnode.next = headnode

    def is_empty(self):
        """是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur 用来移动遍历节点
        cur = self.__head
        # count 记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环的时候没有打印尾节点 所以打印一下
        print(cur.elem)

    def add(self, item):
        """头部添加元素"""
        new_node = Node(item)
        if self.is_empty():
            self.__head = new_node
            new_node.next = new_node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            new_node.next = self.__head
            self.__head = new_node
            cur.next = new_node

    def append(self, item):
        """尾部添加元素"""
        new_node = Node(item)
        if self.is_empty():
            self.__head = new_node
            new_node.next = new_node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.__head

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
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        while cur.next != self.__head:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:
                    # 头节点的情况
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        # 尾节点的处理:
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        """查找元素是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 对比尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    pass

