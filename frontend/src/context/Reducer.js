const reducer = (state, action) => {
  switch (action.type) {
    case "GET_TOKEN":
      return {
        ...state,
        token: action.payload,
        loading: false,
      };
    case "SET_LOADING":
      return {
        ...state,
        loading: true,
      };
    case "GET_ACCESS":
      return {
        ...state,
        access: action.payload,
        loading: false,
      };
    case "ADD_FICHE":
      return {
        ...state,
        fiche: action.payload,
        loading: false,
      };
    case "GET_FICHES":
      return {
        ...state,
        fiches: action.payload,
        loading: false,
      };
    case "GET_FICHE":
      return {
        ...state,
        fiche: action.payload,
        loading: false,
      };
    case "EDIT_FICHE":
      return {
        ...state,
        fiche: action.payload,
        loading: false,
      };
    case "GET_CARRIERES":
      return {
        ...state,
        carrieres: action.payload,
        loading: false,
      };
    case "GET_CARRIERE":
      return {
        ...state,
        carriere: action.payload,
        loading: false,
      };
    case "GET_NAMED_CARRIERE":
      return {
        ...state,
        carriere: action.payload,
        loading: false,
      };
    case "DELETE_ITEM":
      return {
        ...state,
        item: action.payload,
        loading: false,
      };
    default:
      return state;
  }
};

export default reducer;
