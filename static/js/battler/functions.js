window.onload = save();

let skillToggle1 = true;
let skillToggle2 = true;
let weaponToggle1 = true;
let weaponToggle2 = true;
let stuffToggle1 = true;
let stuffToggle2 = true;

function display2() {

    var checkBox = document.getElementById("c2");

    if (checkBox.checked == true) {
        $('#player2').css('display', 'block');
        $('#result').css('top', '305px');
    } else {
        $('#player2').css('display', 'none');
        $('#result').css('top', '220px');
    }
}

function toggle1() {
    if (skillToggle1) {
        skillToggle1 = false;
        $('#skilllistJ1').css('visibility', 'visible');

    } else {
        skillToggle1 = true;
        $('#skilllistJ1').css('visibility', 'hidden');
    }
}

function toggle2() {
    if (stuffToggle1) {
        stuffToggle1 = false;
        $('#stufflistJ1').css('visibility', 'visible');

    } else {
        stuffToggle1 = true;
        $('#stufflistJ1').css('visibility', 'hidden');
    }
}

function toggle3() {
    if (weaponToggle1) {
        weaponToggle1 = false;
        $('#weaponlistJ1').css('visibility', 'visible');

    } else {
        weaponToggle1 = true;
        $('#weaponlistJ1').css('visibility', 'hidden');
    }
}

function toggle4() {
    if (skillToggle2) {
        skillToggle2 = false;
        $('#skilllistJ2').css('visibility', 'visible');

    } else {
        skillToggle2 = true;
        $('#skilllistJ2').css('visibility', 'hidden');
    }
}

function toggle5() {
    if (stuffToggle2) {
        stuffToggle2 = false;
        $('#stufflistJ2').css('visibility', 'visible');

    } else {
        stuffToggle2 = true;
        $('#stufflistJ2').css('visibility', 'hidden');
    }
}

function toggle6() {
    if (weaponToggle2) {
        weaponToggle2 = false;
        $('#weaponlistJ2').css('visibility', 'visible');

    } else {
        weaponToggle2 = true;
        $('#weaponlistJ2').css('visibility', 'hidden');
    }
}

function shutdown1() {
    skillToggle1 = true;
    stuffToggle1 = true;
    $('#skilllistJ1').css('visibility', 'hidden');
    $('#skilllistJ2').css('visibility', 'hidden');
    $('#stufflistJ1').css('visibility', 'hidden');
    $('#stufflistJ2').css('visibility', 'hidden');
    //$('#weaponlistJ1').css('visibility', 'hidden');
    $('#weaponlistJ2').css('visibility', 'hidden');
}

function shutdown2() {
    stuffToggle1 = true;
    weaponToggle1 = true;
    //$('#skilllistJ1').css('visibility', 'hidden');
    $('#skilllistJ2').css('visibility', 'hidden');
    $('#stufflistJ1').css('visibility', 'hidden');
    $('#stufflistJ2').css('visibility', 'hidden');
    $('#weaponlistJ1').css('visibility', 'hidden');
    $('#weaponlistJ2').css('visibility', 'hidden');
}

function shutdown3() {
    weaponToggle1 = true;
    skillToggle1 = true;
    $('#skilllistJ1').css('visibility', 'hidden');
    $('#skilllistJ2').css('visibility', 'hidden');
    //$('#stufflistJ1').css('visibility', 'hidden');
    $('#stufflistJ2').css('visibility', 'hidden');
    $('#weaponlistJ1').css('visibility', 'hidden');
    $('#weaponlistJ2').css('visibility', 'hidden');
}

function shutdown4() {
    skillToggle2 = true;
    stuffToggle2 = true;
    $('#skilllistJ1').css('visibility', 'hidden');
    $('#skilllistJ2').css('visibility', 'hidden');
    $('#stufflistJ1').css('visibility', 'hidden');
    $('#stufflistJ2').css('visibility', 'hidden');
    $('#weaponlistJ1').css('visibility', 'hidden');
    //$('#weaponlistJ2').css('visibility', 'hidden');
}

function shutdown5() {
    stuffToggle2 = true;
    weaponToggle2 = true;
    $('#skilllistJ1').css('visibility', 'hidden');
    //$('#skilllistJ2').css('visibility', 'hidden');
    $('#stufflistJ1').css('visibility', 'hidden');
    $('#stufflistJ2').css('visibility', 'hidden');
    $('#weaponlistJ1').css('visibility', 'hidden');
    $('#weaponlistJ2').css('visibility', 'hidden');
}

