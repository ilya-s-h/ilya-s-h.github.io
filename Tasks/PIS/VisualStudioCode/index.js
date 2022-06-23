const express = require('express');
const app = express();
const port = 8081;
const path = require('path');
const session = require('express-session');
const util = require('util');
const bodyParser = require('body-parser');
const methodOverride = require('method-override');
const partials = require('express-partials');


const passport = require('passport');
const YandexStrategy = require('passport-yandex').Strategy;

const GitHubStrategy = require('passport-github2').Strategy;

app.use(session({ secret: "supersecret", resave: true, saveUninitialized: true }));

let Users = [{'login': 'admin', 'email':'ilya.s.h.u@yandex.ru'},
            {'login': 'local_js_god', 'email':'ilia-gossoudarev@yandex.ru'},
            {'login': 'ilya-s-h', 'email':'fred3105@mail.ru', 'username': 'ilya-s-h'}];

const findUserByLogin = (login) => {
    return Users.find((element)=> {
        return element.login == login;
    })
}

const findUserByEmail = (email) => {
    return Users.find((element)=> {
        return element.email.toLowerCase() == email.toLowerCase();
    })
}

const findUserByUsername = (username) => {
    return Users.find((element)=> {
        return element.username == username;
    })
}

app.use(passport.initialize());
app.use(passport.session());
app.use(express.static(__dirname + '/public')); //

passport.serializeUser((user, done) => {
    done(null, user.login);
  });
  //user - объект, который Passport создает в req.user
passport.deserializeUser((login, done) => {
    user = findUserByLogin(login);
        done(null, user);
});

passport.use(new YandexStrategy({
    clientID: 'ab6bf3c3dd384ecea61d60880b246b14',
    clientSecret: '7090b57a677a47889a1695c71a7ff018',
    callbackURL: "http://localhost:8081/auth/yandex/callback"
  },
  (accessToken, refreshToken, profile, done) => {
    let user = findUserByEmail(profile.emails[0].value);
    user.profile = profile;
    if (user == undefined) return done(true, null);

    done(null, user);
  }
));

// added

passport.use(new GitHubStrategy({
    clientID: 'Iv1.b91c6dc01b00d38c',
    clientSecret: '24d1a9f916c40692b53ee3648f3345b67f97656b',
    callbackURL: "http://localhost:8081/auth/github/callback"
  },
  (accessToken, refreshToken, profile, done) => {
    let user = findUserByUsername(profile.usernames);
    user.profile = profile;
    if (user == undefined) return done(true, null);

    done(null, user);
  }
));
// added


const isAuth = (req, res, next)=> {
    if (req.isAuthenticated()) return next();

    res.redirect('/sorry');
}


app.get('/', (req, res)=> {
    res.sendFile(path.join(__dirname, 'main.html'));
});
app.get('/sorry', (req, res)=> {
    res.sendFile(path.join(__dirname, 'sorry.html'));
});
app.get('/auth/yandex', passport.authenticate('yandex'));

app.get('/auth/yandex/callback', passport.authenticate('yandex', { failureRedirect: '/sorry', successRedirect: '/private' }));

app.get('/private', isAuth, (req, res)=>{
    res.send(req.user);
});


// added

app.get('/auth/github', passport.authenticate('github', { scope: [ 'user:email' ] }));

app.get('/auth/github/callback', passport.authenticate('github', { failureRedirect: '/sorry', successRedirect: '/private' }));

// added


app.listen(port, () => console.log(`App listening on port ${port}!`))

