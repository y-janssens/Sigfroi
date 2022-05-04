axios.get("http://127.0.0.1:8000/api/competences/").then(function (response) {
  skills = response.data;
  document.getElementById("skills-list").innerHTML = "";
  for (let i = 0; i < skills.length; i++) {
    document.getElementById(
      "skills-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleChange(event)" name="${skills[i].name}" /><label for="${skills[i].name}">${skills[i].name}</label></div>`;
  }
});

let skillQueries = [];

const handleChange = (event) => {
  let value = event.target.name;
  if (event.target.checked && !skillQueries.includes(value)) {
    skillQueries.push(value);
  }
  }

let toggle = false;

function panelToggle() {
  if (toggle == false) {
    toggle = true;
    $("#skills-search-container").css("height", "235px");
    $("#skills-search-container").css("padding", "5px 0");
    $("#skills-search-container").css("border-top", "1px solid #938471");
    $("#skills-search-container").css("border-left", "1px solid #938471");
    $("#skills-search-container").css("border-right", "1px solid #938471");
    $("#skills-search-container").css("border-bottom", "1px solid #938471");
    $(".skill-search-content").css("height", "180px");
    $(".arrow").css("transform", "rotate(-90deg)");
    $(".skills-search-btn").css("display", "flex");
  } else {
    toggle = false;
    $("#skills-search-container").css("height", "0px");
    $("#skills-search-container").css("padding", "0");
    $("#skills-search-container").css("border-top", "none");
    $("#skills-search-container").css("border-left", "1px solid #938471");
    $("#skills-search-container").css("border-right", "1px solid #938471");
    $("#skills-search-container").css("border-bottom", "none");
    $(".skill-search-content").css("height", "0px");
    $(".arrow").css("transform", "rotate(90deg)");
    $(".skills-search-btn").css("display", "none");
  }
}

let result = document.getElementById("skill_search_bar_input");
result.addEventListener("keyup", () => {
  let query = result.value;
  document.getElementById("skills-list").innerHTML = "";
  let skillsList = skills.filter(function (skill) {
    return skill.name.toLowerCase().includes(query?.toLowerCase());
  });

  skillsList.map((skill) => {
    return (document.getElementById(
      "skills-list"
    ).innerHTML += `<div class="skill-search-content-item"><input type="checkbox" onchange="handleChange(event)" name="${skill.name}" /><label for="${skill.name}">${skill.name}</label></div>`);
  });
});


