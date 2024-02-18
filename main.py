import watchdog

FILE_PATH = "/Users/kuba/PycharmProjects/traffic-watcher/logs.log"

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
    watchdog.monitor_file(FILE_PATH)
