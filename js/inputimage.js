import * as THREE from './threejs/three.module.js';

var renderer_dict = {}
var lines_dict = {}


function testCycles1(folder,id, is_on_layer1,cycle_list){
    
    var sizeSvg = document.body.clientWidth/10
    
    var canvas_image;

    if(is_on_layer1) canvas_image = "webgl_surface"
    else canvas_image = "webgl_surface2"

    lines_dict[canvas_image] = {}

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
    var url =  "./data/mnist_png/testing/"+folder+"/"+id+".png"

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

    var path = "./data/mnist_cycles/"+folder+"/"+id+"_cycle.json"

    const line_material = new THREE.LineBasicMaterial( { color: 0x0000ff } );


    d3.json(path).then(function(data){
     
    
       for (var cycle_id in data){
            const points = [];
            if(cycle_list.has(parseInt(cycle_id))){ 
                  data[cycle_id].forEach(d => {
                        points.push( new THREE.Vector3( d[1]-13.5, 13.5-d[0], d[2] ) );
                  })
                  const geometry = new THREE.BufferGeometry().setFromPoints( points );
                  const line = new THREE.Line( geometry, line_material );
                  line.scale.set(8/27,8/27,8/27);
                  scene.add(line)
            }

        }
       setTimeout(function(){ renderer.render(scene, camera) },100);
       //renderer.render(scene, camera)
    })

    
}

var cycle_list1 = new Set();
var cycle_list2 = new Set();
var cycle_weights1 = new Array();
var cycle_weights2 = new Array();
function updatePersistenceCycles(pixelSet,cycle_list,cycle_weights,folder,id,is_on_layer1,cur_weight)
{
   var path = "./data/mnist_mapping/"+folder+"/"+id+"_mapping.json";
   var path1 = "./data/mnist_cycles/"+folder+"/"+id+"_cycle.json";
    d3.json(path).then(function(data){
         d3.json(path1).then(function(data1){
         cycle_list.clear();
         cycle_weights.splice(0,cycle_weights.length);
         var pixels = [];
         for (var cycle_id in data1){
             cycle_weights.push(0);
         }
         var entries = Object.entries(data);
         entries.forEach(function(element,i){
            if(pixelSet.has(i)){
                var value = element[1];
                var idx = value.idx;
                var w = value.weights;  
                idx.forEach(function(ele, j){
                    cycle_weights[ele]+= w[j];
                })
            }    
         });
      var min = 99, max = -99;
      cycle_weights.forEach(function(ele, i){
          min = ele < min ? ele : min;
          max = ele > max ? ele : max; 
      })
      cycle_weights.forEach(function(ele, i){
        if(pixelSet.size == 100 && cur_weight == 0.0){
            cycle_list.add(i);  
        } 
        else if (cur_weight == 0.0)
        {  
            if(ele>0) cycle_list.add(i);
        }
        else {
            var threshold = (max - min) * cur_weight + min;
            if(ele>threshold) cycle_list.add(i);
        }
          
          
      })
      testCycles1(folder,id,is_on_layer1,cycle_list);
      })
   });     

}
document.getElementById('filterCycles').onchange = function (){
   var cur_weight = this.value;
   if(folder_1 != undefined)updatePersistenceCycles(mySet,cycle_list1,cycle_weights1,folder_1, id_1, true,cur_weight/10.0);
   if(folder_2 != undefined)updatePersistenceCycles(mySet,cycle_list2,cycle_weights2,folder_2, id_2, false,cur_weight/10.0);
}