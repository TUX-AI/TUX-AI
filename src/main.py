from config import config
import stt
import threading
import executor

configuration = config


stt_thread = threading.Thread(target=stt.start, args=[executor.exec,])
stt_thread.start()


stt_thread.join()
