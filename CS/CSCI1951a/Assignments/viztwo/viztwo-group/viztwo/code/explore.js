


var dataFile = "../data/data.json"

function plotData(xInfo, yInfo, fType, fVal) {
d3.json(dataFile, function(error, data) {
  data = data.data;

  counter = {};
  xLabels = [];
  yLabels = [];

  for (var i = 0; i < data.length; i++) {
    event = data[i];
    
    if (fType in event) {
      if (event[fType] != fVal) {
        continue;
      }  
    }

    if (!(event[xInfo] in counter)) {
      counter[event[xInfo]] = {};
    }
    if (!(event[yInfo] in counter[event[xInfo]])) {
      counter[event[xInfo]][event[yInfo]] = 0;
    }
    counter[event[xInfo]][event[yInfo]] += 1;
    if (xLabels.indexOf(event[xInfo]) == -1) {
      xLabels.push(event[xInfo]);
    }
    if (yLabels.indexOf(event[yInfo]) == -1) {
      yLabels.push(event[yInfo]);
    }
  }

  dataset = []
  for (key1 in counter) {
    for (key2 in counter[key1]) {
      dataset.push(
          {
          xLabel: key1, 
          yLabel: key2, 
          value: counter[key1][key2]
          });
    }
  }

  xLabels.sort();
  yLabels.sort();
  createScatterPlot(dataset, xLabels, yLabels);
});
}




function createScatterPlot(data, xLabels, yLabels) {

  d3.select("#charts").html("");

  var margin = { top: 50, right: 50, bottom: 50, left: 100 },
    width = 650 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;
  
  var svg = d3.select("#charts").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var scaleX = d3.scale.linear()
    .domain([0, xLabels.length])
    .range([0, width]);

  var scaleY = d3.scale.linear()
    .domain([0, yLabels.length])
    .range([0, height]);

  var scaleRadius = d3.scale.sqrt()
    .domain([0, getMaxValue(data, "value")])
    .range([0, Math.min(height/yLabels.length/2, width/xLabels.length/2)]);

  var scaleColor = d3.scale.linear()
    .domain([0, getMaxValue(data, "value")])
    .range([60, 0]);

  var xAxis = d3.svg.axis()
      .scale(scaleX)
      .ticks(0);

  var yAxis = d3.svg.axis()
      .scale(scaleX)
      .ticks(0);

  svg.append("g")
    .attr("class", "y right axis mono")
    .call(yAxis.orient("right"));

  svg.append("g")
    .attr("class", "x top axis mono")
    .call(xAxis.orient("top"));

  var yGraphLabels = svg.selectAll(".yLabel")
    .data(yLabels)
    .enter().append("text")
      .text(function (d) { return d; })
      .attr("x", 0)
      .attr("y", function (d, i) { return scaleY(i); })
      .style("text-anchor", "end")
      .attr("transform", "translate(-10," + scaleY(.5) + ")")
      .attr("class", "mono axis");

  var xGraphLabels = svg.selectAll(".xLabel")
    .data(xLabels)
    .enter().append("text")
      .text(function(d) { return d; })
      .attr("x", function(d, i) { return scaleX(i); })
      .attr("y", 0)
      .style("text-anchor", "middle")
      .attr("transform", "translate(" + scaleX(.5) + ", -10)")
      .attr("class", "mono axis");

  var bubbles = svg.selectAll(".bubbles")
    .data(dataset)
    .enter().append("circle")
      .attr("transform", function(d) { return "translate(" + scaleX(xLabels.indexOf(d.xLabel)+ .5) + "," + scaleY(yLabels.indexOf(d.yLabel) + .5) + ")"; })
      .attr("fill", function(d) { return "hsl(" + scaleColor(d.value) + ", 100%, 50%)"; })
      .attr("r", 0);
      
  bubbles.transition()    
      .duration(300) 
      .attr("r", function(d) { return scaleRadius(d.value); });
      
  var bubbles = svg.selectAll(".bubbleText")
    .data(dataset)
    .enter().append("text")
      .text(function(d) { return d.value; })
      .attr("x", 0)
      .attr("y", 0)
      .attr("transform", function(d) { return "translate(" + scaleX(xLabels.indexOf(d.xLabel)+ .5) + "," + scaleY(yLabels.indexOf(d.yLabel) + .5) + ")"; })
      .attr("class", "bubbleText mono")
      .style("text-anchor", "middle");

}


function getMaxValue(l, key) {
  max = null;
  for (var i = 0; i < l.length; i++) {
    if (max == null) {
      max = l[i][key];
    } else if (max < l[i][key]) {
      max = l[i][key];
    } 
  }
  return max;
}

function plotDataFrom(element) {
  var form = $("#plotForm");
  var key1 = form.find('input[name="key1"]').val();
  var key2 = form.find('input[name="key2"]').val();
  var filterType = form.find('input[name="filterType"]').val();
  var filterVal = form.find('input[name="filterVal"]').val();
  plotData(key1, key2, filterType, filterVal);
}


plotData("age", "category", "", "");