function shutdown6() {
    weaponToggle2 = true;
    skillToggle2 = true;
    $('#skilllistJ1').css('visibility', 'hidden');
    $('#skilllistJ2').css('visibility', 'hidden');
    $('#stufflistJ1').css('visibility', 'hidden');
    //$('#stufflistJ2').css('visibility', 'hidden');
    $('#weaponlistJ1').css('visibility', 'hidden');
    $('#weaponlistJ2').css('visibility', 'hidden');
}

function classesJ1() {
    let Name1 = name1.value;
    let Classe1 = document.getElementById("classeJ1").value;

    if (Classe1 == "Noblesse") {
        cName1 = Name1.fontcolor("#315CDE").fontsize(2.5).bold();
        name1.value = "Joueur 1";

    } else if (Classe1 == "Clergé") {
        cName1 = Name1.fontcolor("#8AA1D1").fontsize(2.5).bold();
        name1.value = "Joueur 1";

    } else if (Classe1 == "Milice") {
        cName1 = Name1.fontcolor("#578251").fontsize(2.5).bold();
        name1.value = "Joueur 1";

    } else if (Classe1 == "Peuple") {
        cName1 = Name1.fontcolor("#D1963E").fontsize(2.5).bold();
        name1.value = "Joueur 1";

    } else if (Classe1 == "Bannis") {
        cName1 = Name1.fontcolor("#A60F0F").fontsize(2.5).bold();
        name1.value = "Joueur 1";

    } else if (Classe1 == "Pnj") {
        cName1 = Name1.fontcolor("#7C2699").fontsize(2.5).bold();
        name1.value = "Joueur 1";

    } else if (Classe1 == "Fangeux") {
        cName1 = Name1.fontcolor("#ffffcc").fontsize(2.5).bold();
        name1.value = "Le fangeux";
    }

}

function classesJ2() {

    let Name2 = name2.value;
    let Classe2 = document.getElementById("classeJ2").value;

    if (Classe2 == "Noblesse") {
        cName2 = Name2.fontcolor("#315CDE").fontsize(2.5).bold();
        name2.value = "Joueur 2";

    } else if (Classe2 == "Clergé") {
        cName2 = Name2.fontcolor("#8AA1D1").fontsize(2.5).bold();
        name2.value = "Joueur 2";

    } else if (Classe2 == "Milice") {
        cName2 = Name2.fontcolor("#578251").fontsize(2.5).bold();
        name2.value = "Joueur 2";

    } else if (Classe2 == "Peuple") {
        cName2 = Name2.fontcolor("#D1963E").fontsize(2.5).bold();
        name2.value = "Joueur 2";

    } else if (Classe2 == "Bannis") {
        cName2 = Name2.fontcolor("#A60F0F").fontsize(2.5).bold();
        name2.value = "Joueur 2";

    } else if (Classe2 == "Pnj") {
        cName2 = Name2.fontcolor("#7C2699").fontsize(2.5).bold();
        name2.value = "Joueur 2";

    } else if (Classe2 == "Fangeux") {
        cName2 = Name2.fontcolor("#ffffcc").fontsize(2.5).bold();
        name2.value = "Le fangeux";
    }
}

