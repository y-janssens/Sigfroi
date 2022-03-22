import axios from "axios";

const manager = axios.create();

export const getToken = async (username, password) => {
  const response = await manager({
    method: "POST",
    url: `/api/token/`,
    data: {
      username,
      password,
    },
  });

  return response.data;
};

export const getFiches = async () => {
  const response = await manager.get(`/api/fiches/`);

  return response.data;
};

export const getFiche = async (id) => {
  const response = await manager.get(`/api/fiches/${id}`);

  return response.data;
};

export const addFiche = async (name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv) => {
  const response = await manager({
    method: "POST",
    url: `/api/fiches/add/`,
    data: {name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv},
  });

  return response.data;
};

export const editFiche = async (id, name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv, For1V, End1V, Hab1V, Char1V, Int1V, Ini1V, Att1V, Par1V, Tir1V, Na1V, Pv1V, For2V, End2V, Hab2V, Char2V, Int2V, Ini2V, Att2V, Par2V, Tir2V, Na2V, Pv2V, For3V, End3V, Hab3V, Char3V, Int3V, Ini3V, Att3V, Par3V, Tir3V, Na3V, Pv3V, For4V, End4V, Hab4V, Char4V, Int4V, Ini4V, Att4V, Par4V, Tir4V, Na4V, Pv4V) => {
  const response = await manager({
    method: "PUT",
    url: `/api/fiches/${id}/`,
    data: {name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv, For1V, End1V, Hab1V, Char1V, Int1V, Ini1V, Att1V, Par1V, Tir1V, Na1V, Pv1V, For2V, End2V, Hab2V, Char2V, Int2V, Ini2V, Att2V, Par2V, Tir2V, Na2V, Pv2V, For3V, End3V, Hab3V, Char3V, Int3V, Ini3V, Att3V, Par3V, Tir3V, Na3V, Pv3V, For4V, End4V, Hab4V, Char4V, Int4V, Ini4V, Att4V, Par4V, Tir4V, Na4V, Pv4V},
  });

  return response.data;
};
  

export const getCarrieres = async () => {
  const response = await manager.get(`/api/carrieres/`);

  return response.data;
};

export const getCarriere = async (id) => {
  const response = await manager.get(`/api/carrieres/${id}`);

  return response.data;
};

export const getNamedCarriere = async (name) => {
  const response = await manager.get(`/api/carrieres/name/${name}`);

  return response.data;
};

export const deleteItem = async (item, id) => {
  const response = await manager.delete(`/api/${item}s/${id}`);

  return response.data;
};
