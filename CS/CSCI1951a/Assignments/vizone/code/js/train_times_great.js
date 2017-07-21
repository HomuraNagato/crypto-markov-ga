//train_times_great.js
//Create graph
var margin = {top: 100, right: 20, bottom: 50, left: 50},
	width = 1000 - margin.left - margin.right,
	height = 600 - margin.top - margin.bottom;

//Axises are linearly proportional to the actual values - these are the functions we'll use to compute axises
var x_scale = d3.scale.linear()
	.range([0, width])
	.domain([0, 23])
	.clamp(true)
	.nice();

var min_scale = d3.scale.linear()
	.range([0, width/24])
	.domain([0, 59])

var y_scale = d3.scale.linear()
	.range([0, height]) //range --> output values.
	.domain([0, 5527]); //hardcoded domain --> input

var left_edge = 80;
var top_edge = 24;
var times = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", 
	"07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", 
	"15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", 
	"23:00", "23:59"]

var colors2 = ["#ff3333","#ff9933", "#ffcc33", "#ccff33", "#66ff33", "#33ffff", "#3399ff", "#3333ff",
	"#9933ff", "#ff33ff", "#ff3399", "#ff9999", "#001a66", "#660066", "#ccccff", "#00ace6"]

//Set up the y axis by spacing cities out proprotional to the distances from each other
d3.csv("js/data/hyperloop.csv", function(schedule){
	d3.csv("js/data/city_distances.csv", function(dist){
		d3.text("js/data/clean.csv", function(sorted){
			//First get labels of the keys so we can find the names of the stations
			var cities = [];
			var train_sched = {};
			var cities_dist = {};
			var hover_info = {};
			//Read distances from csv file
			var distances = {};
			for (var i = 0; i < dist.length; i++){ //start at 1 to skip top row
				distances[dist[i].city2] = +dist[i].miles;
			}

			//Create a mapping of cities to their y values, determined by the values read from distances csv file
			var top_row = d3.keys(schedule[0]);
			for (var i =0; i<top_row.length; i++){
				var city = new Array();
				if ((i % 2) !== 0){ //only look at odd rows
					var column = top_row[i].split(" ");
					for (var j=0; j<column.length; j++){
						if(j !== column.length-1){ //get rid of last word (which is "arrives" in this case) so we just have city name
							city.push(column[j]);
						}
					}
					city = city.join(" ");

					var miles = 0;
					var toAdd = 0
					var curr_length = cities.length;
					if (curr_length > 0){ //makes first city have a y value of 0
						miles = distances[city]
						toAdd = cities[curr_length-1].miles;
					}
					cities.push({city: city, miles: miles + toAdd});
					cities_dist[city] = miles + toAdd //will use to draw paths on graph
				} 
			}

			//Create chart svg object
			var svg2 = d3.select("#trains").append("svg")
				.attr("width", width+margin.left +margin.right)
				.attr("height", height + margin.top + margin.bottom);

			//vertical access - cities spaced out proportional to their distances 
			var y_axis = svg2.selectAll("div")
				.data(cities)
				.enter();

			y_axis.append("text")
				.attr("class", "city_text")
				.text(function(d){ return d.city})
			 	.attr("y", function(d, i){
			 		return y_scale(d.miles) + top_edge
			 	})
			 	.attr("x", "0")

			y_axis.append("line")
				.attr("x1", left_edge)
				.attr("x2", width+margin.right+margin.left)
				.attr("stroke-width", "1")
				.attr("y1", function(d, i){
			 		return y_scale(d.miles) + top_edge
			 	})
			 	.attr("stroke", "#999999")
			 	.attr("y2", function(d){
			 		return y_scale(d.miles) + top_edge;
			 	});

			//horizontal axis, set up similar to y axis
			var x_axis = svg2.selectAll("div")
				.data(times)
				.enter();

			x_axis.append("text")
				.attr("class", "time_text")
				.text(function(d){ return d})
				.attr("y", top_edge/2)
				.attr("x", function(d, i){
					return x_scale(i) + left_edge
				})

			x_axis.append("line")
				.attr("x1", function(d, i){
					return x_scale(i) + left_edge
				})
				.attr("x2", function(d, i){
					return x_scale(i) + left_edge
				})
				.attr("stroke-width", "1")
				.attr("y1", top_edge)
			 	.attr("stroke", "#999999")
			 	.attr("y2", height+top_edge);

			//list of train names
			var train_list = sorted.split('\n').map(function(line){
				var columns = line.split(',');
				columns.splice(1,columns.length);
				return columns;
			});

			var train_info = [] //main data structure used 

			//everything from csv except train names - we do this so we can bind attributes to the times of each train only
			var newCsv = sorted.split('\n').map(function(line){
				var columns = line.split(',');
				columns.splice(0,1);
				return columns;
			});
			var time_format = d3.time.format("%H:%M:%S");

			//I tried to use the line: time_format.parse("00:00:00") to determine the x domain, but I couldn't get it to work, so I
			//wrote this function to convert values of strings to x values
			var convertTime = function(timeString){
				var split = timeString.split(":");
				var hours = +split[0];
				var hours_x = x_scale(hours)
				var minutes = +split[1];
				var min_x = min_scale(minutes)				

				return hours_x + min_x + left_edge;
			}

			//fill data structure train_info (which maps the train name to the coordinates needed to draw its path) so we can then draw the lines
			var time_format = d3.time.format("%H:%M:%S");
			for (var j = 0; j < newCsv.length; j++){
				var sched = []
				var hover_text = "<p><strong>" + train_list[j] + "</strong></p>"
				for(var k = 0; k<newCsv[j].length; k++){
					var line_array = newCsv[j][k].trim().split("|");
					var verb = " arrives: ";
					if((k % 2) !== 1){
						verb = " departs: ";
					}
					hover_text = hover_text + "</p>" + line_array[1] + verb + line_array[0] + "</p>"
				}

				for(var k = 1; k<newCsv[j].length; k+=2){
					var start = newCsv[j][k-1].trim().split("|");
					var end = newCsv[j][k].trim().split("|")
					var info = { //This object is what the train paths are drawn from. Each of these is appended to a list so that we can bind elements to the list 
						train: train_list[j],
						stroke_color: colors2[j],
						xcoord1: convertTime(start[0]),
						ycoord1: y_scale(cities_dist[start[1]]),
						xcoord2:  convertTime(end[0]),
						ycoord2: y_scale(cities_dist[end[1]]),
						hoverText: hover_text
					}
					sched.push(info)
				}
				train_info.push(sched)
			}

			//tool tip (shown when hovering over a train path)
			var tip = d3.tip()
				.attr("class", "tooltip")
				.offset([50, 50])


			//Now actually draw lines! start by creating pseudo elements
			var paths_div = svg2.selectAll("g")
			 	.data(train_list)
			 	.enter()
			 //Create an element for each train
			var paths = paths_div.append("g")
				.attr("class", function(i){
					return train_list[i]
				})
				
			//each path_part is a line from one station to another
			var path_parts = paths.selectAll("line")
				.data(function(d, i){
					return train_info[i]
				})
				.enter()
			//Set the properties of each path segment - coordinates, colors, hovering - based on information
			var part = path_parts.append("line")
			part.call(tip)
			part.attr("class", function(d){
					return d.train
				})
				.attr("x1", function(d){
					return d.xcoord1
				})
				.attr("x2", function(d){
					return d.xcoord2
				})
				.attr("y1", function(d){
					return d.ycoord1 + top_edge
				})
				.attr("y2", function(d){
					return d.ycoord2 + top_edge
				})
				.attr("stroke", function(d){
					return d.stroke_color;
				})
				.attr("stroke-width", 3)
				//hovering features
				.on("mouseover", function(d, i){
					$("." + d.train).attr("stroke-width", 8) //make stroke thicker to highlight
					tip.html(d.hoverText) //add text to tip and show
					tip.show()
				})
				.on("mouseout", function(d){
					$("." + d.train).attr("stroke-width", 3)
					tip.hide() //hide tip
				})


		});
	});
});



