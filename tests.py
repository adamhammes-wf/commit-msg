import unittest

from commit_msg import verify_message as Verify

def make_message(summary, ticket, description=None):
	if description is None:
		return '\n\n'.join((summary, ticket))
	return '\n\n'.join(summary, ticket, description)

class TestVerifyMessage(unittest.TestCase):
	summary = 'Test summary'
	ticket = 'DT-1234'

	def test_has_all_parts(self):
		good_msg = make_message(self.summary, self.ticket) 
		self.assertIsNone(Verify(good_msg))

	def test_multiline_summary(self):
		summary = self.summary + '\nasdf'
		message = make_message(summary, self.ticket)
		self.assertIsNotNone(Verify(message))

	def test_summary_with_punctuation(self):
		summary = self.summary + '.'
		message = make_message(summary, self.ticket)	
		self.assertIsNotNone(Verify(message))

	def test_too_long_summary(self):
		summary = 'a' * 51
		message = make_message(summary, self.ticket)
		self.assertIsNotNone(Verify(message))

	def test_too_long_ticket(self):
		ticket = 'DT-12341234'
		message = make_message(self.summary, ticket)
		self.assertIsNotNone(Verify(message))

	def test_non_datatables(self):
		ticket = 'TA-1234'
		message = make_message(self.summary, ticket)
		self.assertIsNotNone(Verify(message))
		

if __name__ == '__main__':
	unittest.main()
