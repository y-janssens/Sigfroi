class object {
    constructor(id, file, posz, posy, material, map, normalMap, roughnessMap, envMapIntensity, roughness, normalScale, scaleSet){
        this.id = id;
        this.file = file;
        this.posz = posz;
        this.posy = posy;
        this.material = material;
        this.map = map;
        this.normalMap = normalMap;
        this.roughnessMap = roughnessMap;
        this.envMapIntensity = envMapIntensity;
        this.roughness = roughness;
        this.normalScale = normalScale;
        this.scaleSet = scaleSet;
    }
    create() {        
        let mesh = "mesh" + this.id;
        let link = `${static_url}/assets/obj/` + this.file + '.obj';
        let posz = this.posz;
        let posy = this.posy;
        let material = this.material;
        let map = this.map;
        let normalMap = this.normalMap;
        let roughnessMap = this.roughnessMap;
        let envMapIntensity = this.envMapIntensity;
        let roughness = this.roughness;
        let normalScale = this.normalScale;
        let scaleSet = this.scaleSet;

    loader.load(
        link, function (object) {			
    
        object.traverse(function(child){child.castShadow = true;});
        object.traverse(function(child){child.receiveShadow = true;});
        object.position.z = posz;
        object.position.y = posy;
    
        object.traverse( function( child ) {
        if ( child instanceof THREE.Mesh ) {
    
        child.material = material;
        
        child.material.map = map;
        child.material.normalMap = normalMap;
        child.material.roughnessMap = roughnessMap;
    
        child.material.envMapIntensity = envMapIntensity; 
        child.material.roughness = roughness;
        
        child.material.normalScale = new THREE.Vector2(normalScale[0], normalScale[1]);
            }
        } );
        mesh = object ;
        mesh.scale.set (scaleSet[0], scaleSet[1], scaleSet[2]);
        scene.add (mesh);    
        });
    }
}

class texture {
    constructor(name, file, repeat){
        this.name = name;
        this.file = file;
        this.repeat = repeat;
    }
    init(){
        this.name = new THREE.TextureLoader().load(`${static_url}/assets/textures/` + this.file);
        this.name.wrapS = this.name.wrapT = THREE.RepeatWrapping;
        this.name.repeat.set(this.repeat[0], this.repeat[1]);
        return this.name;
    }
}