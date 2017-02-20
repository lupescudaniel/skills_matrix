from skillsmatrix.models import DeveloperSkill, Developer, Skill
devs = Developer.objects.all()
skills = Skill.objects.all()

for d in devs:
 for s in skills:
     try:
         devskill =  DeveloperSkill.objects.get(
            developer=d,
            skill=s
         )
         devskill.has_skill = True
         devskill.save()
     except:
         DeveloperSkill.objects.create(
            developer=d,
            skill=s
         )
