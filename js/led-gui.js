// constants
NUM_LAYERS = 3;
NUM_ROWS = 3;
NUM_COLS = 3;

var currentPattern = null;
var currentFrameIndex = 0;
var currentFrame = null;

// frame object
function Frame(L0, L1, L2) {
  this.layers = Array();
  this.layers[0] = L0;
  this.layers[1] = L1;
  this.layers[2] = L2;
}

// pattern object
function Pattern() {
  this.frames = Array();

  this.del_frame = function() {
    if(this.frames.length > 1) {
      this.frames.splice(currentFrameIndex, 1);
      if(currentFrameIndex > 0) {
        currentFrameIndex -= 1;
      }
      currentFrame = this.frames[currentFrameIndex];
    }
  }

  this.mov_frame = function(direction) {
    console.log("Moving frame " + direction)
    if(direction === "right" && currentFrameIndex+1 < this.frames.length) {
      var temp = this.frames[currentFrameIndex];
      this.frames[currentFrameIndex] = this.frames[currentFrameIndex+1];
      this.frames[currentFrameIndex+1] = temp;
      currentFrameIndex += 1;
    }
    else if (direction === "left" && currentFrameIndex-1 >= 0) {
      var temp = this.frames[currentFrameIndex];
      this.frames[currentFrameIndex] = this.frames[currentFrameIndex-1]
      this.frames[currentFrameIndex-1] = temp;
      currentFrameIndex -= 1;
    }
    else {

    }
  }

  this.add_frame = function() {
    // read current frame state
    var newFrame = new Frame(0, 0, 0);
    this.frames.splice(currentFrameIndex+1, 0, newFrame);
    currentFrameIndex++;
    currentFrame = this.frames[currentFrameIndex];
  }
}

// update gui
function update() {
  update_pattern_display();
  update_frame_display();
}

// draw pattern display
function update_pattern_display() {
  var display = document.getElementById("pattern-view");
  del_children(display);
  for(var i = 0; i < currentPattern.frames.length; i++) {
    var element = document.createElement("button");
    element.type = "button";
    element.textContent = i.toString();
    element.classList.add("btn-pattern-view");
    if(i == currentFrameIndex) {
      element.classList.add("selected");
    }
    display.appendChild(element);
  }
}

// draw frame display
function update_frame_display() {
  var display = document.getElementById("frame-view");
  del_children(display);
  for(var layer = 0; layer < NUM_LAYERS; layer++) {
    var layerbox = document.createElement("div");
    layerbox.className = "layerbox";
    display.appendChild(layerbox);
    var rowhead = document.createElement("span");
    rowhead.textContent = "Layer " + layer.toString();
    layerbox.appendChild(rowhead);
    for(var row = 0; row < NUM_ROWS; row++) {
      var rowbox = document.createElement("div");
      layerbox.appendChild(rowbox);
      for(var col = 0; col < NUM_COLS; col++) {
        var element = document.createElement("button");
        element.type = "button";
        element.id = layer.toString() + (row*NUM_ROWS + col).toString();
        element.textContent = (row*NUM_ROWS + col).toString();
        element.classList.add("btn-frame");
        if(currentFrame.layers[layer] & Math.pow(2, (row*NUM_ROWS + col))) {
          element.classList.add("selected");
        }
        rowbox.appendChild(element);
      }
    }
  }
}
// play button states

// delete children
function del_children(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}

function dec2bin(dec){
    return (dec >>> 0).toString(2);
}

document.addEventListener("click", function(event) {
  if(event.target.type == "button") {
    if(event.target.classList.contains("btn-frame")) {
      var id_string = event.target.id.toString();
      currentFrame.layers[parseInt(id_string[0])] = currentFrame.layers[parseInt(id_string[0])] ^ Math.pow(2, parseInt(id_string[1]));
    }
    else if (event.target.classList.contains("btn-main")) {
      switch(event.target.id) {
        case "btn-new-pattern":
          break;
        case "btn-load-pattern":
          break;
        case "btn-save-pattern":
          break;
        case "btn-export-pattern":
          break;
        default:
          break;
      }
    }
    else if (event.target.classList.contains("btn-pattern")) {
      switch(event.target.id) {
        case "btn-add-frame":
          currentPattern.add_frame();
          break;
        case "btn-del-frame":
          currentPattern.del_frame();
          break;
        case "btn-mov-frame-right":
          currentPattern.mov_frame("right");
          break;
        case "btn-mov-frame-left":
          currentPattern.mov_frame("left");
          break;
        default:
          break;
      }
    }
    else if (event.target.classList.contains("btn-pattern-view")) {
      console.log("Text Content: " + event.target.textContent);
      console.log(currentPattern.frames)
      currentFrame = currentPattern.frames[parseInt(event.target.textContent)];
      currentFrameIndex = parseInt(event.target.textContent);
    }
    else {
      console.log("Other button pressed")
    }
  }

  update();

})

function init() {
  currentPattern = new Pattern();
  currentPattern.frames.push(new Frame(0,0,0));
  currentFrame = currentPattern.frames[0];
  update();
}

init();
