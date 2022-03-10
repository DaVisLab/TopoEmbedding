
//import { loadImage } from './inputimage.js'

var node_id1
var node_id2
var data_ensemble = new Array();

var node_tooltip = d3.select('body')
      	.append('div')
      	.style('position', 'absolute')
        .style('z-index', '10')
      	.style('color',  d3.rgb(20, 20, 20))
        .style('visibility', 'hidden')  
        .style('font-size', '12px')
      	.style('font-weight', 'bold')
      	.text('');

function clickOnNodes(e)
{

  var svg_force = d3.select("#svg_force")

  var node_id = d3.select(this).attr("id");
  var old_node_id

  if(working_on_layer1){
    old_node_id = node_id1;
    node_id1 = node_id;
    folder_1 = node_id1.split('_')[1];
    id_1 = node_id1.split('_')[2];
    
  }
  else{
    old_node_id = node_id2
    node_id2 = node_id
    folder_2 = node_id2.split('_')[1];
    id_2 = node_id2.split('_')[2];
  }

  var folder = node_id.split('_')[1];
  var id = node_id.split('_')[2];
  
  var ensemble_size = data_ensemble.length; 
  data_ensemble.push([ensemble_size, folder, id]);
  ensemble_size = data_ensemble.length;
  
  loadPersistenceImage(folder,id);
 // loadImage(folder,id);
  document.getElementById('filterCycles').onchange();


  if(node_id2 != undefined && node_id1 != undefined){
    console.log(node_id1)
    console.log(node_id2)
    
    var folder1 = node_id1.split('_')[1];
    var id1 = node_id1.split('_')[2];
  
    var folder2 = node_id2.split('_')[1];
    var id2 = node_id2.split('_')[2];
  
    showMinkowskiDiff(folder1, id1, folder2, id2)

  }

  d3.select("#"+node_id).style("fill", "red");
  d3.select("#"+old_node_id).style("fill", "black");

}


export function loadJsonFile()
{

  d3.json("data/mnist_embeddings/embeddings_Isomap.json").then(function(data){ 
    

    var svg_force = d3.select("#svg_force")

    var height = document.body.clientHeight-200;
    var width = height

    d3.select("#svg_force").attr("height", height)
    d3.select("#svg_force").attr("width", width)

    console.log(height, width)
    
    var g = svg_force.append('g')

  //  console.log(svg_force)
   // console.log(height, width)
    
    const zoom = d3.zoom()
    .on('zoom', (event) => {
      g.attr('transform', event.transform);
    })
    .scaleExtent([0, 10])

    svg_force.call(zoom);


    var names = data.name
    var xcoords = data.x
    var ycoords = data.y

    var scaleX = d3.scaleLinear()
                  .domain(d3.extent(xcoords))
                  .range([0,width])

    var scaleY = d3.scaleLinear()
                  .domain(d3.extent(ycoords))
                  .range([0,height])

                                  
    const nodeElements = g.append('g')
                            .selectAll('circle')
                            .data(names)
                            .enter().append('circle')
                            .attr('r', 1)
                            .attr('fill', 'black')
                            .attr("cx", (d,i) => scaleX(xcoords[i]))
                            .attr("cy", (d,i) => scaleY(ycoords[i]))
                            .attr('id', d => ("circle" + "_" + d.split("/")[0] + "_"+ d.split("/")[1].split("_")[0]))
                            .attr("opacity", "0.5")
                            .on('click', clickOnNodes)
                            .on('mouseover', function(d){
                               node_tooltip.style('visibility', 'visible').text(d3.select(this).attr("id")).style('top', (event.pageY - 10)+'px').style('left',(event.pageX+10)+'px');
                            })
                            .on('mouseout',function(d){
                               node_tooltip.style('visibility', 'hidden');
                            })

    const textElements = g.append('g')
                            .selectAll('text')
                            .data(names)
                            .enter()
                            .append('text')
                            .text(d => d.split("/")[0])
                            .attr('font-size', 4)
                            .attr("x", (d,i) => scaleX(xcoords[i]))
                            .attr("y", (d,i) => scaleY(ycoords[i]))
                            .attr("dx", 2)
                            .attr("dy", 2)
                            .attr("pointer-events","none")
                            .attr("fill", "black")

  })
    
  
}