function classes2() {
    let Classe1 = document.getElementById("classeJ1").value;
    let Classe2 = document.getElementById("classeJ2").value;

    function basic1() {
        FOR1.value = 8;
        END1.value = 8;
        HAB1.value = 8;
        CHAR1.value = 8;
        INT1.value = 8;
        INI1.value = 8;
        ATT1.value = 8;
        PAR1.value = 8;
        TIR1.value = 8;
        NA1.value = 2;
        PV1.value = 60;
    }

    function basic2() {
        FOR2.value = 8;
        END2.value = 8;
        HAB2.value = 8;
        CHAR2.value = 8;
        INT2.value = 8;
        INI2.value = 8;
        ATT2.value = 8;
        PAR2.value = 8;
        TIR2.value = 8;
        NA2.value = 2;
        PV2.value = 60;
    }

    function fangeux1() {
        FOR1.value = 13;
        END1.value = 13;
        HAB1.value = 14;
        CHAR1.value = 2;
        INT1.value = 3;
        INI1.value = 15;
        ATT1.value = 14;
        PAR1.value = 5;
        TIR1.value = 5
        NA1.value = 2;
        PV1.value = 100;
    }

    function fangeux2() {
        FOR2.value = 13;
        END2.value = 13;
        HAB2.value = 14;
        CHAR2.value = 2;
        INT2.value = 3;
        INI2.value = 15;
        ATT2.value = 14;
        PAR2.value = 5;
        TIR2.value = 5
        NA2.value = 2;
        PV2.value = 100;
    }

    if (Classe1 == "Noblesse") {
        basic1();
        document.getElementById("EsquiveJ1").checked = false;

    } else if (Classe1 == "Clergé") {
        basic1();
        document.getElementById("EsquiveJ1").checked = false;

    } else if (Classe1 == "Milice") {
        basic1();
        document.getElementById("EsquiveJ1").checked = true;

    } else if (Classe1 == "Peuple") {
        basic1();
        document.getElementById("EsquiveJ1").checked = false;

    } else if (Classe1 == "Bannis") {
        basic1();
        document.getElementById("EsquiveJ1").checked = false;

    } else if (Classe1 == "Pnj") {
        basic1();
        document.getElementById("EsquiveJ1").checked = false;

    } else if (Classe1 == "Fangeux") {
        fangeux1();
        document.getElementById("EsquiveJ1").checked = false;
    }

    if (Classe2 == "Noblesse") {
        basic2();
        document.getElementById("EsquiveJ2").checked = false;

    } else if (Classe2 == "Clergé") {
        basic2();
        document.getElementById("EsquiveJ2").checked = false;

    } else if (Classe2 == "Milice") {
        basic2();
        document.getElementById("EsquiveJ2").checked = true;

    } else if (Classe2 == "Peuple") {
        basic2();
        document.getElementById("EsquiveJ2").checked = false;

    } else if (Classe2 == "Bannis") {
        basic2();
        document.getElementById("EsquiveJ2").checked = false;

    } else if (Classe2 == "Pnj") {
        basic2();
        document.getElementById("EsquiveJ2").checked = false;

    } else if (Classe2 == "Fangeux") {
        fangeux2();
        document.getElementById("EsquiveJ2").checked = false;
    }

}

function save() {

    $('#checkJ1').css('display', 'block');
    $('#checkJ2').css('display', 'block');

    let iniFOR1 = document.getElementById('FOR1').value;
    let iniEND1 = document.getElementById('END1').value;
    let iniHAB1 = document.getElementById('HAB1').value;
    let iniCHAR1 = document.getElementById('CHAR1').value;
    let iniINT1 = document.getElementById('INT1').value;
    let iniINI1 = document.getElementById('INI1').value;
    let iniATT1 = document.getElementById('ATT1').value;
    let iniPAR1 = document.getElementById('PAR1').value;
    let iniTIR1 = document.getElementById('TIR1').value;
    let iniNA1 = document.getElementById('NA1').value;
    let iniPV1 = document.getElementById('PV1').value;

    let iniFOR2 = document.getElementById('FOR2').value;
    let iniEND2 = document.getElementById('END2').value;
    let iniHAB2 = document.getElementById('HAB2').value;
    let iniCHAR2 = document.getElementById('CHAR2').value;
    let iniINT2 = document.getElementById('INT2').value;
    let iniINI2 = document.getElementById('INI2').value;
    let iniATT2 = document.getElementById('ATT2').value;
    let iniPAR2 = document.getElementById('PAR2').value;
    let iniTIR2 = document.getElementById('TIR2').value;
    let iniNA2 = document.getElementById('NA2').value;
    let iniPV2 = document.getElementById('PV2').value;

    /* console.log("Stats stored");
    console.log(
        "For Joueur 1: ", FOR1.value, '\n',
        "End Joueur 1: ", END1.value, '\n',
        "Hab Joueur 1: ", HAB1.value, '\n',
        "Char Joueur 1: ", CHAR1.value, '\n',
        "Int Joueur 1: ", INT1.value, '\n',
        "Ini Joueur 1: ", INI1.value, '\n',
        "Att Joueur 1: ", ATT1.value, '\n',
        "Par Joueur 1: ", PAR1.value, '\n',
        "Tir Joueur 1: ", TIR1.value, '\n',
        "Na Joueur 1: ", NA1.value, '\n',
        "Pv Joueur 1: ", PV1.value, '\n', '\n',

        "For Joueur 2: ", FOR2.value, '\n',
        "End Joueur 2: ", END2.value, '\n',
        "Hab Joueur 2: ", HAB2.value, '\n',
        "Char Joueur 2: ", CHAR2.value, '\n',
        "Int Joueur 2: ", INT2.value, '\n',
        "Ini Joueur 2: ", INI2.value, '\n',
        "Att Joueur 2: ", ATT2.value, '\n',
        "Par Joueur 2: ", PAR2.value, '\n',
        "Tir Joueur 2: ", TIR2.value, '\n',
        "Na Joueur 2: ", NA2.value, '\n',
        "Pv Joueur 2: ", PV2.value, '\n'); */

    $('.reload').on('click', function () {
        document.getElementById("resultContent").innerHTML = "";
        document.getElementById("result2Content").innerHTML = "";
        $('h5').css('visibility', 'hidden');
        $('#result4').empty();

        console.log("Stats restored");

        FOR1.value = iniFOR1;
        END1.value = iniEND1;
        HAB1.value = iniHAB1;
        CHAR1.value = iniCHAR1;
        INT1.value = iniINT1;
        INI1.value = iniINI1;
        ATT1.value = iniATT1;
        PAR1.value = iniPAR1;
        TIR1.value = iniTIR1;
        NA1.value = iniNA1;
        PV1.value = iniPV1;

        FOR2.value = iniFOR2;
        END2.value = iniEND2;
        HAB2.value = iniHAB2;
        CHAR2.value = iniCHAR2;
        INT2.value = iniINT2;
        INI2.value = iniINI2;
        ATT2.value = iniATT2;
        PAR2.value = iniPAR2;
        TIR2.value = iniTIR2;
        NA2.value = iniNA2;
        PV2.value = iniPV2;
    });
}

