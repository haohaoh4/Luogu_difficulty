import src.Luogu_diff as diff
import sys

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.NOTSET)


def main():
	logger.info("Start running")
	sys.stdout.flush()

	user_input = input("Please input your account's name or id.\n")
	try:
		someone = diff.User(user_input)
	except ConnectionError:
		print("Can't find user %s." % user_input)
		return

	times = [0, 0, 0, 0, 0, 0, 0, 0]
	for p in someone.done_problems:
		print("%s:%s" % (p, p.difficulty))
		if p.difficulty<8:
			times[p.difficulty] = times[p.difficulty] + 1
		else:
			times[7] = times[7] + 1

	i = 0
	for n in times:
		print("%s:%s" % (diff.diff_name[i], n))
		i = i + 1


main()
