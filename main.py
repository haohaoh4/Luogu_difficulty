from main_process import *
import logging
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.NOTSET)

try:
	main()
except Exception as e:
	raise e
finally:
	main_end()
