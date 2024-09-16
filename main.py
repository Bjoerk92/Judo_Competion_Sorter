"""

"""
import argparse


def main(args : argparse.Namespace):
    pass




if __name__ == "__main__":

    parser = argparse.ArgumentParser(   prog="Judo Tournament sorter",
                                        description="Program that will make a rough sorting of the ",
                                        epilog="Freeware"
                                    )
    
    parser.add_argument('-filename', '--f', type=str, required=True)
    parser.add_argument('-Output', '--O', type=str, required=False)

    args : argparse.Namespace = parser.parse_args()

    main(args)
    