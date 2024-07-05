from workshop import Workshop
from tire import Tire
from engine import Engine
from car import Car
from motorcycle import Motorcycle


def main():
    wsp = Workshop('Oficina')
    print(wsp)
    fusca = Car(
        manufacturer='VW',
        model='Fusca',
        engine=Engine(200),
        tires=[Tire(205, 55) for _ in range(4)],
        num_doors=2,
    )
    motocabraba = Motorcycle(
        manufacturer='Motoca',
        model='Braba',
        engine=Engine(150),
        tires=[Tire(200, 50) for _ in range(2)],
        has_sidecar=False,
    )
    wsp.fix_vehicle(station=2, vehicle=motocabraba)
    wsp.fix_vehicle(station=1, vehicle=fusca)


if __name__ == '__main__':
    main()
