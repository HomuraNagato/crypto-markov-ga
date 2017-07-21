// set the dimensions of the canvas
var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

datasets = ["../data/age_NE_18-24.csv", "../data/age_NE_25-34.csv", "../data/age_NE_35-44.csv", "../data/age_NE_45-54.csv", "../data/age_NE_55+.csv"]


// set the ranges
var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

var y = d3.scale.linear().range([height, 0]);

// define the axis
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")


var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);


// add the SVG element for age_18-24
var svg2 = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", 
          "translate(" + margin.left + "," + margin.top + ")");




var ch = document.querySelector('[name="q4"]:checked');

s = "age_graph_single_" + ch + ".csv"
//s = "state_donations_18-24.csv"


var graph = function (s) {
  d3.csv(s, function(data) {
  console.log(data);

  // scale the range of the data
  x.domain(data.map(function(d) { return d.category; }));
  y.domain([0, d3.max(data, function(d) { return d.count; })]);

  // add axis
  svg2.select(".x.axis").remove();

  svg2.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .append("text")
      //.attr("transform", "rotate(-90)")
      .attr("y", 50)
      .attr("x", width/2)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text(s)
    .selectAll("text")
      .style("text-anchor", "end")
      .attr("y", 30)
      .attr("x", 30)
      .attr("dx", "-.8em")
      .attr("dy", "-.55em");
      //.attr("transform", "rotate(-90)" );
  /*
  d3.selectAll("x axis")
  .data(data, function(d) { return d.category; })
      .exit()
      .remove();*/

  svg2.select(".y.axis").remove();
  svg2.append("g")
      .attr("class", "y axis")
      .call(yAxis);
/*    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 5)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Frequency");
      */
    



  // Add bar chart
  
  var bar = svg2.selectAll(".bar")
      .data(data);
    bar.enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.category); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.count); })
      .attr("height", function(d) { return height - y(d.count); });

    bar.exit().remove();
    bar
      .transition().duration(750)
      .attr("y", function(d) { return y(d.count); })
      .attr("height", function(d) { return height - y(d.count); });
});
};

graph(datasets[0])

var datasetpicker = d3.select("#dataset-picker").selectAll(".dataset-button")
        .data(datasets);

      datasetpicker.enter()
        .append("input")
        .attr("value", function(d){ return "Dataset " + d })
        .attr("type", "button")
        .attr("class", "dataset-button")
        .on("click", function(d) {
          graph(d);
        });