function id() {
    //$( ".id" ).append("ID " + idGen);
    let idResult = "ID " + idGen;
    console.log(idResult);
}

$('.save').click(function () {
    if (battleStart == true) {
        var blob = new Blob([document.getElementById("resultContent").innerText + document.getElementById("result2Content").innerText], {
            type: "text/html;charset=utf-8"
        });
        saveAs(blob, "Combat N°" + idGen + ".txt");
    } else {
        swal("", "◈ Lancez d'abord le combat! ◈", "warning", {
            closeOnClickOutside: true,
            buttons: false,
            timer: 2000
        });
        return false;
    }
});

function rolld4() {

    var dicenum = swal("◈ 1D4 ◈", "", {

        closeOnClickOutside: true,
        closeOnEsc: true,

        content: {
            element: "input",
            attributes: {
                placeholder: "Entrez le nombre de lancers",
                type: "input",
            },
        },
        buttons: {
            confirm: "Ok",
            cancel: {
                text: "X",
                value: null,
                visible: true,
                className: "",
                closeModal: true,
            },
            roll1: {
                text: "1",
                value: "1",
            },
            roll2: {
                text: "2",
                value: "2",
            }
        }

    }).then((value) => {
        console.log(value);
        if (value == "" || value == null) {
            document.getElementById("result4").innerHTML = "";
            $('h5').css('visibility', 'hidden');
            return false;
        } else {

            document.getElementById("result4").innerHTML = "";

            $('h5').css('visibility', 'visible');

            var diceint = Math.round(value);
            var diceroll, results = '';
            for (i = 1; i <= diceint; i++) {
                diceroll = Math.floor(Math.random() * 4) + 1;
                results += diceroll + '&nbsp;' + '&nbsp;';
            }
            Cresults = "Résultat D4 : ".bold();
            $("#result4").append(Cresults + results).hide().slideDown();
        }
    });
}

function rolld6() {

    var dicenum = swal("◈ 1D6 ◈", "", {

        closeOnClickOutside: true,
        closeOnEsc: true,

        content: {
            element: "input",
            attributes: {
                placeholder: "Entrez le nombre de lancers",
                type: "input",
            },
        },
        buttons: {
            confirm: "Ok",
            cancel: {
                text: "X",
                value: null,
                visible: true,
                className: "",
                closeModal: true,
            },
            roll1: {
                text: "1",
                value: "1",
            },
            roll2: {
                text: "2",
                value: "2",
            }
        }

    }).then((value) => {

        if (value === "" || value == null) {
            document.getElementById("result4").innerHTML = "";
            $('h5').css('visibility', 'hidden');
            return false;
        } else {

            document.getElementById("result4").innerHTML = "";

            $('h5').css('visibility', 'visible');

            var diceint = Math.round(value);
            var diceroll, results = '';
            for (i = 1; i <= diceint; i++) {
                diceroll = Math.floor(Math.random() * 6) + 1;
                results += diceroll + '&nbsp;' + '&nbsp;';
            }
            Cresults = "Résultat D6 : ".bold();
            $("#result4").append(Cresults + results);
        }
    });
}

