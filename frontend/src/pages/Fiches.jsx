import { useContext, useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Context from "../context/Context";
import { getFiches, getCarrieres, addFiche } from "../context/Actions";
import '../styles/sheets.css'
import '../styles/tables.css'

function Fiches() {

  const { fiches, carrieres, dispatch } = useContext(Context)
  const navigate = useNavigate()
  const [name, setName] = useState('')
  const [group, setGroup] = useState('')
  const [rank, setRank] = useState(1)
  const [path, setPath] = useState('')
  const [For, setFor] = useState(8)
  const [End, setEnd] = useState(8)
  const [Hab, setHab] = useState(8)
  const [Char, setChar] = useState(8)
  const [Int, setInt] = useState(8)
  const [Ini, setIni] = useState(8)
  const [Att, setAtt] = useState(8)
  const [Par, setPar] = useState(8)
  const [Tir, setTir] = useState(8)
  const [Na, setNa] = useState(1)
  const [Pv, setPv] = useState(60)

  const handleSubmit = async (e) => {
    e.preventDefault();
    const addFicheData = await addFiche(name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv)
      dispatch({type: 'ADD_FICHE', payload: addFicheData})
      navigate('/')
  }

  useEffect(() => {
    const getFichesData = async() => {
      const fichesData = await getFiches()
      dispatch({type: 'GET_FICHES', payload: fichesData})
    }

    const getCarrieresData = async() => {
      const carrieresData = await getCarrieres()
      dispatch({type: 'GET_CARRIERES', payload: carrieresData})
    }

    getCarrieresData()
    getFichesData()
  }, [dispatch]);


  return (
  <div className='container'>

    <div className="sheet-container">
      <form action="" method="POST" name="sheet-form" onSubmit={handleSubmit}>
        <table className="sheet-table">
          <tbody>
        
            <tr className="sheet-table-header">                    
                <td><input type="text" id="name" placeholder="Nom du joueur" onChange={(e)=> setName(e.target.value)}/></td>
                  <td>
                    <select name="path" id="id_path" onChange={(e)=> setPath(e.target.value)}>
                      {carrieres.map((carriere)=> (
                        <option key={carriere.id}>{carriere.name}</option>
                      ))}
                      
                    </select>
                  </td>      
            </tr>

            <tr className="sheet-table-header">                    
                      <td>
                        <select name="group" id="id_group" onChange={(e)=> setGroup(e.target.value)}>                   
                          <option value="Groupe">Groupe</option>                  
                          <option value="Milice(ne)">Milice</option>                  
                          <option value="Habitant(e)">Peuple</option>                  
                          <option value="Noble">Noblesse</option>                  
                          <option value="Prêtre(sse)">Clergé</option>                  
                          <option value="Banni(e)">Bannis</option>                  
                        </select>
                      </td>

                      <td><p>de rang</p></td> 

                      <td>
                        <select name="rank" onChange={(e)=> setRank(e.target.value)}>
                          <option value="1">1</option>
                          <option value="2">2</option>
                          <option value="3">3</option>
                          <option value="4">4</option>
                        </select>
                      </td>    
              </tr>


        <tr className="sheet-table-stats">
            <td style={{borderBottom:"none"}}>FOR</td>
            <td style={{borderBottom:"none"}}>END</td>
            <td style={{borderBottom:"none"}}>HAB</td>
            <td style={{borderBottom:"none"}}>CHA</td>
            <td style={{borderBottom:"none"}}>INT</td>
            <td style={{borderBottom:"none"}}>INI</td>
            <td style={{borderBottom:"none"}}>ATT</td>
            <td style={{borderBottom:"none"}}>PAR</td>
            <td style={{borderBottom:"none"}}>TIR</td>
            <td style={{borderBottom:"none"}}>NA</td>
            <td style={{borderBottom:"none"}}>PV</td>
        </tr>

        <tr className="sheet-table-stats">
            <td><input type="number" name="For" min="8" max="16" defaultValue="8" onChange={(e)=> setFor(e.target.value)} /></td>
            <td><input type="number" name="End" min="8" max="16" defaultValue="8" onChange={(e)=> setEnd(e.target.value)} /></td>
            <td><input type="number" name="Hab" min="8" max="16" defaultValue="8" onChange={(e)=> setHab(e.target.value)} /></td>
            <td><input type="number" name="Char" min="8" max="16" defaultValue="8" onChange={(e)=> setChar(e.target.value)} /></td>
            <td><input type="number" name="Int" min="8" max="16" defaultValue="8" onChange={(e)=> setInt(e.target.value)} /></td>
            <td><input type="number" name="Ini" min="8" max="16" defaultValue="8" onChange={(e)=> setIni(e.target.value)} /></td>
            <td><input type="number" name="Att" min="8" max="16" defaultValue="8" onChange={(e)=> setAtt(e.target.value)} /></td>
            <td><input type="number" name="Par" min="8" max="16" defaultValue="8" onChange={(e)=> setPar(e.target.value)} /></td>
            <td><input type="number" name="Tir" min="8" max="16" defaultValue="8" onChange={(e)=> setTir(e.target.value)} /></td>
            <td><input type="number" name="Na" min="1" max="16" defaultValue="1" onChange={(e)=> setNa(e.target.value)} /></td>
            <td><input type="number" name="Pv" min="60" max="120" step="5" defaultValue="60" onChange={(e)=> setPv(e.target.value)} /></td>
        </tr>
        </tbody>
      
    </table>

    <div className="sheet-table-btns-grp">
            <button type="submit" className="sheet-table-btn">Valider</button>
            <button type="reset" className="sheet-table-btn" id="reset">Effacer</button>
            </div>

    </form>

    </div>
      
      <div id="list-container">
        
        {fiches.map((fiche) => (

          <div className="sheet-list-item" key={fiche.id}>

          {fiche.group === "Noble" ? (
           <Link to={`/${fiche.id}`}><span className="sheet-list-item-id">{fiche.id}:</span> <span className="noble_c">{fiche.name}</span> - {fiche.path ? (fiche.path.name) : null}</Link>
         ) : fiche.group === "Milice(ne)" ? (
          <Link to={`/${fiche.id}`}><span className="sheet-list-item-id">{fiche.id}:</span> <span className="milice_c">{fiche.name}</span> - {fiche.path ? (fiche.path.name) : null}</Link>
        ) : fiche.group === "Habitant(e)" ? (
          <Link to={`/${fiche.id}`}><span className="sheet-list-item-id">{fiche.id}:</span> <span className="peuple_c">{fiche.name}</span> - {fiche.path ? (fiche.path.name) : null}</Link>
        ) : fiche.group === "Prêtre(sse)" ? (
          <Link to={`/${fiche.id}`}><span className="sheet-list-item-id">{fiche.id}:</span> <span className="clerge_c">{fiche.name}</span> - {fiche.path ? (fiche.path.name) : null}</Link>
        ) : fiche.group === "Banni(e)" && (
          <Link to={`/${fiche.id}`}><span className="sheet-list-item-id">{fiche.id}:</span> <span className="banni_c">{fiche.name}</span> - {fiche.path ? (fiche.path.name) : null}</Link>
        )}
         
         


              <div className="crud-grp">
                  <Link to={`/confirm/fiche/${fiche.id}`} state= {{
                      name: fiche.name,
                      path: fiche.path.name
                    }}
                  ><button className="crud" id="delete">X</button></Link>
              </div>
          </div>

        ))}

            

        
    </div>
    </div>
  )
}

export default Fiches