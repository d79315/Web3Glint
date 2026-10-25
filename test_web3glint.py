# test_web3glint.py
"""
Tests for Web3Glint module.
"""

import unittest
from web3glint import Web3Glint

class TestWeb3Glint(unittest.TestCase):
    """Test cases for Web3Glint class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Glint()
        self.assertIsInstance(instance, Web3Glint)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Glint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
