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
         # commenting out the following two lines. They were only needed for the initial migration to 
         #     the new model field method. If not commented, it will identify every dev having every skill if 
         #     the object is found!
         # devskill.has_skill = True
         # devskill.save()
     except:
         DeveloperSkill.objects.create(
            developer=d,
            skill=s
         )
