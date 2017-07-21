var margin = {top: 20, right: 60, bottom: 30, left: 40},
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
    return "<strong>Title: </strong> <span style='color:lightgreen'>" + d.title + "<br></span>" + "<strong>Authors: </strong> <span style='color:lightgreen'>" + d.author + "</span> <br> <strong>Year: </strong> <span style='color:lightgreen'>" + d.year + "<br></span> <strong>Tags: </strong> <span style='color:lightgreen'>" + d.tag + "</span>";
  });

var chart = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

chart.call(tip);
    

var data = [
{'height': 20, 'tag': 'rs', 'title': "The End of Slow Networks: It's Time for a Redesign", 'year': 'to appear', 'author': ' Carsten Binnig and Andrew Crotty and Alex Galakatos and Tim Kraska and Erfan Zamanian'},
{'height': 40, 'tag': 'di', 'title': 'SIGMOD} 2016', 'year': 'to appear', 'author': 'Yeounoh Chung and Michael Lind Mortensen and Carsten Binnig and Tim Kraska'},
{'height': 60, 'year': 'to appear', 'title': 'Answering Enumeration Queries with the Crowd', 'tag': 'crowd', 'author': 'Beth Trushkowsky and Tim Kraska and Michael J. Franklin and Purnamrita Sarkar'},
{'height': 20, 'timestamp': 'Fri, 14 Aug 2015 15:24:11 +0200', 'year': '2015', 'tag': 'cloud', 'author': 'Sanjay Krishnan and Jiannan Wang and Michael J. Franklin and Ken Goldberg and Tim Kraska'},
{'title': 'An Architecture for Compiling UDF-centric Workflows', 'timestamp': 'Fri, 14 Aug 2015 15:24:11 +0200', 'author': 'Andrew Crotty and Alex Galakatos and Kayhan Dursun and Tim Kraska and Carsten Binnig and Ugur Cetintemel and Stan Zdonik', 'height': 40, 'tag': 'ide,ml,rs', 'year': '2015'},
{'title': 'A Demonstration of the BigDAWG Polystore System', 'timestamp': 'Fri, 14 Aug 2015 15:24:11 +0200', 'author': 'Aaron J. Elmore and Jennie Duggan and Mike Stonebraker and Magdalena Balazinska and Ugur Cetintemel and Vijay Gadepally and J. Heer and Bill Howe and Jeremy Kepner and Tim Kraska and Samuel Madden and David Maier and Timothy G. Mattson and S. Papadopoulos and J. Parkhurst and Nesime Tatbul and Manasi Vartak and Stan Zdonik', 'height': 60, 'tag': 'di', 'year': '2015'},
{'title': 'Vizdom: Interactive Analytics through Pen and Touch', 'timestamp': 'Fri, 14 Aug 2015 15:24:11 +0200', 'author': 'Andrew Crotty and Alex Galakatos and Emanuel Zgraggen and Carsten Binnig and Tim Kraska', 'height': 80, 'tag': 'ide', 'year': '2015'},
{'title': 'S-Store: Streaming Meets Transaction Processing', 'timestamp': 'Tue, 15 Sep 2015 19:25:45 +0200', 'author': 'John Meehan and Nesime Tatbul and Stan Zdonik and Cansu Aslantas and Ugur Cetintemel and Jiang Du and Tim Kraska and Samuel Madden and David Maier and Andrew Pavlo and Michael Stonebraker and Kristin Tufte and Hao Wang', 'height': 100, 'tag': 'stream,tx', 'year': '2015'},
{'title': 'Crowdsourcing Enumeration Queries: Estimators and Interfaces', 'timestamp': 'Wed, 09 Sep 2015 09:50:36 +0200', 'author': 'Beth Trushkowsky and Tim Kraska and Michael J. Franklin and Purnamrita Sarkar and Venketaram Ramachandran', 'height': 120, 'tag': 'crowd', 'year': '2015'},
{'title': 'CIDR', 'timestamp': 'Mon, 23 Mar 2015 09:07:18 +0100', 'author': 'Andrew Crotty and Alex Galakatos and Kayhan Dursun and Tim Kraska and Ugur Cetintemel and Stanley B. Zdonik', 'height': 140, 'tag': 'ml,rs', 'year': '2015'},
{'title': 'ACM', 'timestamp': 'Thu, 10 Sep 2015 16:45:35 +0200', 'author': 'Evan R. Sparks and Ameet Talwalkar and Daniel Haas and Michael J. Franklin and Michael I. Jordan and Tim Kraska', 'height': 160, 'tag': 'ml', 'year': '2015'},
{'title': 'ACM', 'timestamp': 'Wed, 14 Oct 2015 12:38:47 +0200', 'author': 'Dalia Kaulakiene and Christian Thomsen and Torben Bach Pedersen and Ugur Cetintemel and Tim Kraska', 'height': 180, 'tag': 'cloud', 'year': '2015'},
{'title': 'SIGMOD', 'timestamp': 'Thu, 12 Nov 2015 16:33:38 +0100', 'author': 'Christopher R and Divy Agrawal and Magdalena Balazinska and Michael I. Cafarella and Michael I. Jordan and Tim Kraska and Raghu Ramakrishnan', 'height': 200, 'tag': 'ml', 'year': '2015'},
{'title': 'SIGMOD', 'timestamp': 'Thu, 12 Nov 2015 16:33:38 +0100', 'author': 'Abdallah Salama and Carsten Binnig and Tim Kraska and Erfan Zamanian', 'height': 220, 'tag': 'cloud', 'year': '2015'},
{'title': 'TuPAQ: An Efficient Planner for Large-scale Predictive Analytic Queries', 'timestamp': 'Mon, 02 Mar 2015 14:17:34 +0100', 'author': 'Evan R. Sparks and Ameet Talwalkar and Michael J. Franklin and Michael I. Jordan and Tim Kraska', 'height': 240, 'tag': 'ml', 'year': '2015'},
{'title': 'S-Store: Streaming Meets Transaction Processing', 'timestamp': 'Thu, 09 Apr 2015 11:33:20 +0200', 'author': 'John Meehan and Nesime Tatbul and Stanley B. Zdonik and Cansu Aslantas and Ugur Cetintemel and Jiang Du and Tim Kraska and Samuel Madden and David Maier and Andrew Pavlo and Michael Stonebraker and Kristin Tufte and Hao Wang', 'height': 260, 'tag': 'stream,tx', 'year': '2015'},
{'title': "The End of Slow Networks: It's Time for a Redesign", 'timestamp': 'Sat, 02 May 2015 17:50:32 +0200', 'author': 'Carsten Binnig and Ugur Cetintemel and Andrew Crotty and Alex Galakatos and Tim Kraska and Erfan Zamanian and Stanley B. Zdonik', 'height': 280, 'tag': 'rs', 'year': '2015'},
{'title': 'Estimating the Impact of Unknown Unknowns on Aggregate Query Results', 'timestamp': 'Sun, 02 Aug 2015 18:42:02 +0200', 'author': 'Yeounoh Chung and Michael Lind Mortensen and Carsten Binnig and Tim Kraska', 'height': 300, 'tag': 'di', 'year': '2015'},
{'height': 320, 'timestamp': 'Thu, 01 Oct 2015 14:28:48 +0200', 'year': '2015', 'tag': 'cloud', 'author': 'Sanjay Krishnan and Jiannan Wang and Michael J. Franklin and Ken Goldberg and Tim Kraska'},
{'title': 'Tupleware: Distributed Machine Learning on Small Clusters', 'timestamp': 'Wed, 15 Oct 2014 20:48:39 +0200', 'author': 'Andrew Crotty and Alex Galakatos and Tim Kraska', 'height': 20, 'tag': 'ide,ml,rs', 'year': '2014'},
{'title': 'Putting Analytics on the Spot: Or How to Lower the Cost for Analytics', 'timestamp': 'Thu, 04 Sep 2014 13:43:57 +0200', 'author': 'Elkhan Dadashov and Ugur Cetintemel and Tim Kraska', 'height': 40, 'tag': 'cloud', 'year': '2014'},
{'title': 'A} Streaming NewSQL System for Big Velocity Applications', 'timestamp': 'Thu, 07 Aug 2014 13:57:10 +0200', 'author': 'Ugur Cetintemel and Jiang Du and Tim Kraska and Samuel Madden and David Maier and John Meehan and Andrew Pavlo and Michael Stonebraker and Erik Sutherland and Nesime Tatbul and Kristin Tufte and Hao Wang and Stanley B. Zdonik', 'height': 60, 'tag': 'stream,tx', 'year': '2014'},
{'title': 'SIGMOD', 'timestamp': 'Sun, 22 Jun 2014 11:31:11 +0200', 'author': 'Gene Pang and Tim Kraska and Michael J. Franklin and Alan Fekete', 'height': 80, 'tag': 'cloud,tx', 'year': '2014'},
{'title': 'SIGMOD', 'timestamp': 'Sun, 22 Jun 2014 11:31:11 +0200', 'author': 'Jiannan Wang and Sanjay Krishnan and Michael J. Franklin and Ken Goldberg and Tim Kraska and Tova Milo', 'height': 100, 'tag': 'di', 'year': '2014'},
{'title': 'SIGMOD', 'timestamp': 'Sun, 22 Jun 2014 11:31:11 +0200', 'author': 'Bill Howe and Michael J. Franklin and Juliana Freire and James Frew and Tim Kraska and Raghu Ramakrishnan', 'height': 120, 'tag': 'ide,ml', 'year': '2014'},
{'title': 'Tupleware: Redefining Modern Analytics', 'timestamp': 'Tue, 01 Jul 2014 11:58:08 +0200', 'author': 'Andrew Crotty and Alex Galakatos and Kayhan Dursun and Tim Kraska and Ugur Cetintemel and Stanley B. Zdonik', 'height': 140, 'tag': 'ml,rs', 'year': '2014'},
{'title': 'Leveraging Transitive Relations for Crowdsourced Joins', 'timestamp': 'Fri, 12 Sep 2014 12:44:21 +0200', 'author': 'Jiannan Wang and Guoliang Li and Tim Kraska and Michael J. Franklin and Jianhua Feng', 'height': 160, 'tag': 'di,crowd', 'year': '2014'},
{'height': 180, 'timestamp': 'Wed, 01 Oct 2014 15:00:05 +0200', 'year': '2014', 'tag': 'di,crowd', 'author': 'Jiannan Wang and Guoliang Li and Tim Kraska and Michael J. Franklin and Jianhua Feng'},
{'title': 'Finding the Needle in the Big Data Systems Haystack', 'timestamp': 'Thu, 31 Jan 2013 14:22:39 +0100', 'author': 'Tim Kraska', 'height': 20, 'tag': 'ml,cloud', 'year': '2013'},
{'title': 'The New Database Architectures', 'timestamp': 'Fri, 10 May 2013 21:22:05 +0200', 'author': 'Tim Kraska and Beth Trushkowsky', 'height': 40, 'tag': 'cloud', 'year': '2013'},
{'title': 'CIDR', 'timestamp': 'Wed, 15 May 2013 20:47:29 +0200', 'author': 'Gianluca Demartini and Beth Trushkowsky and Tim Kraska and Michael J. Franklin', 'height': 60, 'tag': 'crowd', 'year': '2013'},
{'title': 'CIDR', 'timestamp': 'Wed, 15 May 2013 20:47:29 +0200', 'author': 'Tim Kraska and Ameet Talwalkar and John C. Duchi and Rean Griffith and Michael J. Franklin and Michael I. Jordan', 'height': 80, 'tag': 'ml', 'year': '2013'},
{'title': 'MDCC:} multi-data center consistency', 'timestamp': 'Sat, 20 Apr 2013 14:34:54 +0200', 'author': 'Tim Kraska and Gene Pang and Michael J. Franklin and Samuel Madden and Alan Fekete', 'height': 100, 'tag': 'cloud,tx', 'year': '2013'},
{'title': 'AAAI', 'timestamp': 'Tue, 17 Dec 2013 21:42:30 +0100', 'author': 'Sean Louis Goldberg and Daisy Zhe Wang and Tim Kraska', 'height': 120, 'tag': 'di,crowd', 'year': '2013'},
{'title': 'A Framework for Adaptive Crowd Query Processing', 'timestamp': 'Tue, 17 Dec 2013 21:46:20 +0100', 'author': 'Beth Trushkowsky and Tim Kraska and Michael J. Franklin', 'height': 140, 'tag': 'crowd', 'year': '2013'},
{'title': 'ICDE', 'timestamp': 'Sat, 09 Aug 2014 14:37:12 +0200', 'author': 'Beth Trushkowsky and Tim Kraska and Michael J. Franklin and Purnamrita Sarkar', 'height': 160, 'tag': 'crowd', 'year': '2013'},
{'title': 'IEEE', 'timestamp': 'Wed, 17 Sep 2014 19:35:16 +0200', 'author': 'Evan R. Sparks and Ameet Talwalkar and Virginia Smith and Jey Kottalam and Xinghao Pan and Joseph E. Gonzalez and Michael J. Franklin and Michael I. Jordan and Tim Kraska', 'height': 180, 'tag': 'ml', 'year': '2013'},
{'title': 'SIGMOD', 'timestamp': 'Wed, 26 Jun 2013 09:37:17 +0200', 'author': 'Jiannan Wang and Guoliang Li and Tim Kraska and Michael J. Franklin and Jianhua Feng', 'height': 200, 'tag': 'crowd', 'year': '2013'},
{'title': 'SIGMOD', 'timestamp': 'Wed, 26 Jun 2013 09:37:17 +0200', 'author': 'Michael Armbrust and Eric Liang and Tim Kraska and Armando Fox and Michael J. Franklin and David A. Patterson', 'height': 220, 'tag': 'cloud', 'year': '2013'},
{'title': 'SIGMOD', 'timestamp': 'Wed, 26 Jun 2013 09:37:17 +0200', 'author': 'Jan Schaffner and Tim Januschowski and Megan Kercher and Tim Kraska and Hasso Plattner and Michael J. Franklin and Dean Jacobs', 'height': 240, 'tag': 'cloud', 'year': '2013'},
{'title': 'API} for Distributed Machine Learning', 'timestamp': 'Mon, 04 Nov 2013 15:55:47 +0100', 'author': 'Evan R. Sparks and Ameet Talwalkar and Virginia Smith and Jey Kottalam and Xinghao Pan and Joseph E. Gonzalez and Michael J. Franklin and Michael I. Jordan and Tim Kraska', 'height': 260, 'tag': 'ml', 'year': '2013'},
{'title': 'CrowdER: Crowdsourcing Entity Resolution', 'timestamp': 'Fri, 17 Aug 2012 08:48:54 +0200', 'author': 'Jiannan Wang and Tim Kraska and Michael J. Franklin and Jianhua Feng', 'height': 20, 'tag': 'crowd', 'year': '2012'},
{'title': 'EDBT/ICDT', 'timestamp': 'Sun, 26 Oct 2014 19:10:15 +0100', 'author': 'Simon Loesing and Martin Hentschel and Tim Kraska and Donald Kossmann', 'height': 40, 'tag': 'cloud', 'year': '2012'},
{'title': 'Getting It All from the Crowd', 'timestamp': 'Wed, 10 Oct 2012 21:28:47 +0200', 'author': 'Beth Trushkowsky and Tim Kraska and Michael J. Franklin and Purnamrita Sarkar', 'height': 60, 'tag': 'crowd', 'year': '2012'},
{'height': 80, 'timestamp': 'Wed, 10 Oct 2012 21:28:49 +0200', 'year': '2012', 'tag': 'tx,cloud', 'title': 'MDCC:} Multi-Data Center Consistency'},
{'title': 'CrowdER: Crowdsourcing Entity Resolution', 'timestamp': 'Wed, 10 Oct 2012 21:28:54 +0200', 'author': 'Jiannan Wang and Tim Kraska and Michael J. Franklin and Jianhua Feng', 'height': 100, 'tag': 'crowd,di', 'year': '2012'},
{'title': 'VLDB} Crowd', 'timestamp': 'Mon, 26 Mar 2012 13:50:02 +0200', 'author': 'Amber Feng and Michael J. Franklin and Donald Kossmann and Tim Kraska and Samuel Madden and Sukriti Ramesh and Andrew Wang and Reynold Xin', 'height': 20, 'tag': 'crowd', 'year': '2011'},
{'title': 'A} Data Management Perspective', 'timestamp': 'Wed, 16 Nov 2011 16:52:00 +0100', 'author': 'AnHai Doan and Michael J. Franklin and Donald Kossmann and Tim Kraska', 'height': 40, 'tag': 'crowd', 'year': '2011'}, {'title': 'PIQL:} Success-Tolerant Query Processing in the Cloud', 'timestamp': 'Wed, 30 Nov 2011 20:59:41 +0100', 'author': 'Michael Armbrust and Kristal Curtis and Tim Kraska and Armando Fox and Michael J. Franklin and David A. Patterson', 'height': 60, 'tag': 'cloud', 'year': '2011'},
{'title': 'SIGMOD} 2011', 'timestamp': 'Tue, 14 May 2013 19:43:07 +0200', 'author': 'Philippe Bonnet and Stefan Manegold and Matias Bjrling and Wei Cao and Javier Gonzalez and Joel A. Granados and Nancy Hall and Stratos Idreos and Milena Ivanova and Ryan Johnson and David Koop and Tim Kraska and Dan Olteanu and Paolo Papotti and Christine Reilly and Dimitris Tsirogiannis and Cong Yu and Juliana Freire and Dennis Shasha', 'height': 80, 'tag': 'undefined', 'year': '2011'},
{'title': 'SIGMOD', 'timestamp': 'Thu, 16 Jun 2011 17:14:38 +0200', 'author': 'Michael J. Franklin and Donald Kossmann and Tim Kraska and Sukriti Ramesh and Reynold Xin', 'height': 100, 'tag': 'crowd', 'year': '2011'},
{'title': 'PIQL:} Success-Tolerant Query Processing in the Cloud', 'timestamp': 'Mon, 05 Dec 2011 18:05:09 +0100', 'author': 'Michael Armbrust and Kristal Curtis and Tim Kraska and Armando Fox and Michael J. Franklin and David A. Patterson', 'height': 120, 'tag': 'cloud', 'year': '2011'},
{'height': 20, 'timestamp': 'Mon, 17 Jan 2011 15:54:38 +0100', 'year': '2010', 'tag': 'cloud', 'author': 'Donald Kossmann and Tim Kraska'},
{'title': 'A} Modular Cloud Storage System', 'timestamp': 'Thu, 23 Sep 2010 15:39:20 +0200', 'author': 'Donald Kossmann and Tim Kraska and Simon Loesing and Stephan Merkli and Raman Mittal and Flavio Pfaffhauser', 'height': 40, 'tag': 'cloud', 'year': '2010'},
{'title': 'SIGMOD', 'timestamp': 'Mon, 07 Jun 2010 08:03:40 +0200', 'author': 'Donald Kossmann and Tim Kraska and Simon Loesing', 'height': 60, 'tag': 'cloud,tx', 'year': '2010'},
{'title': 'Consistency Rationing in the Cloud: Pay only when it matters', 'timestamp': 'Sun, 26 Oct 2014 19:10:10 +0100', 'author': 'Tim Kraska and Martin Hentschel and Gustavo Alonso and Donald Kossmann', 'height': 20, 'tag': 'cloud,tx', 'year': '2009'},
{'title': 'XQuery Reloaded', 'timestamp': 'Wed, 22 Jul 2015 16:37:36 +0200', 'author': 'Roger Bamford and Vinayak R. Borkar and Matthias Brantner and Peter M. Fischer and Daniela Florescu and David A. Graf and Donald Kossmann and Tim Kraska and Dan Muresan and Sorin Nasoi and Markos Zacharioudaki', 'height': 40, 'tag': 'xml', 'year': '2009'},
{'title': 'How is the weather tomorrow?: towards a benchmark for the cloud', 'timestamp': 'Tue, 12 Feb 2013 12:25:58 +0100', 'author': 'Carsten Binnig and Donald Kossmann and Tim Kraska and Simon Loesing', 'height': 60, 'tag': 'cloud', 'year': '2009'},
{'title': 'XQuery in the browser', 'timestamp': 'Tue, 05 May 2009 16:01:48 +0200', 'author': 'Ghislain Fourny and Markus Pilman and Daniela Florescu and Donald Kossmann and Tim Kraska and Darin McBeath', 'height': 80, 'tag': 'xml', 'year': '2009'},
{'title': 'SIGMOD', 'timestamp': 'Tue, 10 Jun 2008 07:38:06 +0200', 'author': 'Matthias Brantner and Daniela Florescu and David A. Graf and Donald Kossmann and Tim Kraska', 'height': 20, 'tag': 'cloud', 'year': '2008'},
{'title': 'SIGMOD', 'timestamp': 'Tue, 10 Jun 2008 07:38:05 +0200', 'author': 'Ghislain Fourny and Donald Kossmann and Tim Kraska and Markus Pilman and Daniela Florescu', 'height': 40, 'tag': 'xml', 'year': '2008'},
{'title': 'Extending XQuery with Window Functions', 'timestamp': 'Wed, 22 Jul 2015 16:37:33 +0200', 'author': 'Irina Botan and Peter M. Fischer and Daniela Florescu and Donald Kossmann and Tim Kraska and Rokas Tamosevicius', 'height': 20, 'tag': 'xml,stream', 'year': '2007'},
{'height': 20, 'timestamp': 'Tue, 22 Jul 2014 17:03:58 +0200', 'year': '2006', 'tag': 'xml', 'author': 'Joshua Wing Kei Ho and Tristan Manwaring and SeokHee Hong and David Cho Yau Fung and Kai Xu and Tim Kraska and David Hart'}
];

var color = d3.scale.ordinal()
  .domain(["rs", "crowd", "cloud", "di", "ml", "xml", "tx", "stream", "ide", "undefined"])
  .range(["#393b79", "#6baed6", "#c6dbef", "#9ecae1", "#3182bd", "#756bb1", "#9e9ac8", "#31a354", "#bcbddc", "#a1d99b"]);

 d = data.sort(function(a, b) { return a.year - b.year; }); // sorts based on year
  
  d.total = 4;
		x.domain(data.map(function(d) { return d.year; }));
		y.domain([0, d.total]);

  chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  chart.append("g")
      .attr("class", "y axis")
      .call(yAxis);

  chart.selectAll(".bar")
      .data(data)
    		.enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.year); })
      .attr("y", function(d) { return height-d.height; })
      .attr("height", function(d) { return 20; })
      .attr("width", x.rangeBand())
      .style("fill", function(d) { return color(d.tag); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);

  
  var legend = chart.selectAll(".legend")
      .data(color.domain().slice().reverse())
    		.enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width + 42)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
  				.data(data)
      .attr("x", width +34)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d.tag; });

function type(d) {
  d.year = +d.year;
  return d;
}

