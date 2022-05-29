function stuff() {
    gants = 3;
    mains = 0;
    cerveliere = 5;
    camail = 6;
    capuchon = 2;
    chapel = 7;
    casque = 15;
    tete = 0;
    chemise = 9;
    gambison = 6;
    broigne = 12;
    haubergeon = 11;
    plastron = 11;
    veste = 5;
    harnois = 15;
    lin = 1;
    jambieres_cuir = 4;
    jambieres_maille = 9;

    if (GantsJ1.checked == true) {
        handsJ1 = gants;
    } else {
        handsJ1 = mains;
    }

    if (CervelièreJ1.checked == true) {
        headJ1 = cerveliere;
    } else if (CamailJ1.checked == true) {
        headJ1 = camail;
    } else if (CapuchonJ1.checked == true) {
        headJ1 = capuchon;
    } else if (ChapelJ1.checked == true) {
        headJ1 = chapel;
    } else if (CasqueJ1.checked == true) {
        headJ1 = casque;
    } else {
        headJ1 = tete;
    }

    if (ChemiseJ1.checked == true) {
        torsoJ1 = chemise;
    } else if (GambisonJ1.checked == true) {
        torsoJ1 = gambison;
    } else if (BroigneJ1.checked == true) {
        torsoJ1 = broigne;
    } else if (HaubergeonJ1.checked == true) {
        torsoJ1 = haubergeon;
    } else if (PlastronJ1.checked == true) {
        torsoJ1 = plastron;
    } else if (VesteJ1.checked == true) {
        torsoJ1 = veste;
    } else if (HarnoisJ1.checked == true) {
        torsoJ1 = harnois;
    } else {
        torsoJ1 = lin;
    }

    if (Jambieres_cJ1.checked == true) {
        legsJ1 = jambieres_cuir;
    } else if (Jambieres_mJ1.checked == true) {
        legsJ1 = jambieres_maille;
    } else {
        legsJ1 = lin;
    }

    if (GantsJ2.checked == true) {
        handsJ2 = gants;
    } else {
        handsJ2 = mains;
    }

    if (CervelièreJ2.checked == true) {
        headJ2 = cerveliere;
    } else if (CamailJ2.checked == true) {
        headJ2 = camail;
    } else if (CapuchonJ2.checked == true) {
        headJ2 = capuchon;
    } else if (ChapelJ2.checked == true) {
        headJ2 = chapel;
    } else if (CasqueJ2.checked == true) {
        headJ2 = casque;
    } else {
        headJ2 = tete;
    }

    if (ChemiseJ2.checked == true) {
        torsoJ2 = chemise;
    } else if (GambisonJ2.checked == true) {
        torsoJ2 = gambison;
    } else if (BroigneJ2.checked == true) {
        torsoJ2 = broigne;
    } else if (HaubergeonJ2.checked == true) {
        torsoJ2 = haubergeon;
    } else if (PlastronJ2.checked == true) {
        torsoJ2 = plastron;
    } else if (VesteJ2.checked == true) {
        torsoJ2 = veste;
    } else if (HarnoisJ2.checked == true) {
        torsoJ2 = harnois;
    } else {
        torsoJ2 = lin;
    }

    if (Jambieres_cJ2.checked == true) {
        legsJ2 = jambieres_cuir;
    } else if (Jambieres_mJ2.checked == true) {
        legsJ2 = jambieres_maille;
    } else {
        legsJ2 = lin;
    }

}

function loc1() {
    stuff();

    let dloc1 = Math.floor(Math.random() * 20) + 1;
    let locresJ1_1 = ["la tête", headJ2];
    let locresJ1_2 = ["les bras", torsoJ2];
    let locresJ1_3 = ["les jambes", legsJ2];
    let locresJ1_4 = ["le torse", torsoJ2];

    resultLoc1 = "Jet de localisation : " + dloc1 + "<br>";

    if (dloc1 <= 2) {
        locresJ1 = locresJ1_1[0];
        locprotJ1 = locresJ1_1[1];
    } else if (dloc1 > 2 && dloc1 <= 7) {
        locresJ1 = locresJ1_2[0];
        locprotJ1 = locresJ1_2[1];
    } else if (dloc1 > 7 && dloc1 <= 11) {
        locresJ1 = locresJ1_3[0];
        locprotJ1 = locresJ1_3[1];
    } else if (dloc1 > 11) {
        locresJ1 = locresJ1_4[0];
        locprotJ1 = locresJ1_4[1];
    }
}

function loc2() {
    stuff();

    let dloc2 = Math.floor(Math.random() * 20) + 1;
    let locresJ2_1 = ["la tête", headJ1];
    let locresJ2_2 = ["les bras", torsoJ1];
    let locresJ2_3 = ["les jambes", legsJ1];
    let locresJ2_4 = ["le torse", torsoJ1];

    resultLoc2 = "Jet de localisation : " + dloc2 + "<br>";

    if (dloc2 <= 2) {
        locresJ2 = locresJ2_1[0];
        locprotJ2 = locresJ2_1[1];
    } else if (dloc2 > 2 && dloc2 <= 7) {
        locresJ2 = locresJ2_2[0];
        locprotJ2 = locresJ2_2[1];
    } else if (dloc2 > 7 && dloc2 <= 11) {
        locresJ2 = locresJ2_3[0];
        locprotJ2 = locresJ2_3[1];
    } else if (dloc2 > 11) {
        locresJ2 = locresJ2_4[0];
        locprotJ2 = locresJ2_4[1];
    }
}