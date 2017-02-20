import csv
from skillsmatrix.models import Skill

with open('/home/beth/Code/crc-skillsmatrix/skills_with_families.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Skill.objects.get_or_create(
                name=row[0],
                family=row[1],
                description=row[2],
                skill_url=row[3],
                )
