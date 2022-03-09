

var diffMatrix

function cmp(a, b) {

    if(a[1] < b[1]) return -1;
    return 1;
}

var sizeLineChart = 400

var x_axis
var y_axis

function createWindow(){

    var svg = d3.select("#compare")
                .attr("height", sizeLineChart)
                .attr("width", sizeLineChart);
    var xScale = d3.scaleLinear()
        .domain([0,1])
        .range([0, 380])

    var yScale = d3.scaleLinear()
        .domain([0,1])
        .range([380, 0])


    x_axis = d3.axisBottom()
                .scale(xScale)

    y_axis = d3.axisLeft()
                .scale(yScale)

    svg.append("svg:path")

    svg.append("g")
        .attr("id", "xaxis")
        .attr("transform", "translate(20,380)")
        .call(x_axis)

    svg.append("g")
        .attr("id", "yaxis")
        .attr("transform", "translate(20,0)") 
        .call(y_axis)

    var thebox = svg.append("rect")
        .attr("transform", "translate(20,0)")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", 380)
        .attr("height", 380)
        .attr("id", "selected_interval")
        .attr("fill", "green")
        .attr("opacity", "0.2")
    
}



function showMinkowskiDiff(folder1, id1, folder2, id2){


    path1 = "./data/mnist_pi/"+folder1+"/"+id1+"_pi.csv"
    path2 = "./data/mnist_pi/"+folder2+"/"+id2+"_pi.csv"

    d3.csv(path1).then(function(data1){
        d3.csv(path2).then(function(data2){
            
            var svg = d3.select("#compare")
            .attr("height", 410)
            .attr("width", 410);

            var matrix1 = []
            var matrix2 = []
            var size = 0

            //organize the elements of the matrix in a line
            data1.forEach(element => {
                size = element.length
                var values = Object.keys(element).map(function(key){
                    return element[key];
                });
                matrix1 = matrix1.concat(values)
            });

            data2.forEach(element => {
                size = element.length
                var values = Object.keys(element).map(function(key){
                    return element[key];
                });
                matrix2 = matrix2.concat(values)
            });

            diffMatrix = []
            var maxDiff = 0 
            for(var i=0; i<matrix1.length; i++){
                var diff = Math.abs(matrix1[i]-matrix2[i])
                maxDiff = Math.max(maxDiff, diff)
                diffMatrix.push([i, diff])
            }

            
            diffMatrix.sort(cmp)

            var slide = d3.select("#compareRange1")
                            .style("visibility", "visible")
                            .attr("min", 0)
                            .attr("max", matrix1.length)
                            .attr("value", 0)

            var slide = d3.select("#compareRange2")
                            .style("visibility", "visible")
                            .attr("min", 0)
                            .attr("max", matrix1.length)
                            .attr("value", matrix1.length)


            var xScale = d3.scaleLinear()
                            .domain([0,matrix1.length])
                            .range([0, 380])

            var yScale = d3.scaleLinear()
                            .domain([0,maxDiff])
                            .range([380, 0])


            x_axis = d3.axisBottom()
                            .scale(xScale);

            y_axis = d3.axisLeft()
                            .scale(yScale);


            svg.select("#xaxis")
                .transition()
                .duration(1000)
                .call(x_axis)


            svg.select("#yaxis")
                .transition()
                .duration(1000)
                .call(y_axis)
               

            var theLine =  svg.selectAll("path").data([diffMatrix])
                            .transition()
                            .duration(1000)
                            .attr("transform", "translate(20,0)")
                            .attr("d", d3.line()
                            .x(function(d,i) { return xScale(i) })
                            .y(function(d,i) { return yScale(d[1]) }))
                            .attr("fill", "none")
                            .attr("stroke", "black")
                            .attr("stroke-width", 2)
                        
            
            
        })
    })
}
