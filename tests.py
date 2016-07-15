import unittest

from commit_msg import verify_message as Verify

class TestVerifyMessage(unittest.TestCase):
	summary = 'Test summary'
	ticket = 'DT-1234'

	def test_has_all_parts(self):
		good_msg = ('\n\n').join((self.summary, self.ticket))
		self.assertIsNone(Verify(good_msg))

if __name__ == '__main__':
	unittest.main()
