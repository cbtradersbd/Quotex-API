class MartingaleCalculator:
    @staticmethod
    def calculate_step(base_stake, step, multiplier=2.2):
        return round(base_stake * (multiplier ** step), 2)
