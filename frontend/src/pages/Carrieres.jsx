import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Context from "../context/Context";
import { getCarrieres } from "../context/Actions";
import '../styles/sheets.css'

function Carrieres() {

  const { carrieres, dispatch } = useContext(Context)

  useEffect(() => {
    const getCarrieresData = async() => {
      const carrieresData = await getCarrieres()
      dispatch({type: 'GET_CARRIERES', payload: carrieresData})
    }

    getCarrieresData()
  }, []);

  return (
    <div className='container'>
      
      
      <div id="list-container">
      {carrieres.map((carriere) => (

        <div className="sheet-list-item" key={carriere.id}>

            <Link to={`/carrieres/${carriere.id}`} href=""><span className="sheet-list-item-id">{carriere.id}:</span> {carriere.name}</Link>
        
                <div className="crud-grp">
                <Link to={`/confirm/carriere/${carriere.id}`} state= {{
                      name: carriere.name,
                    }}
                  ><button className="crud" id="delete">X</button></Link>
                </div>
        </div>

))}
</div>

      
      
    </div>
  )
}

export default Carrieres