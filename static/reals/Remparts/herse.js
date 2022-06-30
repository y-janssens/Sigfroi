const shield_material = new THREE.MeshPhysicalMaterial();
const bshield_material = new THREE.MeshPhysicalMaterial();
const beams_material = new THREE.MeshPhysicalMaterial();
const metal_material = new THREE.MeshPhysicalMaterial();
const arrow_material = new THREE.MeshPhysicalMaterial();

shieldTexture = new THREE.TextureLoader().load( './assets/textures/Diff.jpg' );
shieldNorm = new THREE.TextureLoader().load( './assets/textures/Norm.jpg' );
shieldSpec = new THREE.TextureLoader().load( './assets/textures/Spc.jpg' );
shieldMetal = new THREE.TextureLoader().load( './assets/textures/Mtl.jpg');
bshieldTexture = new THREE.TextureLoader().load( './assets/textures/BDiff.jpg' );
bshieldNorm = new THREE.TextureLoader().load( './assets/textures/BNorm.jpg' );
bshieldSpec = new THREE.TextureLoader().load( './assets/textures/BSpc.jpg' );
metalTexture = new THREE.TextureLoader().load( './assets/textures/MetalD.jpg' );
metalNorm = new THREE.TextureLoader().load( './assets/textures/MetalN.jpg' );
metalSpec = new THREE.TextureLoader().load( './assets/textures/MetalS.jpg' );

const herse = new THREE.Group();

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );

cube.scale.x = 0.1;
cube.scale.y = 0.1;
cube.scale.z = 0.1;

cube.position.z -= 20.5;
cube.position.y += 13.25;
cube.visible = false;

scene.add( cube );

const geometry2 = new THREE.BoxGeometry();
const material2 = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube2 = new THREE.Mesh( geometry2, material2 );

cube2.scale.x = 0.1;
cube2.scale.y = 0.1;
cube2.scale.z = 0.1;

cube2.position.z -= 20.5;
cube2.visible = false;

scene.add( cube2 );

const geometry3 = new THREE.BoxGeometry();
const material3 = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube3 = new THREE.Mesh( geometry3, material3 );

cube3.scale.x = 0.1;
cube3.scale.y = 0.1;
cube3.scale.z = 0.1;

cube3.position.z -= 20.5;
cube3.position.y += 5.125;
cube3.visible = false;

scene.add( cube3 );

loader.load(
	'./assets/obj/shield.obj', function (object) {			

	object.traverse(function(child){child.castShadow = true;});
	object.traverse(function(child){child.receiveShadow = true;});
	object.position.z += 0.175;
	object.scale.set (1.5, 1.5, 1.5);

	object.traverse( function( child ) {
	if ( child instanceof THREE.Mesh ) {

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
	} );

	shield = object ;

	});

	loader.load(
	'./assets/obj/back.obj', function (object) {			

	object.traverse(function(child){child.castShadow = true;});
	object.traverse(function(child){child.receiveShadow = true;});
	object.position.z += 0.175;
	object.scale.set (1.5, 1.5, 1.5);

	object.traverse( function( child ) {
	if ( child instanceof THREE.Mesh ) {

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
	} );

	bshield = object ;
    
	});

	loader.load(
	'./assets/obj/beams.obj', function (object) {			

	object.traverse(function(child){child.castShadow = true;});
	object.traverse(function(child){child.receiveShadow = true;});
	object.position.z -= 5.695;

	beamsTexture = new THREE.TextureLoader().load( './assets/textures/beamsD.jpg' );
	beamsTexture.wrapS = beamsTexture.wrapT = THREE.RepeatWrapping;
	beamsTexture.repeat.set(2, 2);

	beamslNorm = new THREE.TextureLoader().load( './assets/textures/beamsN.jpg' );
	beamslNorm.wrapS = beamslNorm.wrapT = THREE.RepeatWrapping;
	beamslNorm.repeat.set(2, 2);

	beamsSpec = new THREE.TextureLoader().load( './assets/textures/beamsS.jpg' );
	beamsSpec.wrapS = beamsSpec.wrapT = THREE.RepeatWrapping;
	beamsSpec.repeat.set(2, 2);

	object.traverse( function( child ) {
	if ( child instanceof THREE.Mesh ) {
	child.material = beams_material;

	child.material.map = beamsTexture;
	child.material.normalMap = beamslNorm;
	child.material.roughnessMap = beamsSpec;

	child.material.roughness = 1.1;
	child.material.envMapIntensity = 0.05;
	child.material.normalScale = new THREE.Vector2(0.25, 0.25);
		}
	} );

	beams = object ;
    
	});

	loader.load(
	'./assets/obj/ornaments.obj', function (object) {			

	object.traverse(function(child){child.castShadow = true;});
	object.traverse(function(child){child.receiveShadow = true;});
	object.position.z -= 5.695;

	object.traverse( function( child ) {
	if ( child instanceof THREE.Mesh ) {

	child.material = metal_material;

	child.material.map = metalTexture;
	child.material.normalMap = metalNorm;
	child.material.roughnessMap = metalSpec;

	child.material.roughness = 1.25;
	child.material.metalness = 0.2;
	child.material.envMapIntensity = 0.05;
	child.material.normalScale = new THREE.Vector2(-0.5, -0.5);
		}
	} );

	ornaments = object ;
    

    
    herse.add (shield);
    herse.add (bshield);
    herse.add (beams);
    herse.add (ornaments);
    herse.add (chains);
    
    scene.add (herse);

    herse.position.z -= 20.5;
    herse.position.y += 5.25;
    herse.scale.set (0.5, 0.5, 0.5);
                   	
	});

	loader.load(
	'./assets/obj/chains.obj', function (object) {			

	object.traverse(function(child){child.castShadow = true;});
	object.traverse(function(child){child.receiveShadow = true;});
	object.position.z -= 5.725;

	object.traverse( function( child ) {
	if ( child instanceof THREE.Mesh ) {

	child.material = metal_material;

	child.material.map = metalTexture;
	child.material.normalMap = metalNorm;
	child.material.roughnessMap = metalSpec;

	child.material.roughness = 1.25;
	child.material.metalness = 0.2;
	child.material.envMapIntensity = 0.05;
	child.material.normalScale = new THREE.Vector2(-0.5, -0.5);
		}
	} );

	chains = object ;
    
	});

