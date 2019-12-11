## Setup
1. Unzip the 192_final_project.zip file
2. cd to the penncourserec project
3. Use python manage.py runserver to run the application

## Usage
### Routes
1. / - this is the splash page where users can proceed to the
bubbles page or the learn more page
2. /select - this is the bubbles page where users can select
courses they've previously taken and liked. Note that all bubbles
are set to unselected everytime this page is visited.
3. /recommend - this is the page where users will see 3 courses
recommended to them
4. /course?code=course_code - this is the course page, where all
information relevant to a course with code "course_code" can be viewed
5. /learnmore - this is the page where users can learn more
about the tech behind penncourserec
6. /about - this is the page where users can learn about the
app's creators - Priyansh and Ivan!

### Word embeddings
Use the ELMo model found here: (http://magnitude.plasticity.ai/elmo/light/elmo_2x2048_256_2048cnn_1xhighway_weights.magnitude)

Download it directly to the top penncourserec/ directory and rename
it to 'elmo-light-1536D.magnitude'.

### Modifying the database
As of now, we didn't build a scraper using the PennLabs API and instead
just manually added a few classes. To do the same, create a superuser
and add courses in the Courses model accordingly. A scraper is a
feature we hope to add in the future.
