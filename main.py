"""

"""
import argparse
import CSV_Reader

def main(args : argparse.Namespace):
    
    CSV = CSV_Reader.CSV(args.f, args.D)
    
    




if __name__ == "__main__":

    parser = argparse.ArgumentParser(   prog="Judo Tournament sorter",
                                        description="Program that will make a rough sorting of the ",
                                        epilog="Freeware"
                                    )
    
    parser.add_argument('-filename', '--f', type=str, required=True)
    parser.add_argument('-Output', '--O', type=str, required=False)
    parser.add_argument('-Delimiter', '--D', type=str, required=False, default=";")
    args : argparse.Namespace = parser.parse_args()

    main(args)
    