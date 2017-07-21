console.log("Just a small town girl, livin' in a lonely world....")

// Start Marey's train...
 d3.csv("python/city_distances.csv", function(data) {
    	console.log(data);

    d3.csv("python/hyperloop.csv", function(h_data) {
    	console.log(h_data);

    var x = d3.scale.linear().range([0,width])
    var y = d3.scale.linear().range([height,0])
    var xAxis = d3.svg.axis().scale(x)
      .orient("bottom").ticks(function(d) { return d.city1; })
    var yAxis = d3.svg.axis().scale(y)
      .orient("left").ticks(5)
    var valueline = d3.svg.line()
      .x(function(d) { console.log(d); return d.miles; })
      .y(function(d) { console.log(d); return d.miles; })

    var svg2 = d3.select("#train")
      .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

    //var data = [(0,4), (2,2), (4,4), (6,6), (8,8), (10,10), (12,12)]
// the range of the data
    //x.domain(d3.extent(data, function(d) { return d.date; }));
    //y.domain([0, d3.max(data, function(d) { return d.close; })]);
    x.domain([0, d3.max(data)])
    y.domain([0, d3.max(data)])

    // Add the valueline path.
    svg2.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));

    // Add the X Axis
    svg2.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svg2.append("g")
        .attr("class", "y axis")
        .call(yAxis);

	})
})