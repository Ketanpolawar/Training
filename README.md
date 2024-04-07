## Team : The Coders
## Team id : WHO63
##  Problem Statement : Adaptive Laearning Pathways


## Acknowledgement :
The following project was made by our Team TheCoders for our Formal submission in he central India's biggest Hackathon Wittyhacks 4.0 orgainised by Major Leauge Hacking(MLH) and Datacode.in.

## Project Title :  PosAbility

### WHY of PosAbility :

Adaptive learning techniques are a beacon of hope for millions of individuals with disabilities worldwide. According to the World Health Organization (WHO), over one billion people, or approximately 15% of the global population, live with some form of disability. Among them, cognitive impairments affect a significant portion, hindering educational attainment and social inclusion. However, adaptive learning technologies offer a transformative solution, as evidenced by studies showing a 30% improvement in learning outcomes among students with disabilities who utilize such tools.

Beyond statistics, let's consider the human impact. Imagine the joy and pride felt by a dyslexic child as they read their first sentence independently using text-to-speech technology. Picture the sense of accomplishment radiating from a visually impaired student as they navigate through interactive learning modules, fully engaged and included. These emotions, coupled with tangible results, underscore the profound social benefit of embracing adaptive learning techniques. By investing in inclusive education, we not only empower individuals with disabilities to reach their full potential but also cultivate a more compassionate and equitable society for all.



### Description :
Our project is based on Adaptive Learning We are creating a Adaptive educational website i.e. website would adapt as per the user . We are focusing to cater our fellow friends with special abilities both major(Blindness,deaf,etc) and minor(congnative disabilities,adhd,dyslexia,etc) .This website will target on providing education keeping in mind the learning preferences of the users thus empowering them and helping them to enhance their skills.Our further aim would be create a model to  track attention retaining capacity of these individuals and thus enganging them with short activities to help them regain their intrest in ongoing lecture to enhance the learning.


![README 1](https://github.com/Wittyhacks4CR007/WH063_TheCoders/assets/115727322/91edc83e-d31e-433a-9f2d-4c903ffe537e)

![README2](https://github.com/Wittyhacks4CR007/WH063_TheCoders/assets/90147468/070d5891-8254-45eb-9de9-ff5726979a3a)


### Tech Stack

This project is built using the following technologies:

- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white)
- ![React.js](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
- ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
- ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
- ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)

Feel free to explore each technology to learn more about how they were used in this project.

| Sr | Steps |
|:---:|:----:|
|1.| Brainstroming over problem statements and calculating  all the possiable and Fesiable Solutions and selecting one which suite the best to intrest |
|2.| Deciding the Tech stack for the project |
|3.| Getting the key Features |
|4.| Deciding the Database Schemas|
|5.| Creating the frontend |
|6.| Creating  the Backend |
|7.| Creating the Rest API's through the Postman|
|8.| Integrating the backend and frontend |

### Api's & Dependencies

Postman is an API development platform used for building, testing, and documenting APIs. It offers a user-friendly interface for designing and sharing APIs, as well as features for automated testing and collaboration. Postman simplifies API workflows, from creation to deployment, streamlining the development process. With its extensive features and integrations, Postman is a go-to tool for developers and teams working with APIs.

### Scope

1. Privacy -> Using Aadhar cards for disabled persons can enhance privacy by providing a centralized and secure identification system tailored to their unique needs, minimizing the risk of identity theft or misuse.
2. Accessibility -> Providing keyboard navigation for blind people enhances accessibility and independence, allowing them to navigate digital interfaces more efficiently through alternative input methods.
3. Inclusivity -> Constructing websites in WCAG guidelines and high contrast enhances accessibility for partially colorblind individuals, ensuring inclusivity and usability.
4. Inclusion -> By integrating sign language communication, we empower deaf individuals with inclusive access to information and services, fostering greater engagement and understanding.
5. Empowerment -> Implementing talk-back features, keyboard operations, and highlighted words supports dyslexic individuals by enhancing text comprehension and facilitating navigation, promoting inclusivity and accessibility.


## Follow this to run the project 

### clone or download
```terminal
$ git clone https://github.com/amazingandyyy/mern.git
$ yarn # or npm i
```

### project structure
```terminal
LICENSE
package.json
server/
   package.json
   .env (to create .env, check [prepare your secret session])
client/
   package.json
...
```

## Usage (run fullstack app on your machine)

### Prerequisites
- [MongoDB](https://gist.github.com/nrollr/9f523ae17ecdbb50311980503409aeb3)
- [Node](https://nodejs.org/en/download/) ^10.0.0
- [npm](https://nodejs.org/en/download/package-manager/)

notice, you need client and server runs concurrently in different terminal session, in order to make them talk to each other

### Client-side usage(PORT: 3000)
```terminal
$ cd client          // go to client folder
$ yarn # or npm i    // npm install packages
$ npm run dev        // run it locally

// deployment for client app
$ npm run build // this will compile the react code using webpack and generate a folder called docs in the root level
$ npm run start // this will run the files in docs, this behavior is exactly the same how gh-pages will run your static site
```

## Server-side usage(PORT: 8000)

### Prepare your secret

run the script at the first level:

(You need to add a JWT_SECRET in .env to connect to MongoDB)

```terminal
// in the root level
$ cd server
$ echo "JWT_SECRET=YOUR_JWT_SECRET" >> src/.env
```

### Start

```terminal
$ cd server   // go to server folder
$ npm i       // npm install packages
$ npm run dev // run it locally
$ npm run build // this will build the server code to es5 js codes and generate a dist file
```

### Deploy Server to [Heroku](https://dashboard.heroku.com/)
```terminal
$ npm i -g heroku
$ heroku login
...
$ heroku create
$ npm run heroku:add <your-super-amazing-heroku-app>
// remember to run this command in the root level, not the server level, so if you follow the documentation along, you may need to do `cd ..`
$ pwd
/Users/<your-name>/mern
$ npm run deploy:heroku
```

### After creating heroku

if using webpack:
remember to update the file
...
 'API_URI': JSON.stringify('https://your-super-amazing-heroku-app.herokuapp.com')
 ```
if using parcel
...
 REACT_APP_API_URI=https://your-super-amazing-heroku-app.herokuapp.com
 ```

## Contributors 


<a href= "https://github.com/MaithiliPawde">Maithili Pawde</a>
<a href= "https://github.com/Harsh9307">Harsh Diwase</a>
<a href= "https://github.com/omsangamwar">Om Sangamwar</a>
<a href= "https://github.com/Ketanpolawar">Ketan Polawar</a>





