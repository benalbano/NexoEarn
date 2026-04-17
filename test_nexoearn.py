# test_nexoearn.py
"""
Tests for NexoEarn module.
"""

import unittest
from nexoearn import NexoEarn

class TestNexoEarn(unittest.TestCase):
    """Test cases for NexoEarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexoEarn()
        self.assertIsInstance(instance, NexoEarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexoEarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
