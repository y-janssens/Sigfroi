const pmremGenerator = new THREE.PMREMGenerator( renderer );
pmremGenerator.compileEquirectangularShader();

const rgbl = new THREE.RGBELoader();
rgbl.setDataType( THREE.UnsignedByteType )
rgbl.setPath( `${static_url}/assets/textures/` )
rgbl.load( 'goegap_1k.hdr', function ( texture ) {

const envMap = pmremGenerator.fromEquirectangular( texture ).texture;
scene.environment = envMap;
//scene.background = envMap;
})

const amb = new THREE.AmbientLight( 0xffffff, 0.75 );

scene.add( amb );
        
const light = new THREE.DirectionalLight( 0xffffff, 1.5 );
light.position.set( 50, 100, 50 );   
light.castShadow = true;

light.shadow.mapSize = new THREE.Vector2(1024, 1024);
light.shadow.camera.near = 0.1;
light.shadow.camera.far = 2000;
light.shadow.focus = 0.105;
light.shadow.bias = 0.00001;
light.shadow.normalBias = 0.02;

const d = 100;

light.shadow.camera.left = - d;
light.shadow.camera.right = d;
light.shadow.camera.top = d;
light.shadow.camera.bottom = - d;

scene.add( light );

const textureLoader = new THREE.TextureLoader();

const textureFlare0 = textureLoader.load( `${static_path}/lensflare/lensflare0.png` );
const textureFlare1 = textureLoader.load( `${static_path}/lensflare/lensflare2.png` );
const textureFlare2 = textureLoader.load( `${static_path}/lensflare/lensflare3.png` );

const lensflare = new THREE.Lensflare();

lensflare.addElement( new THREE.LensflareElement( textureFlare0, 512, 0, light.color ) );
lensflare.addElement( new THREE.LensflareElement( textureFlare2, 60, 0.6 ) );
lensflare.addElement( new THREE.LensflareElement( textureFlare2, 70, 0.7 ) );
lensflare.addElement( new THREE.LensflareElement( textureFlare2, 120, 0.9 ) );
lensflare.addElement( new THREE.LensflareElement( textureFlare2, 70, 1 ) );

light.add( lensflare );
lensflare.visible = true;