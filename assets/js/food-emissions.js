
    var margin = {
        top: 20,
        right: 20,
        bottom: 30,
        left: 120
      };
    var width = 628 - margin.left - margin.right;
    var height = 500 - margin.top - margin.bottom;

    var svg = d3.select("#visualization")
      .append("svg")
        // .attr("width", width + margin.left + margin.right)
        // .attr("height", height + margin.top + margin.bottom)
        .attr("preserveAspectRatio", "xMinYMin meet")
        .attr("viewBox", `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
        .classed("svg-content", true)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var x = d3.scaleLinear()
          .domain([0, 280])
          .range([0, width]);

    var y = d3.scaleBand()
        .range([height, 0]);

    var xAxis = d3.axisBottom(x);
        // .ticks(10, "%");

    var yAxis = d3.axisLeft(y);

    d3.csv("/media/food-emissions/Protein-emission-efficiency.csv", function(error, data) {

      if (error) throw error;

      // sort by nutrient emissions
      data.sort(function(a, b) { return a.nutrient_mass_emission - b.nutrient_mass_emissions; });


      // filter the data
      data = data.filter(function(d) {
        if (d.nutrient_mass_fraction > 0.1) {
          return d
        }
      })

      // x.domain([0, d3.max(data, function(d) { return d.nutrient_mass_emissions; })]);

      y.domain(data.map(function(d) { return d.product_name; }))
        .paddingInner(0.1)
        .paddingOuter(0.5);


      svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis)
        .append("text")
          .attr("class", "label")
          .attr("transform", "translate(" + width + ",0)")
          .attr("y", -5)
          .style("text-anchor", "end")
          .text("Frequency");

      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis);

      svg.selectAll(".bar")
          .data(data)
        .enter().append("rect")
          .attr("class", "bar")
          .attr("x", 0)
          .attr("height", y.bandwidth())
          .attr("y", function(d) { return y(d.product_name); })
          .attr("width", function(d) { return x(d.nutrient_mass_emissions); });

    });

    // function type(d) {
    //   d.frequency = +d.frequency;
    //   return d;
    // }




// // set the dimensions and margins of the graph
// var margin = {top: 10, right: 30, bottom: 30, left: 110},
//     width = 628 - margin.left - margin.right,
//     height = 400 - margin.top - margin.bottom;

// // append the svg object to the body of the page
// var svg = d3.select("#visualization")
//   .append("svg")
//     .attr("preserveAspectRatio", "xMinYMin meet")
//     .attr("viewBox", `-${margin.left} -${margin.right} ${width} ${height}`)
//     .classed("svg-content", true);

// // add the tooltip area to the webpage
// var tooltip = d3.select("body").append("div")
//     .attr("class", "tooltip")
//     .style("opacity", 0);

// var color = d3.scaleOrdinal(d3.schemeCategory10);

// // set the ranges
// var y = d3.scaleBand()
//           .range([200, 0])
//           .padding(0.1);

// var x = d3.scaleLinear()
//           .range([0, 10]);

          
//     var xAxis = d3.axisBottom(x);
//         // .ticks(10, "%");

//     var yAxis = d3.axisLeft(y);

// //Read the data
// d3.csv("/media/food-emissions/Protein-emission-efficiency.csv", function(error, data) {

//   if (error) throw error;

//   // sort by nutrient emissions
//   data.sort(function(a, b) { return a.nutrient_mass_emission - b.nutrient_mass_emissions; });


//   // filter the data
//   data = data.filter(function(d) {
//     if (d.nutrient_mass_fraction > 0.1) {
//       return d
//     }
//   });

//     // Scale the range of the data in the domains
//   x.domain([0, d3.max(data, function(d){ return d.nutrient_mass_emissions; })])
//   y.domain(data.map(function(d) { return d.product_name; }));

//   // append the rectangles for the bar chart
//   svg.selectAll(".bar")
//       .data(data)
//     .enter().append("rect")
//       .attr("class", "bar")
//       // .attr("x", function(d) { return x(d.nutrient_mass_emissions); })
//       .attr("width", function(d) {return x(d.nutrient_mass_emissions); } )
//       .attr("y", function(d) { return y(d.product_name); })
//       .attr("height", y.bandwidth());

//   // add the x Axis
//   // svg.append("g")
//   //     .attr("transform", "translate(0," + height + ")")
//   //     .call(d3.axisBottom(x));

//   // add the y Axis
//   svg.append("g")
//       .call(d3.axisLeft(y));


//   svg.append("g")
//           .attr("class", "x axis")
//           .attr("transform", "translate(0," + 200 + ")")
//           .call(xAxis)
//         .append("text")
//           .attr("class", "label")
//           .attr("transform", "translate(" + 0 + ",0)")
//           .attr("y", -5)
//           .style("text-anchor", "end")
//           .text("Frequency");

  // // Add X axis
  // var x = d3.scaleLinear()
  //   .domain([-0.01, 0.3])
  //   .range([ 0, width ]);
  // svg.append("g")
  //   .attr("transform", "translate(0," + height + ")")
  //   .call(d3.axisBottom(x));

  // // Add Y axis
  // var y = d3.scaleLinear()
  //   .domain([-5, 80])
  //   .range([ height, 0]);
  // svg.append("g")
  //   .call(d3.axisLeft(y));



  // // add the tooltip area to the webpage
  // var tooltip = d3.select("body").append("div")
  //     .attr("class", "tooltip")
  //     .style("opacity", 0);

  // // Add dots
  // svg.append('g')
  //   .selectAll("dot")
  //   .data(data)
  //   .enter()
  //   .append("circle")
  //     .attr("cx", function (d) { return x(d.nutrient_mass_fraction); } )
  //     .attr("cy", function (d) { return y(d.emissions_total); } )
  //     .attr("r", 5)
  //   //   .style("fill", "#69b3a2")
  //     .style("fill", function(d) { return color(d.product_category); })
  //     .on("mouseover", function(d) {
  //         tooltip.transition()
  //              .duration(200)
  //              .style("opacity", .9);
  //         tooltip.html(d.product_name)
  //              .style("left", (d3.event.pageX + 5) + "px")
  //              .style("top", (d3.event.pageY - 28) + "px");
  //     })
  //     .on("mouseout", function(d) {
  //         tooltip.transition()
  //              .duration(500)
  //              .style("opacity", 0);
  //     });

  // // Add the x Axis
  // svg.append("g")
  //     .attr("transform", "translate(0," + height + ")")
  //     .call(d3.axisBottom(x));

  // // text label for the x axis
  // svg.append("text")             
  //     .attr("transform",
  //           "translate(" + (width/2) + " ," + 
  //                          (height + margin.top + 20) + ")")
  //     .style("text-anchor", "middle")
  //     .text("Protein mass fraction [kg protein / kg product]");

  // // Add the y Axis
  // svg.append("g")
  //     .call(d3.axisLeft(y));

  // // text label for the y axis
  // svg.append("text")
  //     .attr("transform", "rotate(-90)")
  //     .attr("y", 0 - margin.left)
  //     .attr("x", 10 - (height / 2))
  //     .attr("dy", "1em")
  //     .style("text-anchor", "middle")
  //     .text("Product CO2 Emissions [kg CO2 / kg product]");     

  // var legend = svg.selectAll(".legend")
  //     .data(color.domain())
  //   .enter().append("g")
  //     .attr("class", "legend")
  //     .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  // legend.append("rect")
  //     .attr("x", width - 18)
  //     .attr("width", 18)
  //     .attr("height", 18)
  //     .style("fill", color);

  // legend.append("text")
  //     .attr("x", width - 24)
  //     .attr("y", 9)
  //     .attr("dy", ".35em")
  //     .style("text-anchor", "end")
  //     .text(function(d) { return d; });

   
// })
