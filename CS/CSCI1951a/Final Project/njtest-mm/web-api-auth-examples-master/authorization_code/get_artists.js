// tools.js
// ========

var request = require('request'); // "Request" library

module.exports = {
  foo: function () {
    var string = "get_artists is being called inside group-app.js";
    return string;
    // whatever
  },
  call_artist: function (artist_id, access_token) {
    // whatever

                    // Gets information on artist Utada Hikaru and puts average popularity in friend_popularity array
        var artists= {
          url: 'https://api.spotify.com/v1/artists/'+artist_id,
          headers: { 'Authorization': 'Bearer ' + access_token },
          json: true
        };

        var output1 = '';


        // use the access token to access the Spotify Web API. Looks at this users artists
        request.get(artists, function(error, response, body) {
          //var output1 = body.name;
          output1 = console.log(body.name);
        });

        return output1;
  }
};
