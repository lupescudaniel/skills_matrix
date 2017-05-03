# Skills Matrix
This is the CRC app for organizing and recording skills within a team. Currently being utilized within the Software Development Group.

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
manage.py migrate
manage.py createsuperuser
manage.py runserver
</pre>

## Contributing Guidelines
All contributions from should be made via Pull Requests to the master branch. This may change as the application matures.

## App Entity Relationship Diagrams
Skills Matrix App structure reflects the following ERD: 
![alt text][erd]

[erd]: https://raw.githubusercontent.com/ecaldwe1/skillsmatrix/master/SkillsMatrixERD.png "Skillsmatrix app database ERD"



