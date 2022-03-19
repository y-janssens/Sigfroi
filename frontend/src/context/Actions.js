import axios from "axios";

const manager = axios.create();

export const getToken = async (username, password) => {
  const response = await manager({
    method: 'POST',
    url: '/api/token/',    
    data: {
      username,
      password,
    }
  })

  return response.data;
}

export const getFiches = async () => {
  const response = await manager.get(`/api/fiches/`);

  return response.data;
};

export const getFiche = async (id) => {
  const response = await manager.get(`/api/fiches/${id}`);

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

export const deleteItem = async(item, id) => {
  const response = await manager.delete(`/api/${item}s/${id}`);

  return response.data;
};