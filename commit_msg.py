#!/usr/bin/env python
import re
import sys

missing_parts_message = (
'A commit message consists of the following parts, separated by blank lines:\n'
'	1. A short summary of the changes\n'
'	2. A more detailed description, if necessary\n'
'	3. The Jira ticket number'
)

MAX_SUMMARY_LENGTH = 50

too_long_summary = (
'Please keep the commit summary to at most {0} characters.'.format(MAX_SUMMARY_LENGTH))

MULTILINE_SUMMARY = (
'Summaries may not be more than one line.')

summary_ends_with_period = 'Summaries may not end with punctuation.'

ticket_matcher = r'^DT-\d{1,5}$'

invalid_ticket = (
'Invalid ticket. Tickets must match the pattern \'{0}\'.'.format(ticket_matcher))

MAX_LINE_LENGTH = 72

line_too_long = (
'Lines in the description must be at most {0} characters long'.format(MAX_LINE_LENGTH))

def verify_summary(summary):
	if len(summary) > MAX_SUMMARY_LENGTH:
		return too_long_summary
	
	if summary[-1] in '?!.,':
		return summary_ends_with_period

	if '\n' in summary:
		return MULTILINE_SUMMARY

def verify_ticket(ticket):
	if not re.match(ticket_matcher, ticket):
		return invalid_ticket

def verify_description(paragraphs):
	lines = [line for paragraph in paragraphs 
		      for line in paragraph.split('\n')]

	if any([len(line) > MAX_LINE_LENGTH for line in lines]):
		return line_too_long

def verify_message(message):
	parts = message.split('\n\n')
	
	if len(parts) < 2:
		return missing_parts_message

	summary = parts[0]
	ticket = parts[-1]

	if verify_summary(summary):
		return verify_summary(summary)

	if verify_ticket(ticket):
		return verify_ticket(ticket)

	if len(parts) > 2 and verify_description(parts[1:-1]):
		return verify_description(parts[1:-1])

def main():
	file_name = sys.argv[1]
	with open(file_name, 'r') as f:
		message = f.read()

	error = verify_message(message)
	
	if error:
		print(error)
		sys.exit(1)

	sys.exit(0)

if __name__ == '__main__':
	main() 
