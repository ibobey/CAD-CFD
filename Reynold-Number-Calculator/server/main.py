from reynold_number import water_at_10C
from reynold_number.ReynoldNumber import ReynoldNumber

if __name__ == '__main__':
    reynold = ReynoldNumber(u=2, L=1, fluid=water_at_10C)
    reynold_number = reynold.calculate_reynold_number()
    print(reynold_number)
    print(reynold.predict_flow_type())