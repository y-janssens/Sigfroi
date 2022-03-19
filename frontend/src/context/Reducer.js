const reducer = (state, action) => {
  switch (action.type) {
    case "GET_TOKEN":
      return {
        ...state,
        token: action.payload
      };
    case "GET_ACCESS":
      return {
        ...state,
        access: action.payload
      };
    case "GET_FICHES":
      return {
        ...state,
        fiches: action.payload
      };
    case "GET_FICHE":
      return {
        ...state,
        fiche: action.payload
      };
    case "GET_CARRIERES":
      return {
        ...state,
        carrieres: action.payload
      };
    case "GET_CARRIERE":
      return {
        ...state,
        carriere: action.payload
      };
    case "DELETE_ITEM":
      return {
        ...state,
        item: action.payload
      };
    default:
      return state;
  }
};

export default reducer;
