import { useContext, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import Context from "../context/Context";
import { getFiche } from "../context/Actions";

function Fiche() {
  const { fiche, dispatch } = useContext(Context)
  const {id} = useParams()

  useEffect(() => {
    const getFicheData = async() => {
      const ficheData = await getFiche(id)
      dispatch({type: 'GET_FICHE', payload: ficheData})
    }

    getFicheData()
  }, []);
  return (
    <div className='container'>
      <h1>Fiche {fiche.name}</h1>
    </div>
  )
}

export default Fiche