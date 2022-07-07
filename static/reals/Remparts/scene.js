// Scene Camera & Renderer

const renderer = new THREE.WebGLRenderer({
  antialias: false,
  preserveDrawingBuffer: true,
});
renderer.setSize(window.innerWidth, window.innerHeight);

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.LinearToneMapping;
renderer.toneMappingExposure = 0.9;

scene = new THREE.Scene();
scene.background = new THREE.Color(0x609fc3);
scene.fog = new THREE.Fog(0x609fc3, 1, 250);

camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  20000
);
camera.position.z = 40;

const objects = [];

let raycaster;
let moveForward = false;
let moveBackward = false;
let moveLeft = false;
let moveRight = false;
let canJump = false;

let prevTime = performance.now();
const velocity = new THREE.Vector3();
const direction = new THREE.Vector3();

const loader = new THREE.OBJLoader();

// Controls

const controls = new THREE.PointerLockControls(camera, document.body);

const blocker = document.getElementById("blocker");
const instructions = document.getElementById("instructions");

instructions.addEventListener("click", function () {
  controls.lock();
});

controls.addEventListener("lock", function () {
  instructions.style.display = "none";
  blocker.style.display = "none";
});

controls.addEventListener("unlock", function () {
  blocker.style.display = "block";
  instructions.style.display = "";
});

scene.add(controls.getObject());

const onKeyDown = function (event) {
  switch (event.code) {
    case "ArrowUp":
    case "KeyW":
      moveForward = true;
      break;

    case "ArrowLeft":
    case "KeyA":
      moveLeft = true;
      break;

    case "ArrowDown":
    case "KeyS":
      moveBackward = true;
      break;

    case "ArrowRight":
    case "KeyD":
      moveRight = true;
      break;

    case "Space":
      if (canJump) {
        velocity.y += 350;
      }
      canJump = false;
      break;
  }
};

const onKeyUp = function (event) {
  switch (event.code) {
    case "ArrowUp":
    case "KeyW":
      moveForward = false;
      break;

    case "ArrowLeft":
    case "KeyA":
      moveLeft = false;
      break;

    case "ArrowDown":
    case "KeyS":
      moveBackward = false;
      break;

    case "ArrowRight":
    case "KeyD":
      moveRight = false;
      break;
  }
};

document.addEventListener("keydown", onKeyDown);
document.addEventListener("keyup", onKeyUp);

raycaster = new THREE.Raycaster(
  new THREE.Vector3(),
  new THREE.Vector3(0, -1, 0),
  0,
  10
);

// Materials

const shield_material = new THREE.MeshPhysicalMaterial();
const bshield_material = new THREE.MeshPhysicalMaterial();
const beams_material = new THREE.MeshPhysicalMaterial();
const metal_material = new THREE.MeshPhysicalMaterial();
const arrow_material = new THREE.MeshPhysicalMaterial();

shieldTexture = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/Diff.jpg`
);
shieldNorm = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/Norm.jpg`
);
shieldSpec = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/Spc.jpg`
);
shieldMetal = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/Mtl.jpg`
);
bshieldTexture = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/BDiff.jpg`
);
bshieldNorm = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/BNorm.jpg`
);
bshieldSpec = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/BSpc.jpg`
);
metalTexture = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/MetalD.jpg`
);
metalNorm = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/MetalN.jpg`
);
metalSpec = new THREE.TextureLoader().load(
  `${static_url}/assets/textures/MetalS.jpg`
);

// Herse

const herse = new THREE.Group();

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);

cube.scale.x = 0.1;
cube.scale.y = 0.1;
cube.scale.z = 0.1;

cube.position.z -= 20.5;
cube.position.y += 13.25;
cube.visible = false;

scene.add(cube);

const geometry2 = new THREE.BoxGeometry();
const material2 = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube2 = new THREE.Mesh(geometry2, material2);

cube2.scale.x = 0.1;
cube2.scale.y = 0.1;
cube2.scale.z = 0.1;

cube2.position.z -= 20.5;
cube2.visible = false;

scene.add(cube2);

const geometry3 = new THREE.BoxGeometry();
const material3 = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube3 = new THREE.Mesh(geometry3, material3);

cube3.scale.x = 0.1;
cube3.scale.y = 0.1;
cube3.scale.z = 0.1;

cube3.position.z -= 20.5;
cube3.position.y += 5.125;
cube3.visible = false;

scene.add(cube3);

loader.load(`${static_url}/assets/obj/shield.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });
  object.position.z += 0.175;
  object.scale.set(1.5, 1.5, 1.5);

  object.traverse(function (child) {
    if (child instanceof THREE.Mesh) {
      child.material = shield_material;
      child.material.side = THREE.DoubleSide;

      child.material.map = shieldTexture;
      child.material.normalMap = shieldNorm;
      child.material.roughnessMap = shieldSpec;
      child.material.metalnessMap = shieldMetal;

      child.material.roughness = 2.75;
      child.material.metalness = 1;
      child.material.envMapIntensity = 0.05;
      child.material.normalScale = new THREE.Vector2(-0.5, -0.5);
    }
  });

  shield = object;
});

