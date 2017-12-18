import csv
from models import Stars

with open("missions.csv") as csvfile:
    for row in csv.reader(csvfile):
        created = Stars.objects.get_or_create(
            star_name=row[0],
            hip_name=row[1],
            gj_name=row[2],

            planets_in_system=row[12],

            distance=row[16],

            v_band=row[19],

            b_v_mag=row[22],

            spectral_type=row[25],

            stellar_bm_lumo=row[26]
        )

