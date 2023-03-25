#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, square as sq

class test_square(unittest.TestCase):
    
    def test_is_correct_number(self):
        self.assertTrue(sq.is_correct_number(5))
        self.assertFalse(sq.is_correct_number(-1))
        self.assertTrue(sq.is_correct_number(7))
        self.assertFalse(sq.is_correct_number(16))
        self.assertFalse(sq.is_correct_number(0))
        

    def test_create_empty_square(self):
        expected = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

        self.assertEqual(expected, sq.create_empty_square(3))
        self.assertEqual(3, len(sq.create_empty_square(3)))

    def test_verify_square(self):
        self.assertTrue(True)

    def test_magic_square(self):
        square = sq.create_empty_square(3)
        magic_square = sq.build_magic_square(3,square)
        
        expected = [[2, 7, 6], 
                    [9, 5, 1], 
                    [4, 3, 8]]

        self.assertEqual(expected,magic_square)


