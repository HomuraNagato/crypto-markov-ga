//wrapper.js

// Write cmd below in terminal to install node
//npm install spotify-web-api-node --save

var SpotifyWebApi = require('spotify-web-api-node');

// credentials are optional
var spotifyApi = new SpotifyWebApi({
  clientId : '93ba9aeed2e94c22a2c9a7cb4aff6fa8',
  clientSecret : '7b4ccf4a65e445e4b4aeb25f84c7b195',
  redirectUri : 'http://localhost:8888/callback'
});

// Access Token Authorization here
//spotifyApi.setAccessToken('<your_access_token>');

// Get Elvis' albums
spotifyApi.getArtistAlbums('43ZHCT0cAZBISjO8DG9PnE')
  .then(function(data) {
    console.log('Artist albums', data.body);
  }, function(err) {
    console.error(err);
  });

  