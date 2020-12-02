let mobilenet;

function modelReady(){
    console.log('Model is ready!!!');
    mobilenet.predict(img, gotResults);
}

function gotResults(err, results){
  if(err){
    cosole.error(err);
  }
  else{
    console.log(results);
    let label = results[0].clssNname;
    fill(0);
    textSize(64);
    text(label, 10, height-100);
  }
}

funtion imageReady(){
    image(img, 0, 0, width, height);
}
function setup(){
  createCanvas(640, 480);
  img = createImg('', imageReady);
  img.hide();
  background(0);

  mobilenet = ml5.imageClassifier('MobileNet', modelReady);
}
