//var data = [4, 8, 15, 16, 23, 42];

d3.csv("data.csv", function(data) {
    console.log(data);

var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 600 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom,
    barHeight = 20;


var x = d3.scale.linear()
    .domain([0, 100])
    .range([0, width]);
/*
var x = d3.scale.linear().range([0, width]);*/

var chart = d3.select(".chart")
    .attr("width", width)
    //.attr("height", barHeight * data.length);
    .attr("height", height);

var gradient = chart.append("defs")
  .append("linearGradient")
    .attr("id", "gradient");
    /*
    .attr("x1", "0%")
    .attr("y1", "0%")
    .attr("x2", "100%")
    .attr("y2", "100%");
    .attr("spreadMethod", "pad");

gradient.append("stop")
    .attr("offset", "0%")
    .attr("stop-color", "lightblue")
    .attr("stop-opacity", 1);

gradient.append("stop")
    .attr("offset", "100%")
    .attr("stop-color", "red")
    .attr("stop-opacity", 1);
    */

gradient.append("stop")
    .attr("stop-color", "lightgreen")
    .attr("offset", "0%");

gradient.append("stop")
    .attr("stop-color", "darkgreen")
    .attr("offset", "100%")

var bar = chart.selectAll("g")
    .data(data)
  .enter().append("g")
    .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

//changed the width from x, which computes the length of bar based on data to the width of the chart
bar.append("rect")
    .attr("width", width)
    .style("fill", "url(#gradient)")
    .attr("height", barHeight - 1);

bar.append("text")
    .attr("x", function(d) { return x(d.value) - 3; })
    .attr("y", barHeight / 2)
    .attr("dy", ".35em")
    .text(function(d) { return d.value; });

//added a line that is positioned at the end of the data
bar.append("line")
        //.style("stroke", "orange")
        .attr("x1", function(d) { return x(d.value); })
        .attr("y1", 0)
        .attr("x2", function(d) { return x(d.value); })
        .attr("y2", barHeight);
});