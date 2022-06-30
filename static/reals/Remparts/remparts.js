const basic_material = new THREE.MeshStandardMaterial({ color: 0x808080 });
const ground_material = new THREE.MeshPhysicalMaterial();
const tower_material = new THREE.MeshPhysicalMaterial();

wallTexture = new texture('wallTexture', 'wallD2.jpg', [10, 10]).init();
wallNorm = new texture('wallNorm', 'wallN2.jpg', [10, 10]).init();
wallRough = new texture('wallRough', 'wallR2.jpg', [10, 10]).init();

const tower_1 = new object(1, 'tower', -20.195, -0.1, tower_material, wallTexture, wallNorm, wallRough, 0.05, 0.75, [0.25, 0.25], [0.5, 0.5, 0.5]).create();

const tower_2 = new object(2, 'tower2', -20.195, -0.1, tower_material, wallTexture, wallNorm, wallRough, 0.05, 0.75, [0.25, 0.25], [0.5, 0.5, 0.5]).create();

const gate = new object(3, 'gate', -20.195, -0.1, basic_material, null, null, null, 0.05, 0.75, [0.25, 0.25], [0.5, 0.5, 0.5]).create();

const bloc_1 = new object(4, 'bloc1', -20.195, -0.1, basic_material, null, null, null, 0.05, 0.75, [0.25, 0.25], [0.5, 0.5, 0.5]).create();

const bloc_2 = new object(5, 'bloc2', -20.195, -0.1, basic_material, null, null, null, 0.05, 0.75, [0.25, 0.25], [0.5, 0.5, 0.5]).create();

terrTexture = new texture('terrTexture', 'terrasseD.jpg', [500, 500]).init();
terrNorm = new texture('terrNorm', 'terrasseN.jpg', [500, 500]).init();
terrSpec = new texture('terrSpec', 'terrasseS.jpg', [500, 500]).init();

const city_map = new object(6, 'city_map', 0, -51.275, ground_material, terrTexture, terrNorm, terrSpec, 0.01, 0.25, [1, 1], [1, 1, 1]).create();        