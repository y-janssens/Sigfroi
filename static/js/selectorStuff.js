let stuffToggle = false;
let stuffCount = 0;
let weapons = {};
let armors = {};
let stuffs = [];
let stuffPayload = []
let stuffList = document.getElementById("stuffs-list");

axios.get(`${window.location.origin}/api/equipement/armes/`).then(function (response) {
  Object.assign(weapons, response.data);
  axios.get(`${window.location.origin}/api/equipement/armures/`).then(function (response) {
    Object.assign(armors, response.data);
    handleResponse();
  });
});

const handleStuffPayload = () => {
  for (let i in stuffPayload) {
    stuffList.innerHTML += `<input type="text" name="send-stuff" value="${stuffPayload[i]}" style="display: none" />`
  }
};

const handleResponse = () => {
  for (let i in weapons) {
    stuffs.push(weapons[i])
  }
  for (let i in armors) {
    stuffs.push(armors[i])
  }
  stuffList.innerHTML = "";
  for (let i = 0; i < stuffs.length; i++) {
    stuffList.innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleStuffCheck(event)" value="${stuffs[i].name}" name="skill-request" /><label for="${stuffs[i].name}" class="skill-search-content-item-label" onclick="handleStuffClick(event)">${stuffs[i].name}</label></div>`;
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
    stuffPayload.push(event.target.value)
  } else {
    stuffCount -= 1;
    for (let i in stuffPayload) {
      if (stuffPayload[i] == event.target.value) {
        stuffPayload.splice(i, 1);
      }
    }
  }

  document.getElementById("stuff-selector-title").innerHTML =
    stuffCount < 1
      ? "Ajouter un nouvel équipement"
      : stuffCount == 1
      ? `${stuffCount} équipement sélectionné`
      : `${stuffCount} équipements sélectionnés`;
};

let stuffResult = document.getElementById("stuff_search_bar_input");
stuffResult.addEventListener("keyup", () => {
  let query = stuffResult.value;
  stuffList.innerHTML = "";
  let stuffsList = stuffs.filter(function (stuff) {
    return stuff.name.toLowerCase().includes(query?.toLowerCase());
  });

  stuffsList.map((stuff) => {
    return (stuffList.innerHTML += `<div class="stuff-search-content-item"><input type="checkbox" onchange="handleStuffCheck(event)" value="${stuff.name}" name="stuff-request" /><label for="${stuff.name}" class="stuff-search-content-item-label" onclick="handleStuffClick(event)">${stuff.name}</label></div>`);
  });
});
