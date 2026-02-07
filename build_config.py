from dataclasses import dataclass

@dataclass
class Config:
    body_weight: float
    body_fat_percentage: float
    target_body_fat_percentage: float | None
    age: int
    height: int
    activity_level: float
    
def build_config(args) -> Config:
        
        optionals = (
                args.target_body_fat_percentage if args.target_body_fat_percentage else None,
                #default values
                args.age if args.age else 25,
                args.height if args.height else 172,
                args.activity_level if args.activity_level else 1.0
        )

        return Config(
            body_weight=args.body_weight,
            body_fat_percentage=args.body_weight,
            target_body_fat_percentage=optionals[0],
            age=optionals[1],
            height=optionals[2],
            activity_level=optionals[3]
        )