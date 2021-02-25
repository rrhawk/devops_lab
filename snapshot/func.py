import psutil


class SnapshotClass:

    snapCount = 0

    def __init__(self):
        self.cpu = str(psutil.cpu_percent(interval=0.5))
        self.mem = str(psutil.virtual_memory().total - psutil.virtual_memory().available)
        self.vm = str(psutil.virtual_memory().used)
        self.io = str(psutil.disk_io_counters())
        self.net = str(psutil.net_io_counters())
        SnapshotClass.snapCount += 1

    @property
    def display_count(self):
        return SnapshotClass.snapCount
