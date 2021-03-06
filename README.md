# codecamp-skillinator-django
django app for CRC Skills Matrix app

## Setup
### Prerequisites
* Python 2.7.x
* Virtualenv (optional)
* Pip
* Sqlite

### Installation/Initialization
<pre>
git clone https://github.com/ecaldwe1/skills_matrix.git
pip install -r requirements.txt
codecamp-skillinator-django/manage.py migrate
codecamp-skillinator-django/manage.py createsuperuser
codecamp-skillinator-django/manage.py runserver
</pre>

## Contributing Guidelines
All contributions from non-c3 participants should be made via Pull Requests to the master branch. C3 team members may push directly to the master branch. This may change as the application matures.

## App Entity Relationship Diagrams
Skillsmatrix App structure reflects the following ERD: 
![alt text][erd]

[erd]: https://raw.githubusercontent.com/ecaldwe1/skills_matrix/master/SkillsMatrixERD.png "Skillsmatrix app database ERD"



