#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Assignment 1, Q2:
    "Implement an algorithm to find the kth to last element of a singly linked list."
My assumptions:
    1. I can use an implementation of linked list that can return its current size (length) after construction.
    2. Return value of the kth to last node (instead of the node itself).
    3. Return None in case of a negative k, return the first element (root) in case of k > size.
'''
import unittest


class Node:
    '''
    Node class, each node has a value and a pointer to the next node.
    '''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return 'Node_{}'.format(self.value)


class LinkedList:
    '''
    Singly linked list structure with possibility to store the current length (number of nodes)
    and add new nodes to the end of the list.
    '''

    def __init__(self):
        self.root = None
        self.tail = None
        self.length = 0

    def add(self, value):
        '''
        Add a new node to the end of the linked list, with a specified value.
        :param value: Value to initialize the new node with.
        :return: None
        '''
        curr_node = Node(value)
        if not self.root:
            self.root = curr_node
        else:
            self.tail.next = curr_node
        self.tail = curr_node
        self.length += 1

    def __len__(self):
        return self.length


def kth_to_last(linked_list, k):
    '''
    Find the kth to last element of a singly linked list.
    Returns value of the element, or None if k is a negative number.
    If k is greater than the size of the linked_list, returns the first element.

    :param linked_list: LinkedList object in which we need to find the element.
    :param k: Integer specifying kth to last element.
    :return: Value of the kth to last node in the linked list, or None if k is a negative number,
    or value of the first element if k is larger than the size of the linked list.
    '''
    if k < 0:
        return None
    target_index = len(linked_list) - k
    curr_node = linked_list.root
    curr_index = 0
    while curr_node and curr_index < target_index - 1:
        curr_node = curr_node.next
        curr_index += 1
    return curr_node.value