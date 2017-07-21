/**
 * This is an example of a basic node.js script that performs
 * the Authorization Code oAuth2 flow to authenticate against
 * the Spotify Accounts.
 *
 * For more information, read
 * https://developer.spotify.com/web-api/authorization-guide/#authorization_code_flow

 To run in terminal, type 'node app.js'. Then open a chrome and type 'localhost:8888'. Login, then look at terminal for info
 */

// run 'npm install simple_statistics' to install statistic software to use statistic controls
// run 'npm install d3' to install d3 and then require it to allow use of d3 in this file coded in node.js

var d3 = require('d3'),
    http = require('http'),
    fs = require('fs');

var express = require('express'); // Express web server framework
var request = require('request'); // "Request" library
var querystring = require('querystring');
var cookieParser = require('cookie-parser');

var client_id = '93ba9aeed2e94c22a2c9a7cb4aff6fa8'; // Your client id
var client_secret = '7b4ccf4a65e445e4b4aeb25f84c7b195'; // Your client secret
var redirect_uri = 'http://localhost:8888/callback'; // Your redirect uri


/**
 * Generates a random string containing numbers and letters
 * @param  {number} length The length of the string
 * @return {string} The generated string
 */
var generateRandomString = function(length) {
  var text = '';
  var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

  for (var i = 0; i < length; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
};

var stateKey = 'spotify_auth_state';

var app = express();

app.use(express.static(__dirname + '/public'))
   .use(cookieParser());

app.get('/login', function(req, res) {

  var state = generateRandomString(16);
  res.cookie(stateKey, state);

  // your application requests authorization
  var scope = 'user-read-private user-read-email user-follow-read';
  res.redirect('https://accounts.spotify.com/authorize?' +
    querystring.stringify({
      response_type: 'code',
      client_id: client_id,
      scope: scope,
      redirect_uri: redirect_uri,
      state: state
    }));
});

app.get('/callback', function(req, res) {

  // your application requests refresh and access tokens
  // after checking the state parameter

  var code = req.query.code || null;
  var state = req.query.state || null;
  var storedState = req.cookies ? req.cookies[stateKey] : null;

  if (state === null || state !== storedState) {
    res.redirect('/#' +
      querystring.stringify({
        error: 'state_mismatch'
      }));
  } else {
    res.clearCookie(stateKey);
    var authOptions = {
      url: 'https://accounts.spotify.com/api/token',
      form: {
        code: code,
        redirect_uri: redirect_uri,
        grant_type: 'authorization_code'
      },
      headers: {
        'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
      },
      json: true
    };

    request.post(authOptions, function(error, response, body) {
      if (!error && response.statusCode === 200) {

        var access_token = body.access_token,
            refresh_token = body.refresh_token;

        var options = {
          url: 'https://api.spotify.com/v1/me',
          headers: { 'Authorization': 'Bearer ' + access_token },
          json: true
        };

        // use the access token to access the Spotify Web API. Displays user information
        request.get(options, function(error, response, body) {
          //console.log(body);
          //console.log('country and name: ' + body['country'] + ', ' + body['display_name'])
        });

        // Begin my code ----------------------------------------
        var async = require("async");
        var get_artists = require("./get_artists");

        var collector = [];
        var popular_array = [];
        var utada_artists = [];
        var popular_artists = [];
        var friend_popularity = ["value"];

        var options_three = {
          url: 'https://api.spotify.com/v1/me/playlists',
          headers: { 'Authorization': 'Bearer ' + access_token },
          json: true
        };


        var eg2 = '';

        // Use the async module to perform each callback sequentally
        async.series([
          function(callback) {
            setTimeout(function() {
              console.log("task 1"); // Task 1 takes my login, filters on artists, and takes popularity from each artist. Then a user's popularity is based on the average popularity of their artists
              callback(null, 1);
                var options_artist = {
                  url: 'https://api.spotify.com/v1/me/following?limit=20&type=artist',
                  headers: { 'Authorization': 'Bearer ' + access_token },
                  json: true
                };

                // use the access token to access the Spotify Web API. Looks at this users artists
                request.get(options_artist, function(error, response, body) {
                  //console.log(body);
                  //console.log(body['artists'].total);
                  
                  // Prints to console the artist and popularity of artist the user is following
                  body['artists'].items.forEach(function(item) {
                    console.log(item);
                    //console.log('popularity of ' + item.name + ' is ' + item.popularity);
                    popular_array.push(item.popularity)
                  });

                  popular_array = popular_array.sort();
                  var mean = d3.mean(popular_array);
                  friend_popularity.push(mean);
                  console.log("mean of your popular artists: " + mean);
            });
            }, 600);
          },
          function(callback) {
            setTimeout(function() {

              callback(null, 2);
              utada_id = '7lbSsjYACZHn1MSDXPxNF2';



              //calls call_artist function with id and returns all the information from the call
              var eg2 = get_artists.call_artist(utada_id, access_token);
              
            }, 200);
          },
          function(callback) {
            setTimeout(function() {
              callback(null, 3);

              console.log("console log2:" + eg2 + ". ");

            }, 100);
          }
        ], function(error, results) {
          console.log(results);
        });
          

      // End my code ----------------------------------------

      
        // need to work on getting other peoples following artist and correctly run the for csv 
        // Eg Noah's Spotify id is: 1234392786



        // we can also pass the token to the browser to make requests from there
        res.redirect('/#' +
          querystring.stringify({
            access_token: access_token,
            refresh_token: refresh_token
          }));
      } else {
        res.redirect('/#' +
          querystring.stringify({
            error: 'invalid_token'
          }));
      }
    });
  }
});

app.get('/refresh_token', function(req, res) {

  // requesting access token from refresh token
  var refresh_token = req.query.refresh_token;
  var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: { 'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64')) },
    form: {
      grant_type: 'refresh_token',
      refresh_token: refresh_token
    },
    json: true
  };

  request.post(authOptions, function(error, response, body) {
    if (!error && response.statusCode === 200) {
      var access_token = body.access_token;
      res.send({
        'access_token': access_token
      });
    }
  });
});

console.log('Listening on 8888');
app.listen(8888);