loader.load(`${static_url}/assets/obj/back.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });
  object.position.z += 0.175;
  object.scale.set(1.5, 1.5, 1.5);

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
      child.material.normalScale = new THREE.Vector2(-0.5, -0.5);
    }
  });

  bshield = object;
});

loader.load(`${static_url}/assets/obj/beams.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });
  object.position.z -= 5.695;

  beamsTexture = new THREE.TextureLoader().load(
    `${static_url}/assets/textures/beamsD.jpg`
  );
  beamsTexture.wrapS = beamsTexture.wrapT = THREE.RepeatWrapping;
  beamsTexture.repeat.set(2, 2);

  beamslNorm = new THREE.TextureLoader().load(
    `${static_url}/assets/textures/beamsN.jpg`
  );
  beamslNorm.wrapS = beamslNorm.wrapT = THREE.RepeatWrapping;
  beamslNorm.repeat.set(2, 2);

  beamsSpec = new THREE.TextureLoader().load(
    `${static_url}/assets/textures/beamsS.jpg`
  );
  beamsSpec.wrapS = beamsSpec.wrapT = THREE.RepeatWrapping;
  beamsSpec.repeat.set(2, 2);

  object.traverse(function (child) {
    if (child instanceof THREE.Mesh) {
      child.material = beams_material;

      child.material.map = beamsTexture;
      child.material.normalMap = beamslNorm;
      child.material.roughnessMap = beamsSpec;

      child.material.roughness = 1.1;
      child.material.envMapIntensity = 0.05;
      child.material.normalScale = new THREE.Vector2(0.25, 0.25);
    }
  });

  beams = object;
});

loader.load(`${static_url}/assets/obj/ornaments.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });
  object.position.z -= 5.695;

  object.traverse(function (child) {
    if (child instanceof THREE.Mesh) {
      child.material = metal_material;

      child.material.map = metalTexture;
      child.material.normalMap = metalNorm;
      child.material.roughnessMap = metalSpec;

      child.material.roughness = 1.25;
      child.material.metalness = 0.2;
      child.material.envMapIntensity = 0.05;
      child.material.normalScale = new THREE.Vector2(-0.5, -0.5);
    }
  });

  ornaments = object;

  herse.add(shield);
  herse.add(bshield);
  herse.add(beams);
  herse.add(ornaments);
  herse.add(chains);

  scene.add(herse);

  herse.position.z -= 20.5;
  herse.position.y += 5.25;
  herse.scale.set(0.5, 0.5, 0.5);
});

loader.load(`${static_url}/assets/obj/chains.obj`, function (object) {
  object.traverse(function (child) {
    child.castShadow = true;
  });
  object.traverse(function (child) {
    child.receiveShadow = true;
  });
  object.position.z -= 5.725;

  object.traverse(function (child) {
    if (child instanceof THREE.Mesh) {
      child.material = metal_material;

      child.material.map = metalTexture;
      child.material.normalMap = metalNorm;
      child.material.roughnessMap = metalSpec;

      child.material.roughness = 1.25;
      child.material.metalness = 0.2;
      child.material.envMapIntensity = 0.05;
      child.material.normalScale = new THREE.Vector2(-0.5, -0.5);
    }
  });

  chains = object;
});

// Animation & render

function animate() {
  requestAnimationFrame(animate);

  const time = performance.now();

  raycaster.ray.origin.copy(controls.getObject().position);
  raycaster.ray.origin.y -= 10;

  const intersections = raycaster.intersectObjects(objects);
  const onObject = intersections.length > 0;
  const delta = (time - prevTime) / 1000;
  const delta2 = (time - prevTime) / 25000;

  velocity.x -= velocity.x * 10.0 * delta;
  velocity.z -= velocity.z * 10.0 * delta;
  velocity.y -= 400 * 100.0 * delta2;

  direction.z = Number(moveForward) - Number(moveBackward);
  direction.x = Number(moveRight) - Number(moveLeft);
  direction.normalize();

  if (moveForward || moveBackward) velocity.z -= direction.z * 100.0 * delta;
  if (moveLeft || moveRight) velocity.x -= direction.x * 100.0 * delta;

  if (onObject === true) {
    velocity.y = Math.max(1000, velocity.y);
    canJump = true;
  }

  controls.moveRight(-velocity.x * delta);
  controls.moveForward(-velocity.z * delta);
  controls.getObject().position.y += velocity.y * delta2;

  if (controls.getObject().position.y < 1.75) {
    velocity.y = 0;
    controls.getObject().position.y = 1.75;
    canJump = true;
  }

  prevTime = time;

  renderer.render(scene, camera);
  renderer.setPixelRatio(window.devicePixelRatio);

  if (resizeRendererToDisplaySize(renderer)) {
    const canvas = renderer.domElement;
    camera.aspect = canvas.clientWidth / canvas.clientHeight;
    camera.updateProjectionMatrix();
  }

  const target = cube2.position;
  const distance = camera.position.distanceTo(target);

  if (distance < 10) {
    herse.position.lerp(cube.position, 0.015);
  } else if (distance > 10) {
    if (herse.position.y > 5) {
      herse.position.lerp(cube3.position, 0.015);
    }
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
