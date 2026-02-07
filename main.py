def main():
    import argparse
    from build_config import build_config
    from validate import validate
    import temptool

    def parse_args(argv=None):
        
        parser = argparse.ArgumentParser(
            prog='OptimalWeightLoss',
            description="Calculates how many calories you can burn today (or over a period of time) without significant muscle loss",
            epilog='6 7'
        )

        parser.add_argument(
            "body_weight",
            required=True,
            help="Weight in pounds (integer or float)"
        )

        parser.add_argument(
            "body_fat_percentage",
            required=True,
            help="Estimated body fat percentage (integer or float)"
        )

        parser.add_argument(
            "age",
            type=int,
            default=25,
            help="age in years (integer); default is 25"
        )

        parser.add_argument(
            "height",
            type=int,
            default=172,
            help="height in centimeters (lol); default is 172"
        )

        parser.add_argument(
            "activity_level",
            type=float,
            default=1.0,
            help="activity level; default is 1.0; if you don't know what this is, this tool might be a bit too advanced for you"
        )

        #optional argument, produces results over a range of time
        parser.add_argument(
            "--target",
            type="int",
            help="Optional argument; Will calculate over a period of time; target body fat percentage (integer or float)"
        )

        #--target argument must be provided, outputs calculations to a csv file in the same directory.
        parser.add_argument(
            "--output",
            action="store_true",
            help="Outputs current body fat percentage, current weight"
        )

        args = parser.parse_args(argv)

        if validate(args):
             return args
        else:
            raise ValueError("Argument(s) invalid")

    def run(config):
        return temptool.calculateDay(config)
        
    # runs above function to parse and validate arguments
    args = parse_args()

    #build program configuration from validated arguments
    config = build_config(args)

    #runs program
    run(config)


if __name__=="__main__":
    main()