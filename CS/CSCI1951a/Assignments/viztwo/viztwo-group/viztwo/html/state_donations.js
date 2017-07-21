// Setting size and positioning of visualization
var margin = { top: 0, right: 0, bottom: 30, left: 30 };
var width = 1200 - margin.left - margin.right;
var height = 800;

// Planning out map coloring
var buckets = 9;
var legendElementWidth = Math.floor(width / buckets);
var colors = colorbrewer.Greens[buckets];

// Data files!
var donations = "../data/state_donations.csv";
var names = "../data/us-state-names.tsv"

// Dictionaries to hold CSV & TSV data
var amounts = {};
var name_id = {};

// Store donations by state in the amounts dictionary
d3.csv(donations, function(d) {
	d.forEach(function(d) {
		amounts[d.state] = d.amount;
	});
});

// Store state ids by abbreviation in the name_id dictionary
d3.tsv(names, function(d) {
	d.forEach(function(d) {
		name_id[d.id] = d.code;
	})
})

// Define the map projection
var projection = d3.geo.albersUsa()
	.scale(1500)
	.translate([width / 2, height / 2]);

// Generate the path
var path = d3.geo.path()
	.projection(projection);

// The SVG that will contain our map!
var svg = d3.select("#map").append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)

// Adding a group representing states to the SVG
var g = svg.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
	.append("g")
	.attr("id", "states");

// Initialize tooltips
var tooltip = d3.select("body")
    .append("div")
    .attr("class", "tooltip");

// Importing state boundary data
d3.json("../data/states.json", function(error, us) {
	if (error) throw error;

	// Define features and thresholds for color buckets
	var features = topojson.feature(us, us.objects.states).features;
	thresholds = [0, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]

	// Determining what fill each state should have
	var states = g.selectAll("path")
		.data(features)
		.enter().append("path")
		.attr("d", path)
		.attr("id", function(d) { return name_id[d.id] })
		.style("fill", function(d) {
			for (var i = thresholds.length - 1; i >= 0; i--) {
				if (amounts[name_id[d.id]] > thresholds[i]) {
					return colors[i];
				}
			}
		});

	// Label each state with its abbreviation
	var labels = g.selectAll("text")
		.data(features)
		.enter().append("text")
		.text(function(d) { return name_id[d.id]; })
		.attr("x", function(d) { 
			var pcd = path.centroid(d)[0];
			if (!(isNaN(pcd))) 
				return pcd;
		})
		.attr("y", function(d) { 
			var pcd = path.centroid(d)[1];
			if (!(isNaN(pcd)))
				return pcd;
		})
		.attr("text-anchor", "middle")
		.attr("font-size", "10pt")
		.attr("font-weight", "bold");

	// We want tooltips to work on both states and their labels
	tooltip_regions = svg.selectAll("path, text");

	// Display how much a state donated when the mouse is on it
	tooltip_regions.on("mouseover", function(d) { 
  		tooltip.transition()
  			.duration(200)
  			.style("opacity", .9);
  		tooltip.html(amounts[name_id[d.id]])
  			.style("left", (path.centroid(d)[0] + 10) + "px")
  			.style("top", (path.centroid(d)[1] + 70) + "px");
  		tooltip.style("visibility", "visible");
  	});
	  	
  	// Remove tooltips when the mouse is moved off the map
  	tooltip_regions.on("mouseout", function() { return tooltip.style("visibility", "hidden"); });

  	// Create the legend based on the previously defined thresholds
	var legend = svg.selectAll(".legend")
		.data(thresholds, function(d) { return d; });

	legend.enter().append("g").attr('class', 'legend');

	// Color rectangles for the legend matching values to colors
	legend.append("rect")
		.attr("x", function(d, i) { return legendElementWidth * i; })
		.attr("y", height - 40)
		.attr("width", legendElementWidth)
		.attr("height", 20)
		.style("fill", function(d, i) { return colors[i]; });

	// Label each color with the appropriate donation amount
	legend.append("text")
		.text(function(d) { return "≥ " + Math.round(d); })
		.attr("x", function(d, i) { return legendElementWidth * i; })
		.attr("y", height);

	legend.exit().remove();
});