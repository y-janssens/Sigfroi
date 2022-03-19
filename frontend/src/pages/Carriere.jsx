import { useContext, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import Context from "../context/Context";
import { getCarriere } from "../context/Actions";

function Carriere() {
  const { carriere, dispatch } = useContext(Context)
  const {id} = useParams()

  useEffect(() => {
    const getCarriereData = async() => {
      const carriereData = await getCarriere(id)
      dispatch({type: 'GET_CARRIERE', payload: carriereData})
    }

    getCarriereData()
  }, []);
  return (
    <div className='container'>
      <h1>{carriere.name}</h1>
    </div>
  )
}

export default Carriere