var viewWindow = document.getElementById("cube-view");

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75,
                                          300 / 300,
                                          0.1,
                                          1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(400, 400);
viewWindow.appendChild(renderer.domElement);

camera.position.z = 5;

var controls = new THREE.OrbitControls(camera);

// define geometries
var geometry_led = new THREE.BoxGeometry(0.25,0.25,0.25);
var geometry_base = new THREE.BoxGeometry(3,0.25,3);

// define materials
var material_on = new THREE.MeshBasicMaterial({color: 0xFF0000});
var material_off = new THREE.MeshBasicMaterial({color: 0x590808});
var material_base = new THREE.MeshBasicMaterial({color: 0xAA4500});


function clear_scene() {
  while(scene.children.length > 0) {
    scene.remove(scene.children[0]);
  }
}

function fill_scene() {
  // add leds
  for(var yy = -1; yy <= 1; yy++) {
    for(var xx = -1; xx <=1; xx++) {
      for(var zz = -1; zz <= 1; zz++) {
        if(currentFrame.layers[yy+1] & Math.pow(2, (zz+1)*NUM_ROWS + xx+1)) {
          var cube = new THREE.Mesh(geometry_led, material_on);
        }
        else {
          var cube = new THREE.Mesh(geometry_led, material_off);
        }

        scene.add(cube);
        cube.position.set(xx,yy,zz);
      }
    }
  }

  // add base
  var base = new THREE.Mesh(geometry_base, material_base);
  scene.add(base);
  base.position.set(0,-2, 0)
}

function render() {
  clear_scene();
  fill_scene();
	requestAnimationFrame( render );
	renderer.render( scene, camera );
  //controls.update();
}
render();
