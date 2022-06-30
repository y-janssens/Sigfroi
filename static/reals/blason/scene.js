// Scene Camera & Renderer

const renderer = new THREE.WebGLRenderer({
  antialias: false,
  preserveDrawingBuffer: true,
  alpha: true,
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x000000, 0);
document.body.appendChild(renderer.domElement);

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputEncoding = THREE.LinearEncoding;

scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

camera.position.set(0, 0, 5);

const shield_material = new THREE.MeshPhysicalMaterial();
const bshield_material = new THREE.MeshPhysicalMaterial();
const loader = new THREE.OBJLoader();

const pmremGenerator = new THREE.PMREMGenerator(renderer);
pmremGenerator.compileEquirectangularShader();

const rgbl = new THREE.RGBELoader();
rgbl.setDataType(THREE.UnsignedByteType);
rgbl.setPath(`${static_url}/src/`);
rgbl.load("map.hdr", function (texture) {
  const envMap = pmremGenerator.fromEquirectangular(texture).texture;
  scene.environment = envMap;
});

const rotation_speed = 0.01;

let floorGeometry = new THREE.PlaneGeometry(20, 20);
let floorMaterial = new THREE.ShadowMaterial();
floorMaterial.opacity = 0.55;
let floorMesh = new THREE.Mesh(floorGeometry, floorMaterial);
floorMesh.rotation.x = -Math.PI / 2;
floorMesh.receiveShadow = true;
floorMesh.side = THREE.DoubleSide;
floorMesh.position.y -= 2.7;
scene.add(floorMesh);

// Lights

const ambiant = new THREE.AmbientLight(0xffffff, 0.1);
scene.add(ambiant);

const light = new THREE.SpotLight(0xffffff, 0.75);
light.position.set(100, 100, 100);
light.castShadow = true;

light.shadow.mapSize = new THREE.Vector2(2048, 2048);
light.shadow.camera.near = 15;
light.shadow.focus = 0.165;
light.shadow.bias = 0.000001;
light.shadow.normalBias = 0.02;

scene.add(light);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.1);
directionalLight.position.y = 3;
directionalLight.position.x = -5;
directionalLight.position.z = -5;

scene.add(directionalLight);

// Objects

testshield = loader.load(`${static_url}/src/shield.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });

  shieldTexture = new THREE.TextureLoader().load(`${static_url}/src/Diff.jpg`);
  shieldNorm = new THREE.TextureLoader().load(`${static_url}/src/Norm.jpg`);
  shieldSpec = new THREE.TextureLoader().load(`${static_url}/src/Spc.jpg`);
  shieldMetal = new THREE.TextureLoader().load(`${static_url}/src/Mtl.jpg`);
  object.traverse(function (child) {
    if (child instanceof THREE.Mesh) {
      child.material = shield_material;
      child.material.side = THREE.DoubleSide;

      child.material.map = shieldTexture;
      child.material.normalMap = shieldNorm;
      child.material.roughnessMap = shieldSpec;
      child.material.metalnessMap = shieldMetal;

      child.material.roughness = 2;
      child.material.reflectivity = 0.1;
      child.material.metalness = 0.15;
      child.material.envMapIntensity = 0.05;
      child.material.normalScale = new THREE.Vector2(0.5, 0.5);
    }
  });

  fshield = object;

  shield = new THREE.Group();

  shield.add(fshield);

  scene.add(shield);

  function animate() {
    requestAnimationFrame(animate);
    fshield.rotation.y += rotation_speed;
  }

  animate();
});

loader.load(`${static_url}/src/back.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });

  bshieldTexture = new THREE.TextureLoader().load(`${static_url}/src/BDiff.jpg`);
  bshieldNorm = new THREE.TextureLoader().load(`${static_url}/src/BNorm.jpg`);
  bshieldSpec = new THREE.TextureLoader().load(`${static_url}/src/BSpc.jpg`);
  object.traverse(function (child) {
    if (child instanceof THREE.Mesh) {
      child.material = bshield_material;
      child.material.side = THREE.DoubleSide;

      child.material.map = bshieldTexture;
      child.material.normalMap = bshieldNorm;
      child.material.roughnessMap = bshieldSpec;

      child.material.roughness = 2;
      child.material.reflectivity = 0.1;
      child.material.envMapIntensity = 0.05;
      child.material.normalScale = new THREE.Vector2(0.5, 0.5);
    }
  });

  bshield = object;
  scene.add(bshield);

  function animate() {
    requestAnimationFrame(animate);
    bshield.rotation.y += rotation_speed;
  }

  animate();
});

// Controls

const controls = new THREE.OrbitControls(camera, renderer.domElement);

controls.maxPolarAngle = Math.PI / 2;
controls.minPolarAngle = Math.PI / 2;
controls.enableDamping = true;
controls.enablePan = false;
controls.dampingFactor = 0.1;
controls.autoRotate = false;
controls.autoRotateSpeed = 1;
controls.maxDistance = 5;
controls.minDistance = 3;
controls.zoomSpeed = 0.5;
controls.rotateSpeed = 0.5;

// Animation & render

function animate() {
  renderer.render(scene, camera);

  renderer.setPixelRatio(window.devicePixelRatio);

  requestAnimationFrame(animate);

  controls.update();

  if (resizeRendererToDisplaySize(renderer)) {
    const canvas = renderer.domElement;
    camera.aspect = canvas.clientWidth / canvas.clientHeight;
    camera.updateProjectionMatrix();
  }
}

animate();

function resizeRendererToDisplaySize(renderer) {
  const canvas = renderer.domElement;
  var width = window.innerWidth;
  var height = window.innerHeight;
  var canvasPixelWidth = canvas.width / window.devicePixelRatio;
  var canvasPixelHeight = canvas.height / window.devicePixelRatio;

  const needResize = canvasPixelWidth !== width || canvasPixelHeight !== height;
  if (needResize) {
    renderer.setSize(width, height, true);
  }
  return needResize;
}
