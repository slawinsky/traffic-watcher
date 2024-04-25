import watchdog
import analyzer
import db
import ebtables

FILE_PATH = "/Users/kuba/PycharmProjects/traffic-watcher/logs.log"

if __name__ == '__main__':
    watchdog.monitor_file(FILE_PATH)
