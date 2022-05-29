let acrobatieCombat1 = document.getElementById("acrobatieCombatJ1");
let acrobatieCombat2 = document.getElementById("acrobatieCombatJ2");
let adresseTir1 = document.getElementById("adresseTirJ1");
let adresseTir2 = document.getElementById("adresseTirJ2");
let armePred1 = document.getElementById("armePredJ1");
let armePred2 = document.getElementById("armePredJ2");
let armePredDef1 = document.getElementById("armePredDefJ1");
let armePredDef2 = document.getElementById("armePredDefJ2");
let bararre1 = document.getElementById("bararreJ1");
let bararre2 = document.getElementById("bararreJ2");
let berserker1 = document.getElementById("berserkerJ1");
let berserker2 = document.getElementById("berserkerJ2");
let coupsPuis1 = document.getElementById("coupsPuisJ1");
let coupsPuis2 = document.getElementById("coupsPuisJ2");
let degainer1 = document.getElementById("degainerJ1");
let degainer2 = document.getElementById("degainerJ2");
let esquive1 = document.getElementById("esquiveJ1");
let esquive2 = document.getElementById("esquiveJ2");
let feinte1 = document.getElementById("feinteJ1");
let feinte2 = document.getElementById("feinteJ2");

// Joueur 1

function skill1J1() {
    if (acrobatieCombat1.checked == true) {
        HAB1.value = (parseInt(HAB1.value) + 1);
    } else if (acrobatieCombat1.checked == false) {
        HAB1.value = (parseInt(HAB1.value) - 1);
    }
}

function skill3J1() {
    if (armePred1.checked == true) {
        ATT1.value = (parseInt(ATT1.value) + 1);
    } else if (armePred1.checked == false) {
        ATT1.value = (parseInt(ATT1.value) - 1);
    }
}

function skill4J1() {
    if (armePredDef1.checked == true) {
        PAR1.value = (parseInt(PAR1.value) + 1);
    } else if (armePredDef1.checked == false) {
        PAR1.value = (parseInt(PAR1.value) - 1);
    }
}

function skill5J1() {
    if (feinte1.checked == true) {
        HAB2.value = (parseInt(HAB2.value) - 1);
        PAR2.value = (parseInt(PAR2.value) - 1);
    } else if (feinte1.checked == false) {
        HAB2.value = (parseInt(HAB2.value) + 1);
        PAR2.value = (parseInt(PAR2.value) + 1);
    }
}

// Joueur 2

function skill1J2() {
    if (acrobatieCombat2.checked == true) {
        HAB2.value = (parseInt(HAB2.value) + 1);
    } else if (acrobatieCombat2.checked == false) {
        HAB2.value = (parseInt(HAB2.value) - 1);
    }
}

function skill3J2() {
    if (armePred2.checked == true) {
        ATT2.value = (parseInt(ATT2.value) + 1);
    } else if (armePred1.checked == false) {
        ATT2.value = (parseInt(ATT2.value) - 1);
    }
}

function skill4J2() {
    if (armePredDef2.checked == true) {
        PAR2.value = (parseInt(PAR2.value) + 1);
    } else if (armePredDef2.checked == false) {
        PAR2.value = (parseInt(PAR2.value) - 1);
    }
}

function skill5J2() {
    if (feinte2.checked == true) {
        HAB1.value = (parseInt(HAB1.value) - 1);
        PAR1.value = (parseInt(PAR1.value) - 1);
    } else if (feinte2.checked == false) {
        HAB1.value = (parseInt(HAB1.value) + 1);
        PAR1.value = (parseInt(PAR1.value) + 1);
    }
}