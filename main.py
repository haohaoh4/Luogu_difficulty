from main_process import *

import logging
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.NOTSET)

try:
	main()
except Exception as e:
	logger.error("Error happened,Exit.")
	logger.info("Catch Exception,info \"" + str(e) + "\"")
	sys.stdout.flush()
	raise e
finally:
	main_end()
