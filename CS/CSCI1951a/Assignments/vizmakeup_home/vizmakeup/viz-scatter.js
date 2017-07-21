var margin = {top: 20, right: 30, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");
    
var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>Author: </strong> <span style='color:lightgreen'>" + d.author + "<br></span>" + "<strong>Count: </strong> <span style='color:lightgreen'>" + d.count + "</span> <br> <strong>Tag: </strong> <span style='color:lightgreen'>" + d.tag + "<br></span> <strong>Year: </strong> <span style='color:lightgreen'>" + d.year + "</span>";
  });

var chart = d3.select(".chart-scatter")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

chart.call(tip);

var color = d3.scale.ordinal()
  .domain(["rs", "crowd", "cloud", "di", "ml", "xml", "tx", "stream", "ide", "undefined"])
  .range(["#393b79", "#6baed6", "#c6dbef", "#9ecae1", "#3182bd", "#756bb1", "#9e9ac8", "#31a354", "#bcbddc", "#a1d99b"]);


var pubs = [
	{author: "Tim Kraska", count: 41, year: 2015, month: "Aug", days: 14, tag: "cloud"},
  {author: "Michael I. Jordan", count: 1, year: 2015, month: "Sept", days: 10, tag: "ml"},
  {author: "Ryan Johnson'", count: 1, year: 2011, month: "May", days: 14, tag: "undefined"},
  {author: "Kristal Curtis", count: 2, year: 2011, month: "Nov", days: 30, tag: "cloud"},
  {author: "Torben Bach Pedersen", count: 1, year: 2015, month: "Oct", days: 14, tag: "cloud"},
  {author: "Michael J. Franklin", count: 27, year: 2015, month: "Sept", days: 10, tag: "ml"},
  {author: "Paolo Papotti", count: 1, year: 2013, month: "May", days: 14, tag: "undefined"},
  {author: "Michael Stonebraker", count: 3, year: 2015, month: "Sep", days: 15, tag: "stream,tx"},
  {author: "John Meehan", count: 2, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "Hao Wang", count: 5, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "David A. Patterson", count: 1, year: 2013, month: "June", days: 26, tag: "cloud"},
  {author: "Philippe Bonnet", count: 1, year: 2011, month: "May", days: 14, tag: "undefined"},
  {author: "Raghu Ramakrishnan", count: 2, year: 2015, month: "Nov", days: 12, tag: "ml"},
  {author: "Abdallah Salama", count: 1, year: 2015, month: "Nov", days: 12, tag: "cloud"},
  {author: "Sorin Nasoi", count: 1, year: 2015, month: "July", days: 22, tag: "xml"},
  {author: "Beth Trushkowsky", count: 5, year: 2015, month: "Sept", days: 9, tag: "crowd"},
  {author: "Simon Loesing", count: 1, year: 2014, month: "Oct", days: 26, tag: "cloud"},
  {author: "Reynold Xin", count: 1, year: 2011, month: "Mar", days: 26, tag: "crowd"},
  {author: "Michael Armbrust", count: 1, year: 2011, month: "Nov", days: 30, tag: "cloud"},
  {author: "J. Parkhurst", count: 1, year: 2015, month: "Aug", days: 15, tag: "di"},
  {author: "Juliana Freire", count: 2, year: 2014, month: "June", days: 22, tag: "ide,ml"},
  {author: "Stephan Merkli", count: 1, year: 2010, month: "Sept", days: 10, tag: "cloud"},
  {author: "Purnamrita Sarkar", count: 2, year: 2012, month: "Oct", days: 10, tag: "crowd"},
  {author: "Sanjay Krishnan", count: 1, year: 2015, month: "Aug", days: 15, tag: "cloud"},
  {author: "Donald Kossmann", count: 10, year: 2012, month: "Oct", days: 26, tag: "cloud"},
  {author: "Cong Yu", count: 1, year: 2011, month: "May", days: 14, tag: "undefined"},
  {author: "Samuel Madden", count: 1, year: 2015, month: "Aug", days: 14, tag: "di"},
  {author: "Stanley B. Zdonik", count: 1, year: 2015, month: "Mar", days: 23, tag: "ml,rs"},
  {author: "Dean Jacobs", count: 1, year: 2013, month: "June", days: 26, tag: "cloud"},
  {author: "Jiang Du", count: 3, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "Kristin Tufte", count: 4, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "Andrew Pavlo", count: 3, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "Andrew Crotty", count: 2, year: 2015, month: "Mar", days: 23, tag: "ml,rs"},
  {author: "Alex Galakatos", count: 7, year: 2015, month: "Aug", days: 14, tag: "ide,ml,rs"},
  {author: "David A. Graf", count: 2, year: 2009, month: "July", days: 22, tag: "xml"},
  {author: "Daniela Florescu", count: 4, year: 2009, month: "July", days: 22, tag: "xml"},
  {author: "S. Papadopoulos", count: 1, year: 2015, month: "Aug", days: 14, tag: "di"},
  {author: "Carsten Binnig", count: 5, year: 2015, month: "Aug", days: 14, tag: "ide,ml,rs"},
  {author: "Sukriti Ramesh", count: 2, year: 2011, month: "Mar", days: 26, tag: "crowd"},
  {author: "Cansu Aslantas", count: 2, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "Ken Goldberg", count: 3, year: 2015, month: "Aug", days: 14, tag: "cloud"},
  {author: "Ugur Cetintemel", count: 9, year: 2015, month: "Aug", days: 14, tag: "ide,ml,rs"},
  {author: "Peter M. Fischer", count: 2, year: 2015, month: "July", days: 22, tag: "xml"},
  {author: "Virginia Smith", count: 2, year: 2013, month: "Sept", days: 17, tag: "ml"},
  {author: "Nesime Tatbul", count: 4, year: 2015, month: "Aug", days: 14, tag: "di"},
  {author: "David Maier", count: 4, year: 2015, month: "Sept", days: 15, tag: "stream,tx"},
  {author: "Ameet Talwalkar", count: 5, year: 2015, month: "Sept", days: 10, tag: "ml"},
  {author: "Michael Lind Mortensen", count: 2, year: 2015, month: "Aug", days: 2, tag: "di"},
  {author: "Magdalena Balazinska", count: 2, year: 2015, month: "Aug", days: 14, tag: "di"}
];

var months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];
 
		x.domain(months.map(function(d) { return d; }));
		y.domain([0, d3.max(pubs, function(d) { return d.count; })]);
		
  chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  chart.append("g")
      .attr("class", "y axis")
      .call(yAxis);
		
		chart.selectAll(".dot")
      .data(pubs)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 4.5)
      .attr("cx", function(d) { return x(d.month)+x.rangeBand()/2+75*((d.days - 1) / 30); }) //width between each month is 900/12=75, not fully accurate since computing each month to have 30 days
      .attr("cy", function(d) { return y(d.count); })
      .style("fill", function(d) { return color(d.tag); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);
  
  var legend = chart.selectAll(".legend")
      .data(color.domain().slice().reverse())
    		.enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
  				.data(data)
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d.tag; });

function type(d) {
  d.year = +d.year; 
  return d;
}

