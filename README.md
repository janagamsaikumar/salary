# salary
# Model deployement using FLaskAPI (a micro web frame work)
# case study: HR of certain company who is hiring required to know the salalry of the newly joined employee. A model is created based on the experience of the employee shpuld predict the salary
# varibles:
name, age, experience, salary.
salary would be my dependent variable and experience would be my independent variable with the linear regression i solved the problem and with good accuracy 
model is build and should be dumped in the pickle file and saved and loaded in model.pkl(model is saved in this particular  file)
#Flask API:
this is the web frame work where our model is deployed
initially create a file (app.py)importing the packages creating an api with defining a function and also index.html file is loaded (this is the web browser page designing file) 
when our model is read from the pkl file html file will display the page format where you give our input.
# files required to build an api model
model.pkl
model.py
app.py
save the files and note should run the application  in flask env make sure that activated the flask environment and then run your application 'python app.py' in the command prompt or anaconda prompt where this particular application is developed.
this gives a URL ''address''portnumber' example http\\127.0.0.0\5000 buy copying this IP address and run in the web browser the page is displayed and run your app. only a admin can access the application because the application related files are saved in the particular machine
to make it access globally deploying model in any cloud application
# model deployement in the HEROKU cloud.
files required: 
model.py
model.pkl
app.py
index.html(should be kept in the templates folder as i've mentioned in the code)
procfile(helps the browzer to run which file first)
requirement.text(where all the libraries are included)
csv file
style.css (styled page) 
all these files uploaded in the githut repository connected to Heroku cloud  specify the file name then select and connect 
then a particular URL is created with respect to our file name the URL is accessed globally now.


