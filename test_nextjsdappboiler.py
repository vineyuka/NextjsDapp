# test_nextjsdappboiler.py
"""
Tests for NextjsDappBoiler module.
"""

import unittest
from nextjsdappboiler import NextjsDappBoiler

class TestNextjsDappBoiler(unittest.TestCase):
    """Test cases for NextjsDappBoiler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextjsDappBoiler()
        self.assertIsInstance(instance, NextjsDappBoiler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextjsDappBoiler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
