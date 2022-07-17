class Selector {
  constructor(query, name, queryParse) {
    this.query = query;
    this.name = name;
    this.queryParse = queryParse;
    this.queryToggle = false;
    this.queryCount = 0;
    this.queryPayload = [];
    this.queryList = document.getElementById(`${query}s-list`);
    this.queryResult = document.getElementById(`${query}_search_bar_input`);

    this.queryResult.addEventListener("keyup", () => {
      let search = this.queryResult.value.toLowerCase();
      this.queryList.innerHTML = "";
      this.querysList = this.queryParse.filter(function (query) {
        return query.name.toLowerCase().includes(search?.toLowerCase());
      });
      this.parse(this.querysList);
    });
  }

  get masculine() {
    return this.query === "stuff" || this.query === "alias";
  }

  get hasNoSelection() {
    return this.queryCount < 1;
  }

  get plural() {
    return this.queryCount >= 2;
  }

  parse(list) {
    list.map((item) => {
      return (this.queryList.innerHTML += `<div class="query-search-content-item"><input type="checkbox" onchange="handle${this.query}Check(event)" value="${item.name}" name="${item}-request" /><label for="${item.name}" class="${item}-search-content-item-label" onclick="handle${this.query}Click(event)">${item.name}</label></div>`);
    });
    this.handleQueryTitle();
  }

  handleQueryPayload() {
    for (let i in this.queryPayload) {
      this.queryList.innerHTML += `<input type="text" name="send-${this.query}" value="${this.queryPayload[i]}" style="display: none" />`;
    }
  }

  panelQueryToggle() {
    if (this.queryToggle == false) {
      this.queryToggle = true;
      $(`#${this.query}s-selector-container`).css("min-height", "315px");
      $(`#${this.query}s-search-container`).css("height", "235px");
      $(`#${this.query}s-search-container`).css("padding", "5px 0");
      $(`#${this.query}s-search-container`).css("border", "1px solid #938471");
      $(`.${this.query}-search-content`).css("height", "180px");
      $(`.${this.query}-arrow`).css("transform", "rotate(-90deg)");
      $(`.${this.query}s-search-btn`).css("display", "flex");
    } else {
      this.queryToggle = false;
      $(`#${this.query}s-selector-container`).css("min-height", "200px");
      $(`#${this.query}s-search-container`).css("height", "0px");
      $(`#${this.query}s-search-container`).css("padding", "0");
      $(`#${this.query}s-search-container`).css("border-top", "none");
      $(`#${this.query}s-search-container`).css("border-bottom", "none");
      $(`.${this.query}-search-content`).css("height", "0px");
      $(`.${this.query}-arrow`).css("transform", "rotate(90deg)");
      $(`.${this.query}s-search-btn`).css("display", "none");
    }
  }

  handleQueryTitle() {
    const value = `${this.queryCount} ${this.name}`;
    const element = this.masculine ? `Ajouter un nouvel ${this.name}` : `Ajouter une nouvelle ${this.name}`;
    const selected = this.masculine ? (this.plural ? `${value}s sélectionnés` : `${value} sélectionné`) : (this.plural ? `${value}s sélectionnées` : `${value} sélectionnée`);

    document.getElementById(`${this.query}-selector-title`).innerHTML = this.hasNoSelection ? element : selected;
  }

  handleQueryClick(event) {
    event.target.closest("div").children[0].click();
  }

  handleQueryCheck(event) {
    if (event.target.checked) {
      this.queryCount += 1;
      this.queryPayload.push(event.target.value);
    } else {
      this.queryCount -= 1;
      for (let i in this.queryPayload) {
        if (this.queryPayload[i] == event.target.value) {
          this.queryPayload.splice(i, 1);
        }
      }
    }
    this.handleQueryTitle();
  }
}