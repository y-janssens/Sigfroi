let idGen = Math.floor(Math.random() * 3000000000000000000) + 1;
let battleStart = false;

function fight() {
    battleStart = true;
    console.clear();
    let number = 0;

    let iniNA1 = document.getElementById('NA1').value;
    let iniNA2 = document.getElementById('NA2').value;

    let iniINI1 = document.getElementById('INI1').value;
    let iniINI2 = document.getElementById('INI2').value;

    classesJ1();
    classesJ2();
    save();
    console.time('time');

    document.getElementById("resultContent").innerHTML = "";
    document.getElementById("result2Content").innerHTML = "";

    function start() {
        $("#resultContent").append("<h2>Début du combat</h2>" + "<h2>◈</h2>").hide().slideDown(100);
        newRound();
        ini();
        id();
    }

    function newRound() {
        number = number + 1;
        $("#resultContent").append("<h3> Tour " + number + "</h3>" + "<br>").hide().slideDown(3000);
    }

    function ini() {

        let dini = Math.floor(Math.random() * 20) + 1;

        let resultini = "Jet d'initiative : " + dini + "<br>";

        if ((number == 1 & degainerJ1.checked == true)) {
            INI1.value = (parseInt(iniINI1) + 1);
        } else if (number >= 2) {
            INI1.value = (parseInt(iniINI1));
        }

        if ((number == 1 & degainerJ2.checked == true)) {
            INI2.value = (parseInt(iniINI2) + 1);
        } else if (number >= 2) {
            INI2.value = (parseInt(iniINI2));
        }

        if (parseInt(INI1.value) === parseInt(INI2.value)) {

            $("#resultContent").append(cName1 + " et " + cName2 + " ont le même score d'INI : " + INI1.value + "<br>" +
                resultini).slideDown(3000);

            if (dini < 10) {
                if (parseInt(PV1.value) <= 0 || parseInt(PV2.value) <= 0) {
                    return false;
                }
                $("#resultContent").append(cName1 + " a l'initiative" + "<br>" + "<br>").slideDown(3000);
                att1();
            } else if (dini >= 10) {
                if (parseInt(PV1.value) <= 0 || parseInt(PV2.value) <= 0) {
                    return false;
                }
                $("#resultContent").append(cName2 + " a l'initiative" + "<br>" + "<br>").slideDown(3000);
                att2();
            }
        }

        if (parseInt(INI1.value) >= parseInt(INI2.value)) {
            if (parseInt(PV1.value) <= 0 || parseInt(PV2.value) <= 0) {
                return false;
            }
            $("#resultContent").append(cName1 + " a l'initiative: " + "INI " + INI1.value + "<br>" + "<br>").slideDown(3000);
            att1();

        } else if (parseInt(INI1.value) < parseInt(INI2.value)) {
            if (parseInt(PV1.value) <= 0 || parseInt(PV2.value) <= 0) {
                return false;
            }
            $("#resultContent").append(cName2 + " a l'initiative: " + "INI " + INI2.value + "<br>" + "<br>").slideDown(3000);
            att2();
        }
    }

    function att1() {
        loc1();
        loc2();
        damage();

        let d1 = Math.floor(Math.random() * 20) + 1;
        let d2 = Math.floor(Math.random() * 20) + 1;
        let d3 = Math.floor(Math.random() * 20) + 1;
        let d9 = (((FOR1.value * 2) + dmgJ1) - END2.value - locprotJ2 - parJ2); // Formule dégats avec parade réussie
        let d10 = (((FOR1.value * 2) + dmgJ1) - END2.value - locprotJ2); // Formule dégats avec parade/esquive ratée

        let sucess1 = d1 + " réussi";
        let rSucess1 = sucess1.fontcolor("green");

        let failure1 = d1 + " échec";
        let rFailure1 = failure1.fontcolor("red");

        let sucess2 = d2 + " réussi";
        let rSucess2 = sucess2.fontcolor("green");

        let failure2 = d2 + " échec";
        let rFailure2 = failure2.fontcolor("red");

        let sucess3 = d3 + " réussi";
        let rSucess3 = sucess3.fontcolor("green");

        let failure3 = d3 + " échec";
        let rFailure3 = failure3.fontcolor("red");

        if (d1 < ATT1.value) {
            resultr1 = rSucess1;
        } else {
            resultr1 = rFailure1;
        }

        if (d2 < PAR2.value) {
            resultr2 = rSucess2;
        } else {
            resultr2 = rFailure2;
        }

        if (d3 < HAB2.value) {
            resultr3 = rSucess3;
        } else {
            resultr3 = rFailure3;
        }

        if (parseInt(PV1.value) <= 0) {
            return;
        }
        if (parseInt(PV2.value) <= 0) {
            return;
        }
        $("#resultContent").append(cName1 + " tente d'attaquer: " + "ATT " + ATT1.value + " (NA restants : " + (NA1.value = ((NA1.value) - 1)) + ")" + "<br>" + resultr1 + "<br>").slideDown(3000);

        if (d1 < ATT1.value) {
            $("#resultContent").append(resultLoc1 + cName1 + " vise : " + locresJ1 + "<br>").slideDown(3000);
            if (EsquiveJ2.checked == true) {
                $("#resultContent").append(cName2 + " tente d'esquiver: " + "HAB " + HAB2.value + " (NA restants : " + (NA2.value = ((NA2.value) - 0.5)) + ")" + "<br>" + resultr3 + "<br>").slideDown(3000);

                if (d3 < HAB2.value) { // esquive réussie
                    void (0);
                } else { // esquive ratée
                    $("#resultContent").append(cName2 + " perd " + d10 + " Pvs." + "<br>" +
                        " Pvs restants : " + (PV2.value = ((PV2.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                }

            } else if (EsquiveJ2.checked == false) {
                $("#resultContent").append(cName2 + " tente de parer: " + "PAR " + PAR2.value + " (NA restants : " + (NA2.value = ((NA2.value) - 0.5)) + ")" + "<br>" + resultr2 + "<br>").slideDown(3000);

                if (d2 < PAR2.value) { // parade réussie
                    $("#resultContent").append(cName2 + " perd " + d9 + " Pvs." + "<br>" +
                        " Pvs restants : " + (PV2.value = ((PV2.value) - d9)) + "<br>" + "<br>").slideDown(3000);

                } else { // parade ratée
                    $("#resultContent").append(cName2 + " perd " + d10 + " Pvs." + "<br>" +
                        " Pvs restants : " + (PV2.value = ((PV2.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                }
            }
            rounds();
            att2();
        } else {
            rounds();
            att2();
        }
    }

    function att2() {
        loc1();
        loc2();
        damage();

        let d1 = Math.floor(Math.random() * 20) + 1;
        let d2 = Math.floor(Math.random() * 20) + 1;
        let d3 = Math.floor(Math.random() * 20) + 1;
        let d9 = (((FOR2.value * 2) + dmgJ2) - END1.value - locprotJ1 - parJ1); // Formule dégats avec parade réussie
        let d10 = (((FOR2.value * 2) + dmgJ2) - END1.value - locprotJ1); // Formule dégats avec parade/esquive ratée

        let sucess1 = d1 + " réussi";
        let rSucess1 = sucess1.fontcolor("green");

        let failure1 = d1 + " échec";
        let rFailure1 = failure1.fontcolor("red");

        let sucess2 = d2 + " réussi";
        let rSucess2 = sucess2.fontcolor("green");

        let failure2 = d2 + " échec";
        let rFailure2 = failure2.fontcolor("red");

        let sucess3 = d3 + " réussi";
        let rSucess3 = sucess3.fontcolor("green");

        let failure3 = d3 + " échec";
        let rFailure3 = failure3.fontcolor("red");

        if (d1 < ATT1.value) {
            resultr1 = rSucess1;
        } else {
            resultr1 = rFailure1;
        }

        if (d2 < PAR2.value) {
            resultr2 = rSucess2;
        } else {
            resultr2 = rFailure2;
        }

        if (d3 < HAB2.value) {
            resultr3 = rSucess3;
        } else {
            resultr3 = rFailure3;
        }

        if (parseInt(PV1.value) <= 0) {
            return;
        }
        if (parseInt(PV2.value) <= 0) {
            return;
        }
        $("#resultContent").append(cName2 + " tente d'attaquer: " + "ATT " + ATT2.value + " (NA restants : " + (NA2.value = ((NA2.value) - 1)) + ")" + "<br>" + resultr1 + "<br>").slideDown(3000);

        if (d1 < ATT2.value) {
            $("#resultContent").append(resultLoc2 + cName2 + " vise : " + locresJ2 + "<br>").slideDown(3000);
            if (EsquiveJ1.checked == true) {
                $("#resultContent").append(cName1 + " tente d'esquiver: " + "HAB " + HAB1.value + " (NA restants : " + (NA1.value = ((NA1.value) - 0.5)) + ")" + "<br>" + resultr3 + "<br>").slideDown(3000);

                if (d3 < HAB1.value) { // esquive réussie
                    void (0);
                } else { // esquive ratée
                    $("#resultContent").append(cName1 + " perd " + d10 + " Pvs." + "<br>" +
                        " Pvs restants : " + (PV1.value = ((PV1.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                }

            } else if (EsquiveJ1.checked == false) {
                $("#resultContent").append(cName1 + " tente de parer: " + "PAR " + PAR1.value + " (NA restants : " + (NA1.value = ((NA1.value) - 0.5)) + ")" + "<br>" + resultr2 + "<br>").slideDown(3000);

                if (d2 < PAR1.value) { // parade réussie
                    $("#resultContent").append(cName1 + " perd " + d9 + " Pvs." + "<br>" +
                        " Pvs restants : " + (PV1.value = ((PV1.value) - d9)) + "<br>" + "<br>").slideDown(3000);

                } else { // parade ratée
                    $("#resultContent").append(cName1 + " perd " + d10 + " Pvs." + "<br>" +
                        " Pvs restants : " + (PV1.value = ((PV1.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                }
            }
            rounds();
            att1();
        } else {
            rounds();
            att1();
        }
    }

    function rounds() {

        if ((parseInt(NA1.value) <= 0) & (parseInt(NA2.value) <= 0)) {
            $("#resultContent").append("<h3>Fin du tour</h3>" + "<h3>◈</h3>").slideDown(3000);
            NA1.value = iniNA1;
            NA2.value = iniNA2;
            newRound();
            ini();
        }
    }

    function last1() {
        let d1 = Math.floor(Math.random() * 20) + 1;
        let d2 = Math.floor(Math.random() * 20) + 1;
        let d3 = Math.floor(Math.random() * 20) + 1;
        let berserker1 = document.getElementById("berserkerJ1");

        if ((berserker1.checked == true) & (parseInt(PV1.value) <= 0)) {
            $("#resultContent").append(cName1 + " tente d'attaquer une dernière fois: " + "ATT " + ATT1.value + " (NA restants : " + (NA1.value = ((NA1.value) - 1)) + ")" + "<br>" + resultr1 + "<br>").slideDown(3000);
            if (d1 < ATT1.value) {
                $("#resultContent").append(resultLoc1 + cName1 + " vise : " + locresJ1 + "<br>").slideDown(3000);
                if (EsquiveJ2.checked == true) {
                    $("#resultContent").append(cName2 + " tente d'esquiver: " + "HAB " + HAB2.value + " (NA restants : " + (NA2.value = ((NA2.value) - 0.5)) + ")" + "<br>" + resultr3 + "<br>").slideDown(3000);

                    if (d3 < HAB2.value) { // esquive réussie
                        void (0);
                    } else { // esquive ratée
                        $("#resultContent").append(cName2 + " perd " + d10 + " Pvs." + "<br>" +
                            " Pvs restants : " + (PV2.value = ((PV2.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                    }

                } else if (EsquiveJ2.checked == false) {
                    $("#resultContent").append(cName2 + " tente de parer: " + "PAR " + PAR2.value + " (NA restants : " + (NA2.value = ((NA2.value) - 0.5)) + ")" + "<br>" + resultr2 + "<br>").slideDown(3000);

                    if (d2 < PAR2.value) { // parade réussie
                        $("#resultContent").append(cName2 + " perd " + d9 + " Pvs." + "<br>" +
                            " Pvs restants : " + (PV2.value = ((PV2.value) - d9)) + "<br>" + "<br>").slideDown(3000);

                    } else { // parade ratée
                        $("#resultContent").append(cName2 + " perd " + d10 + " Pvs." + "<br>" +
                            " Pvs restants : " + (PV2.value = ((PV2.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                    }
                }
            } else {
                return;
            }
        }
    }

    function last2() {
        let d1 = Math.floor(Math.random() * 20) + 1;
        let d2 = Math.floor(Math.random() * 20) + 1;
        let d3 = Math.floor(Math.random() * 20) + 1;
        let berserker2 = document.getElementById("berserkerJ2");

        if ((berserker2.checked == true) & (parseInt(PV2.value) <= 0)) {
            $("#resultContent").append(cName2 + " tente d'attaquer une dernière fois: " + "ATT " + ATT2.value + " (NA restants : " + (NA2.value = ((NA2.value) - 1)) + ")" + "<br>" + resultr3 + "<br>").slideDown(3000);
            if (d1 < ATT2.value) {
                $("#resultContent").append(resultLoc2 + cName2 + " vise : " + locresJ2 + "<br>").slideDown(3000);
                if (EsquiveJ1.checked == true) {
                    $("#resultContent").append(cName1 + " tente d'esquiver: " + "HAB " + HAB1.value + " (NA restants : " + (NA1.value = ((NA1.value) - 0.5)) + ")" + "<br>" + resultr3 + "<br>").slideDown(3000);

                    if (d3 < HAB1.value) { // esquive réussie
                        void (0);
                    } else { // esquive ratée
                        $("#resultContent").append(cName1 + " perd " + d10 + " Pvs." + "<br>" +
                            " Pvs restants : " + (PV1.value = ((PV1.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                    }

                } else if (EsquiveJ1.checked == false) {
                    $("#resultContent").append(cName1 + " tente de parer: " + "PAR " + PAR1.value + " (NA restants : " + (NA1.value = ((NA1.value) - 0.5)) + ")" + "<br>" + resultr2 + "<br>").slideDown(3000);

                    if (d2 < PAR1.value) { // parade réussie
                        $("#resultContent").append(cName1 + " perd " + d9 + " Pvs." + "<br>" +
                            " Pvs restants : " + (PV1.value = ((PV1.value) - d9)) + "<br>" + "<br>").slideDown(3000);

                    } else { // parade ratée
                        $("#resultContent").append(cName1 + " perd " + d10 + " Pvs." + "<br>" +
                            " Pvs restants : " + (PV1.value = ((PV1.value) - d10)) + "<br>" + "<br>").slideDown(3000);
                    }
                }
            } else {
                return;
            }
        }
    }

    start();
    last1();
    last2();
    outcome();
    console.timeEnd('time');
}

function check() {
    if (parseInt(PV1.value) <= 0 || parseInt(PV2.value) <= 0) {
        return false;
    }
}

function outcome() {
    if (parseInt(PV1.value) <= 0) {
        $("#resultContent").append("<h2>◈ Fin du combat ◈</h2>" + "<br>").slideDown(3000);
        $("#result2Content").append(cName1 + " n'a plus de Pvs." + "<br>" +
            cName1 + " est K-O." + "<br>" +
            cName2 + " remporte la victoire!").hide().delay(2500).slideDown(500);
        return;
    } else if (parseInt(PV2.value) <= 0) {
        $("#resultContent").append("<h2>◈ Fin du combat ◈<h2>" + "<br>").slideDown(3000);
        $("#result2Content").append(cName2 + " n'a plus de Pvs." + "<br>" +
            cName2 + " est K-O." + "<br>" +
            cName1 + " remporte la victoire!").hide().delay(2500).slideDown(500);
        return;
    }
}