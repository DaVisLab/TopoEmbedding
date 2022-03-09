
function createPersistenceImage(layer){

    var sizeSvg = document.body.clientWidth/10

    var svg = d3.select(layer)
                    .attr("height", sizeSvg)
                    .attr("width",sizeSvg);

    var scaleAxis = d3.scaleLinear()
        .domain([0,10])
        .range([0,sizeSvg])
      
      //insert the boxes
      var boxes = svg.selectAll("rect")
                  .data([...Array(100).keys()]).enter()
                  .append("rect")
                  .attr("x", d => scaleAxis(parseInt(d%10)))
                  .attr("y", d => scaleAxis(parseInt(d/10)))
                  .attr("width", sizeSvg/10)
                  .attr("height", sizeSvg/10)
                  .attr("fill", "white")
                  .attr("id", "box_pi")
                  .style("stroke","black")
                  .style("stroke-width", "1px");
     var slide = d3.select("#filterCycles")
                            .style("visibility", "visible")
                            .attr("min", 0)
                            .attr("max", 10.0)
                            .attr("value", 0.0)
}

function loadPersistenceImage(folder, id)             
{

    var path = "./data/mnist_pi/"+folder+"/"+id+"_pi.csv"
    
    d3.csv(path).then(function(data){

        var sizeSvg = document.body.clientWidth/10

        var pisvg 
        if(working_on_layer1) pisvg = "#svg_psImage"
        else pisvg = "#svg_psImage2"

        var svg = d3.select(pisvg)

        var matrix = []
        var size = 0

        //organize the elements of the matrix in a line
        data.forEach(element => {
            size = element.length
            var values = Object.keys(element).map(function(key){
                return element[key];
            });
            matrix = matrix.concat(values)
        });

        //create a linear color scale with values going from blue to red (we can change this)
        var colorscale = d3.scaleLinear()
                        .domain(d3.extent(matrix))
                        .range(["blue","red"])

        //create a linear scale for all the elements in the matrix
        var scaleAxis = d3.scaleLinear()
                      .domain([0,10])
                      .range([0,sizeSvg])
        
        //insert the boxes
        var boxes = svg.selectAll("#box_pi")
                    .data(matrix).transition().duration(400)
                    .attr("x", (d,i) => scaleAxis(parseInt(i%10)))
                    .attr("y", (d,i) => scaleAxis(parseInt(i/10)))
                    .attr("width", sizeSvg/10)
                    .attr("height", sizeSvg/10)
                    .attr("fill", d => colorscale(d))
                    .style("stroke","black")
                    .style("stroke-width", "1px");

        

    });
    
}


var mySet = new Set;
for(var i = 0;i<100;i++)mySet.add(i);
function updatePersistenceImages(valMin, valMax){
    
    filterValues  = diffMatrix.slice(valMin, valMax)
   
    mySet.clear();
    filterValues.forEach(d => mySet.add(d[0]))
    document.getElementById('filterCycles').onchange();

    d3.selectAll("#box_pi").style("opacity", 0.1)
    var selection = d3.selectAll("rect").filter((d, i) =>{
         
         return mySet.has(i%(diffMatrix.length));
     }) 
        

    var boxes = d3.selectAll("#box_pi").filter((d, i) =>{ return mySet.has(i%(diffMatrix.length))}).style("opacity", 1) 
    

    var xScale = d3.scaleLinear()
            .domain([0,100])
            .range([0, 380])

    d3.select("#selected_interval")
        .transition()
        .duration(1000)
        .attr("x", xScale(valMin))
        .attr("width", xScale(valMax-valMin))

}
