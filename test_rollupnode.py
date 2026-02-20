# test_rollupnode.py
"""
Tests for RollupNode module.
"""

import unittest
from rollupnode import RollupNode

class TestRollupNode(unittest.TestCase):
    """Test cases for RollupNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RollupNode()
        self.assertIsInstance(instance, RollupNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RollupNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
