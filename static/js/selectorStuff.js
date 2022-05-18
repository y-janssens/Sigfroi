let stuffToggle = false;
let stuffCount = 0;
let weapons = {};
let armors = {};
let stuffs = [];

axios.get(`${window.location.origin}/api/equipement/armes/`).then(function (response) {
  Object.assign(weapons, response.data);
  axios.get(`${window.location.origin}/api/equipement/armures/`).then(function (response) {
    Object.assign(armors, response.data);
    handleResponse();
  });
});

const handleResponse = () => {
  Object.assign(stuffs, weapons, armors);
  document.getElementById("stuffs-list").innerHTML = "";
  for (let i = 0; i < stuffs.length; i++) {
    document.getElementById(
      "stuffs-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleStuffCheck(event)" value="${stuffs[i].name}" name="skill-request" /><label for="${stuffs[i].name}" class="skill-search-content-item-label" onclick="handleStuffClick(event)">${stuffs[i].name}</label></div>`;
  }
};

function panelStuffToggle() {
  if (stuffToggle == false) {
    stuffToggle = true;
    $("#stuffs-selector-container").css("min-height", "315px");
    $("#stuffs-search-container").css("height", "235px");
    $("#stuffs-search-container").css("padding", "5px 0");
    $("#stuffs-search-container").css("border", "1px solid #938471");
    $(".stuff-search-content").css("height", "180px");
    $(".stuff-arrow").css("transform", "rotate(-90deg)");
    $(".stuffs-search-btn").css("display", "flex");
  } else {
    stuffToggle = false;
    $("#stuffs-selector-container").css("min-height", "200px");
    $("#stuffs-search-container").css("height", "0px");
    $("#stuffs-search-container").css("padding", "0");
    $("#stuffs-search-container").css("border-top", "none");
    $("#stuffs-search-container").css("border-bottom", "none");
    $(".stuff-search-content").css("height", "0px");
    $(".stuff-arrow").css("transform", "rotate(90deg)");
    $(".stuffs-search-btn").css("display", "none");
  }
}

const handleStuffClick = (event) => {
  event.target.closest("div").children[0].click();
};

const handleStuffCheck = (event) => {
  if (event.target.checked) {
    stuffCount += 1;
  } else {
    stuffCount -= 1;
  }

  document.getElementById("selector-title").innerHTML =
    stuffCount < 1
      ? "Ajouter une nouvelle compétence"
      : stuffCount == 1
      ? `${stuffCount} compétence sélectionnée`
      : `${stuffCount} compétences sélectionnées`;
};

let stuffResult = document.getElementById("stuff_search_bar_input");
stuffResult.addEventListener("keyup", () => {
  let query = stuffResult.value;
  document.getElementById("stuffs-list").innerHTML = "";
  let stuffsList = stuffs.filter(function (stuff) {
    return stuff.name.toLowerCase().includes(query?.toLowerCase());
  });

  stuffsList.map((stuff) => {
    return (document.getElementById(
      "stuffs-list"
    ).innerHTML += `<div class="stuff-search-content-item"><input type="checkbox" onchange="handleStuffCheck(event)" value="${stuff.name}" name="stuff-request" /><label for="${stuff.name}" class="stuff-search-content-item-label" onclick="handleStuffClick(event)">${stuff.name}</label></div>`);
  });
});
