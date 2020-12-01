import argparse
import sys
import subprocess


def main(args):

        
    subprocess.run(['cat', '/etc/os-release'], check=True)


if __name__ == '__main__':
    main(sys.argv[1:])