function rolld8() {

    var dicenum = swal("◈ 1D8 ◈", "", {

        closeOnClickOutside: true,
        closeOnEsc: true,

        content: {
            element: "input",
            attributes: {
                placeholder: "Entrez le nombre de lancers",
                type: "input",
            },
        },
        buttons: {
            confirm: "Ok",
            cancel: {
                text: "X",
                value: null,
                visible: true,
                className: "",
                closeModal: true,
            },
            roll1: {
                text: "1",
                value: "1",
            },
            roll2: {
                text: "2",
                value: "2",
            }
        }

    }).then((value) => {

        if (value === "" || value == null) {
            document.getElementById("result4").innerHTML = "";
            $('h5').css('visibility', 'hidden');
            return false;
        } else {

            document.getElementById("result4").innerHTML = "";

            $('h5').css('visibility', 'visible');

            var diceint = Math.round(value);
            var diceroll, results = '';
            for (i = 1; i <= diceint; i++) {
                diceroll = Math.floor(Math.random() * 8) + 1;
                results += diceroll + '&nbsp;' + '&nbsp;';
            }
            Cresults = "Résultat D8 : ".bold();
            $("#result4").append(Cresults + results);
        }
    });
}

function rolld10() {

    var dicenum = swal("◈ 1D10 ◈", "", {

        closeOnClickOutside: true,
        closeOnEsc: true,

        content: {
            element: "input",
            attributes: {
                placeholder: "Entrez le nombre de lancers",
                type: "input",
            },
        },
        buttons: {
            confirm: "Ok",
            cancel: {
                text: "X",
                value: null,
                visible: true,
                className: "",
                closeModal: true,
            },
            roll1: {
                text: "1",
                value: "1",
            },
            roll2: {
                text: "2",
                value: "2",
            }
        }

    }).then((value) => {

        if (value === "" || value == null) {
            document.getElementById("result4").innerHTML = "";
            $('h5').css('visibility', 'hidden');
            return false;
        } else {

            document.getElementById("result4").innerHTML = "";

            $('h5').css('visibility', 'visible');

            var diceint = Math.round(value);
            var diceroll, results = '';
            for (i = 1; i <= diceint; i++) {
                diceroll = Math.floor(Math.random() * 10) + 1;
                results += diceroll + '&nbsp;' + '&nbsp;';
            }
            Cresults = "Résultat D10 : ".bold();
            $("#result4").append(Cresults + results);
        }
    });
}

function rolld20() {

    var dicenum = swal("◈ 1D20 ◈", "", {

        closeOnClickOutside: true,
        closeOnEsc: true,

        content: {
            element: "input",
            attributes: {
                placeholder: "Entrez le nombre de lancers",
                type: "input",
            },
        },
        buttons: {
            confirm: "Ok",
            cancel: {
                text: "X",
                value: null,
                visible: true,
                className: "",
                closeModal: true,
            },
            roll1: {
                text: "1",
                value: "1",
            },
            roll2: {
                text: "2",
                value: "2",
            }
        }

    }).then((value) => {

        if (value === "" || value == null) {
            document.getElementById("result4").innerHTML = "";
            $('h5').css('visibility', 'hidden');
            return false;
        } else {

            document.getElementById("result4").innerHTML = "";

            $('h5').css('visibility', 'visible');

            var diceint = Math.round(value);
            var diceroll, results = '';
            for (i = 1; i <= diceint; i++) {
                diceroll = Math.floor(Math.random() * 20) + 1;
                results += diceroll + '&nbsp;' + '&nbsp;';
            }
            Cresults = "Résultat D20 : ".bold();
            $("#result4").append(Cresults + results);
        }
    });
}

function rolld100() {

    var dicenum = swal("◈ 1D100 ◈", "", {

        closeOnClickOutside: true,
        closeOnEsc: true,

        content: {
            element: "input",
            attributes: {
                placeholder: "Entrez le nombre de lancers",
                type: "input",
            },
        },
        buttons: {
            confirm: "Ok",
            cancel: {
                text: "X",
                value: null,
                visible: true,
                className: "",
                closeModal: true,
            },
            roll1: {
                text: "1",
                value: "1",
            },
            roll2: {
                text: "2",
                value: "2",
            }
        }

    }).then((value) => {

        if (value === "" || value == null) {
            document.getElementById("result4").innerHTML = "";
            $('h5').css('visibility', 'hidden');
            return false;
        } else {

            document.getElementById("result4").innerHTML = "";

            $('h5').css('visibility', 'visible');

            var diceint = Math.round(value);
            var diceroll, results = '';
            for (i = 1; i <= diceint; i++) {
                diceroll = Math.floor(Math.random() * 100) + 1;
                results += diceroll + '&nbsp;' + '&nbsp;';
            }
            Cresults = "Résultat D100 : ".bold();
            $("#result4").append(Cresults + results);
        }
    });
}