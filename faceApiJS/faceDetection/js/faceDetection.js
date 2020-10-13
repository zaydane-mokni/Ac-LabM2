const video = document.getElementById('videoInput')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('./models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('./models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('./models'),
  faceapi.nets.faceExpressionNet.loadFromUri('./models'),
  faceapi.nets.ssdMobilenetv1.loadFromUri('./models')
]).then(startVideo)

async function startVideo() {
   navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
   await getData();
   recognizeFaces();
}

async function recognizeFaces() {
  const labeledFaceDescriptors = await loadLabeledImages();
  const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.8);

  video.addEventListener('play', () => {
    const canvas = faceapi.createCanvasFromMedia(video);
    document.body.append(canvas);
    const displaySize = { width: video.width, height: video.height };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
      const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceDescriptors();
      const resizedDetections = faceapi.resizeResults(detections, displaySize);

      const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor));
      canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);

      results.forEach( (result, i) => {
          const box = resizedDetections[i].detection.box;
          const drawBox = new faceapi.draw.DrawBox(box, {label: result.label.toString()});
          drawBox.draw(canvas);
    })
      // to add face expression
      //faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    }, 100);
  });
}

async function loadLabeledImages() {
  const labels = ['zaydane', 'test'];
  return Promise.all(
    labels.map(async label => {
      const descriptions = [];
      for (let i = 1; i <= 2; i++) {
        const img = await faceapi.fetchImage(`./images/${label}/${i}.jpg`);
        const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor();
        descriptions.push(detections.descriptor);
      }
      return new faceapi.LabeledFaceDescriptors(label, descriptions);
    })
  );
}

async function getData() {
  firebase.database()
  .ref('images')
  .once('value', async data => {
    data.forEach( item => {
      console.log(item.val());
    });
  });
}