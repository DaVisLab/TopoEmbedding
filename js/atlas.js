
var w = 500;
var h = 500;
var num_pixel = 50;
var pixel_w = (w - 20) / num_pixel;
var pixel_h = 20;
var circle_ridius = 5.0;
var color_list = ['blue','red'];
var color_function = [d3.interpolateRgb, d3.interpolateHsl, d3.interpolateHcl];
var color_array = [];
color_array =  d3.scaleLinear().domain([0, num_pixel]).interpolate(color_function[0]).range([color_list[0], color_list[1]]);
var  cycle_atlas = new Array();
var max = -10, min = 10;
function initiateAtlas()
{
    var svg_atlas = d3.select("#persistence_atlas")
                .attr("height", w)
                .attr("width", h);
}
function createAtlas(folder, id, n)
{
   var pixel_data = new Array();
   var svg_atlas = d3.select("#persistence_atlas");
   for(var i = 0; i < num_pixel; i++){
       svg_atlas.append("rect")
                  .attr("x", pixel_w * (i + 0.5))
                  .attr("y", pixel_h * n)
                  .attr("width", pixel_w)
                  .attr("height", pixel_h)
                  .attr("fill", color_array(i))
                  .style("stroke","black")
                  .style("stroke-width", "0px"); 
   }
  var path = "./data/mnist_pd/"+folder+"/"+id+"_pd.csv";
  var temp = d3.randomUniform(0, 255);
  var data_color = d3.rgb(d3.randomUniform(0, 255)(),d3.randomUniform(0, 255)(),d3.randomUniform(0, 255)());
  var cycle_area = new Array();
  
  d3.text(path).then(function(data){
       var count = 0;
       data = d3.csvParseRows(data);
       data.forEach(element => {
           size = element.length
           var values = Object.keys(element).map(function(key){
                return element[key];
           }); 
           var type = parseInt(values[2]);
           if(type==1){
               var death = parseFloat(values[1]);
               var birth = parseFloat(values[0]);
               var persistence = death - birth;
               cycle_atlas.push([folder,id,count,persistence]);
               max = max > persistence ? max : persistence;
               min = min < persistence ? min : persistence;
               svg_atlas.append("circle")
               .attr("cx", w * persistence + 20)
               .attr("cy", pixel_h * n + 10)
               .attr("r", circle_ridius)
               .style("fill", data_color)
               .style("stroke", "black")
               .style("stroke-width", "2px")
               .attr("id", folder + "_" + id + "_" + count)
               .on("click", onClickShowCycle)
               .on('mouseover',function(){
                    currentObject = d3.select(this).style("stroke","white").style("stroke-width", "2px"); 
               })
               .on('mouseout',function(){
                    currentObject = d3.select(this).style("stroke","black").style("stroke-width", "2px"); 
               })
               count++;
           }
        });

  });            
}
function onClickShowCycle()
{
   
    var circle_id =  d3.select(this).attr("id");
    
    var folder = circle_id.split('_')[0];
    var data_id = circle_id.split('_')[1];
    var cycle_id = circle_id.split('_')[2];

    var sizeSvg = document.body.clientWidth/10
    
    var canvas_image;

    canvas_image = "webgl_surface3"
   
    var canv = document.getElementById( canvas_image );
    
    canv.setAttribute("width", sizeSvg)
    canv.setAttribute("height", sizeSvg)

    var renderer
  
    renderer = new THREE.WebGLRenderer({canvas: canv, antialias: true, alpha: true});
    renderer.setSize( sizeSvg, sizeSvg );

    var scene = new THREE.Scene();
    scene.background = new THREE.Color( 0xff0000 );

    var fieldOfView = 75;
    var aspectRatio = sizeSvg / sizeSvg;

    var nearPlane = 0.1;
    var farPlane = 100;

    var camera = new THREE.PerspectiveCamera(
        fieldOfView, aspectRatio, nearPlane, farPlane
      );

    camera.position.z = 5;


    var loader = new THREE.TextureLoader();
    var url =  "./data/mnist_png/testing/"+folder+"/"+ data_id +".png"

    var geometry = new THREE.PlaneGeometry(8, 8);
    var material = new THREE.MeshLambertMaterial({
        map: loader.load(url)
      });

    var mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(0,0,0)


    var light = new THREE.PointLight( 0xffffff, 1, 0 );
    light.position.set(1, 1, 100 );
    scene.add(mesh);
    scene.add(light);

    var path = "./data/mnist_cycles/"+folder+"/"+ data_id +"_cycle.json"

    const line_material = new THREE.LineBasicMaterial( { color: 0x0000ff } );


    d3.json(path).then(function(data){
       const points = [];
       data[cycle_id].forEach(d => {
                        points.push( new THREE.Vector3( d[1]-13.5, 13.5-d[0], d[2] ) );
        });
    
       const geometry = new THREE.BufferGeometry().setFromPoints( points );
       const line = new THREE.Line( geometry, line_material );
       line.scale.set(8/27,8/27,8/27);
       scene.add(line);  
       setTimeout(function(){ renderer.render(scene, camera) },100);
       //renderer.render(scene, camera)
    })

}
