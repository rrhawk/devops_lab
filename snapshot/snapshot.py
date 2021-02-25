#!/usr/bin/env python
import argparse
import sched
import json
import time
import func


def main():
    file_object = open("file.txt", "a+")
    s = sched.scheduler(time.time, time.sleep)

    def timer_func(sc):
        snap = func.SnapshotClass()
        if args.type == "text":
            file_object.write('TIMESTAMP: {0} SNAPSHOT: \
            {1}'.format(snap.display_count, snap.__dict__) + '\n')
        elif args.type == "json":
            json_object = json.dumps(snap.__dict__, indent=5)
            with open("file.json", "a+") as outfile:
                outfile.write('TIMESTAMP: {0} SNAPSHOT: \
                {1}'.format(snap.display_count, json_object + '\n'))
        sc.enter(args.time, 1, timer_func, (sc,))

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "type",
        type=str,
        help="type of output file: text ot json"
    )
    parser.add_argument(
        '--time',
        type=int,
        default=300,
        help='provide an integer (default: 5min)'
    )
    args = parser.parse_args()
    s.enter(args.time, 1, timer_func, (s,))
    s.run()


if __name__ == "__main__":
    main()
