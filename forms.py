from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, HiddenField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired
from werkzeug.datastructures import MultiDict

class InputForm(Form):
    Name = StringField('Name',render_kw={"size":"116"}) 
    Email = StringField('Email',render_kw={"size":"116"}) 
    Password = StringField('Password',render_kw={"size":"116"}) 
    A1 = SelectField('A.1 (Responsive Web Design ) Basic HTML and HTML5', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A2 = SelectField('A.2 (Responsive Web Design ) Basic CSS', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A3 = SelectField('A.3 (Responsive Web Design ) Applied Visual Design', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A4 = SelectField('A.4 (Responsive Web Design ) Applied Accessibility', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A5 = SelectField('A.5 (Responsive Web Design ) Responsive Web Design Principles', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A6 = SelectField('A.6 (Responsive Web Design ) CSS Flexbox', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A7 = SelectField('A.7 (Responsive Web Design ) CSS Grid', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    A8 = SelectField('A.8 (Responsive Web Design ) Responsive Web Design Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B1 = SelectField('B.1 (Javascript Algorithms And Data Structures ) Basic JavaScript', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B2 = SelectField('B.2 (Javascript Algorithms And Data Structures ) ES6', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B3 = SelectField('B.3 (Javascript Algorithms And Data Structures ) Regular Expressions', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B4 = SelectField('B.4 (Javascript Algorithms And Data Structures ) Debugging', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B5 = SelectField('B.5 (Javascript Algorithms And Data Structures ) Basic Data Structures', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B6 = SelectField('B.6 (Javascript Algorithms And Data Structures ) Basic Algorithm Scripting', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B7 = SelectField('B.7 (Javascript Algorithms And Data Structures ) Object Oriented Programming', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B8 = SelectField('B.8 (Javascript Algorithms And Data Structures ) Functional Programming', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B9 = SelectField('B.9 (Javascript Algorithms And Data Structures ) Intermediate Algorithm Scripting', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    B10 = SelectField('B.10 (Javascript Algorithms And Data Structures ) JavaScript Algorithms and Data Structures Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C1 = SelectField('C.1 (Front End Libraries ) Bootstrap', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C2 = SelectField('C.2 (Front End Libraries ) jQuery', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C3 = SelectField('C.3 (Front End Libraries ) Sass', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C4 = SelectField('C.4 (Front End Libraries ) React', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C5 = SelectField('C.5 (Front End Libraries ) Redux', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C6 = SelectField('C.6 (Front End Libraries ) React and Redux', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    C7 = SelectField('C.7 (Front End Libraries ) Front End Libraries Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    D1 = SelectField('D.1 (Data Visualization ) Data Visualization with D3', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    D2 = SelectField('D.2 (Data Visualization ) JSON APIs and Ajax', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    D3 = SelectField('D.3 (Data Visualization ) Data Visualization Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    E1 = SelectField('E.1 (Apis And Microservices ) Managing Packages with Npm', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    E2 = SelectField('E.2 (Apis And Microservices ) Basic Node and Express', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    E3 = SelectField('E.3 (Apis And Microservices ) MongoDB and Mongoose', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    E4 = SelectField('E.4 (Apis And Microservices ) Apis and Microservices Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    F1 = SelectField('F.1 (Information Security And Quality Assurance ) Information Security with HelmetJS', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    F2 = SelectField('F.2 (Information Security And Quality Assurance ) Quality Assurance and Testing with Chai', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    F3 = SelectField('F.3 (Information Security And Quality Assurance ) Advanced Node and Express', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    F4 = SelectField('F.4 (Information Security And Quality Assurance ) Information Security and Quality Assurance Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    G1 = SelectField('G.1 (Coding Interview Prep ) Algorithms', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    G2 = SelectField('G.2 (Coding Interview Prep ) Data Structures', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    G3 = SelectField('G.3 (Coding Interview Prep ) Take Home Projects', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    G4 = SelectField('G.4 (Coding Interview Prep ) Rosetta Code', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    G5 = SelectField('G.5 (Coding Interview Prep ) Project Euler ', choices=[('Not yet started','Not yet started'),('In progress','In progress'),('Completed','Completed')])
    Save = SubmitField('Save',render_kw={"size":"500"})

class LoginForm(Form):
    LoginEmail = StringField('Email',render_kw={"size":"116"}) 
    LoginPassword = StringField('Password',render_kw={"size":"116"}) 
    LoginButton = SubmitField('Login',render_kw={"size":"500"})

class RegisterForm(Form):
    RegisterEmail = StringField('Email',render_kw={"size":"116"}) 
    RegisterPassword = StringField('Password',render_kw={"size":"116"}) 
    RegisterButton = SubmitField('Register',render_kw={"size":"500"})
