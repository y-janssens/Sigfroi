import { useContext, useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import Context from "../context/Context";
import { getFiche, getCarrieres, editFiche, getNamedCarriere } from "../context/Actions";
import Spinner from "../components/Spinner"
import "../styles/sheets.css";
import "../styles/tables.css";

function Fiche() {
  const { fiche, carrieres, carriere, loading, dispatch } = useContext(Context);
  const { id } = useParams();
  const navigate = useNavigate();
  const {name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv} = fiche;
  const{For1, End1, Hab1, Char1, Int1, Ini1, Att1, Par1, Tir1, Na1, Pv1, For2, End2, Hab2, Char2, Int2, Ini2, Att2, Par2, Tir2, Na2, Pv2, For3, End3, Hab3, Char3, Int3, Ini3, Att3, Par3, Tir3, Na3, Pv3, For4, End4, Hab4, Char4, Int4, Ini4, Att4, Par4, Tir4, Na4, Pv4} = carriere;

  const [fname, setName] = useState('');
  const [fgroup, setGroup] = useState('');
  const [frank, setRank] = useState(1);
  const [fpath, setPath] = useState(null);
  const [fFor, setFor] = useState(8);
  const [fEnd, setEnd] = useState(8);
  const [fHab, setHab] = useState(8);
  const [fChar, setChar] = useState(8);
  const [fInt, setInt] = useState(8);
  const [fIni, setIni] = useState(8);
  const [fAtt, setAtt] = useState(8);
  const [fPar, setPar] = useState(8);
  const [fTir, setTir] = useState(8);
  const [fNa, setNa] = useState(1);
  const [fPv, setPv] = useState(60);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const editFicheData = await editFiche(id, fname, fgroup, frank, fpath, fFor, fEnd, fHab, fChar, fInt, fIni, fAtt, fPar, fTir, fNa, fPv);
    dispatch({ type: "GET_FICHE", payload: editFicheData });
    navigate(`/${id}`);
  };

  const handleChange = async () => {
    const editFicheData = await editFiche(id, fname, fgroup, frank, fpath, fFor, fEnd, fHab, fChar, fInt, fIni, fAtt, fPar, fTir, fNa, fPv);
    dispatch({ type: "GET_FICHE", payload: editFicheData });
    navigate(`/${id}`);
  }

  const handleRank = (e) => {
    setRank(e.currentTarget.value)
    handleChange()
  }

  useEffect(() => {
    dispatch({ type: "SET_LOADING" })

    const getFicheData = async () => {
      const ficheData = await getFiche(id);
      dispatch({ type: "GET_FICHE", payload: ficheData });
      setName(name);
      setGroup(group);
      //setRank(rank);
      setPath(path);
      setFor(For);
      setEnd(End);
      setHab(Hab);
      setChar(Char);
      setInt(Int);
      setIni(Ini);
      setAtt(Att);
      setPar(Par);
      setTir(Tir);
      setNa(Na);
      setPv(Pv);
    
    };   

    const getCarrieresData = async () => {
      const carrieresData = await getCarrieres();
      dispatch({ type: "GET_CARRIERES", payload: carrieresData });
    };


    getFicheData();
    getCarrieresData();

    const getCarriereData = async () => {
        if(path != null) {
      const carriereData = await getNamedCarriere(path.name);
    dispatch({ type: "GET_NAMED_CARRIERE", payload: carriereData });    
        }
         
  };

  getCarriereData();
  

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dispatch, name]);

  if (loading) {
    return <Spinner />
  }

  return (
    <div className='container'>

    <div className="sheet-container">
      <form action="" method="POST" name="sheet-form" onSubmit={handleSubmit}>
        <table className="sheet-table">
          <tbody>
        
            <tr className="sheet-table-header">                    
                <td><input type="text" id="name" placeholder="Nom du joueur" defaultValue={name} onChange={(e)=> setName(e.target.value)}/></td>
                  <td>
                    {path && (
                      <select name="path" id="id_path" defaultValue={path.name} onChange={(e)=> setPath(e.target.value)}>
                      {carrieres.map((carriere)=> (
                        <option key={carriere.id}>{carriere.name}</option>
                      ))}                      
                    </select>
                    )}
                  </td>      
            </tr>

            <tr className="sheet-table-header">                    
                      <td>
                        {group && (
                          <select name="group" id="id_group" defaultValue={group} onChange={(e)=> setGroup(e.target.value)}>                   
                          <option value="Groupe">Groupe</option>                  
                          <option value="Milice(ne)">Milice</option>                  
                          <option value="Habitant(e)">Peuple</option>                  
                          <option value="Noble">Noblesse</option>                  
                          <option value="Prêtre(sse)">Clergé</option>                  
                          <option value="Banni(e)">Bannis</option>                  
                        </select>
                        )}
                      </td>

                      <td><p>de rang</p></td> 

                      <td>
                        {rank && (
                          <select name="rank" defaultValue={rank} onChange={handleRank}>
                          <option value="1">1</option>
                          <option value="2">2</option>
                          <option value="3">3</option>
                          <option value="4">4</option>
                        </select>
                        )}
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
            <td><input type="number" name="For" min="8" max="16" defaultValue={For} onChange={(e)=> setFor(e.target.value)} /></td>
            <td><input type="number" name="End" min="8" max="16" defaultValue={End} onChange={(e)=> setEnd(e.target.value)} /></td>
            <td><input type="number" name="Hab" min="8" max="16" defaultValue={Hab} onChange={(e)=> setHab(e.target.value)} /></td>
            <td><input type="number" name="Char" min="8" max="16" defaultValue={Char} onChange={(e)=> setChar(e.target.value)} /></td>
            <td><input type="number" name="Int" min="8" max="16" defaultValue={Int} onChange={(e)=> setInt(e.target.value)} /></td>
            <td><input type="number" name="Ini" min="8" max="16" defaultValue={Ini} onChange={(e)=> setIni(e.target.value)} /></td>
            <td><input type="number" name="Att" min="8" max="16" defaultValue={Att} onChange={(e)=> setAtt(e.target.value)} /></td>
            <td><input type="number" name="Par" min="8" max="16" defaultValue={Par} onChange={(e)=> setPar(e.target.value)} /></td>
            <td><input type="number" name="Tir" min="8" max="16" defaultValue={Tir} onChange={(e)=> setTir(e.target.value)} /></td>
            <td><input type="number" name="Na" min="1" max="16" defaultValue={Na} onChange={(e)=> setNa(e.target.value)} /></td>
            <td><input type="number" name="Pv" min="60" max="120" step="5" defaultValue={Pv} onChange={(e)=> setPv(e.target.value)} /></td>
        </tr>

        {rank === 1 ? (
        <tr className="sheet-table-stats">
        <td><input type="number" name="For" min="1" max="16" defaultValue={For1} /></td>
        <td><input type="number" name="End" min="1" max="16" defaultValue={End1} /></td>
        <td><input type="number" name="Hab" min="1" max="16" defaultValue={Hab1} /></td>
        <td><input type="number" name="Char" min="1" max="16" defaultValue={Char1} /></td>
        <td><input type="number" name="Int" min="1" max="16" defaultValue={Int1} /></td>
        <td><input type="number" name="Ini" min="1" max="16" defaultValue={Ini1} /></td>
        <td><input type="number" name="Att" min="1" max="16" defaultValue={Att1} /></td>
        <td><input type="number" name="Par" min="1" max="16" defaultValue={Par1} /></td>
        <td><input type="number" name="Tir" min="1" max="16" defaultValue={Tir1} /></td>
        <td><input type="number" name="Na" min="1" max="16" defaultValue={Na1} /></td>
        <td><input type="number" name="Pv" min="5" max="120" step="5" defaultValue={Pv1} /></td>
    </tr>
        ) : rank === 2 ? (
          <tr className="sheet-table-stats">
          <td><input type="number" name="For" min="1" max="16" defaultValue={For2} /></td>
          <td><input type="number" name="End" min="1" max="16" defaultValue={End2} /></td>
          <td><input type="number" name="Hab" min="1" max="16" defaultValue={Hab2} /></td>
          <td><input type="number" name="Char" min="1" max="16" defaultValue={Char2} /></td>
          <td><input type="number" name="Int" min="1" max="16" defaultValue={Int2} /></td>
          <td><input type="number" name="Ini" min="1" max="16" defaultValue={Ini2} /></td>
          <td><input type="number" name="Att" min="1" max="16" defaultValue={Att2} /></td>
          <td><input type="number" name="Par" min="1" max="16" defaultValue={Par2} /></td>
          <td><input type="number" name="Tir" min="1" max="16" defaultValue={Tir2} /></td>
          <td><input type="number" name="Na" min="1" max="16" defaultValue={Na2} /></td>
          <td><input type="number" name="Pv" min="5" max="120" step="5" defaultValue={Pv2} /></td>
      </tr>
        ) : rank === 3 ? (
          <tr className="sheet-table-stats">
          <td><input type="number" name="For" min="1" max="16" defaultValue={For3} /></td>
          <td><input type="number" name="End" min="1" max="16" defaultValue={End3} /></td>
          <td><input type="number" name="Hab" min="1" max="16" defaultValue={Hab3} /></td>
          <td><input type="number" name="Char" min="1" max="16" defaultValue={Char3} /></td>
          <td><input type="number" name="Int" min="1" max="16" defaultValue={Int3} /></td>
          <td><input type="number" name="Ini" min="1" max="16" defaultValue={Ini3} /></td>
          <td><input type="number" name="Att" min="1" max="16" defaultValue={Att3} /></td>
          <td><input type="number" name="Par" min="1" max="16" defaultValue={Par3} /></td>
          <td><input type="number" name="Tir" min="1" max="16" defaultValue={Tir3} /></td>
          <td><input type="number" name="Na" min="1" max="16" defaultValue={Na3} /></td>
          <td><input type="number" name="Pv" min="5" max="120" step="5" defaultValue={Pv3} /></td>
      </tr>
        ) : rank === 4 && (
          <tr className="sheet-table-stats">
            <td><input type="number" name="For" min="1" max="16" defaultValue={For4} /></td>
            <td><input type="number" name="End" min="1" max="16" defaultValue={End4} /></td>
            <td><input type="number" name="Hab" min="1" max="16" defaultValue={Hab4} /></td>
            <td><input type="number" name="Char" min="1" max="16" defaultValue={Char4} /></td>
            <td><input type="number" name="Int" min="1" max="16" defaultValue={Int4} /></td>
            <td><input type="number" name="Ini" min="1" max="16" defaultValue={Ini4} /></td>
            <td><input type="number" name="Att" min="1" max="16" defaultValue={Att4} /></td>
            <td><input type="number" name="Par" min="1" max="16" defaultValue={Par4} /></td>
            <td><input type="number" name="Tir" min="1" max="16" defaultValue={Tir4} /></td>
            <td><input type="number" name="Na" min="1" max="16" defaultValue={Na4} /></td>
            <td><input type="number" name="Pv" min="5" max="120" step="5" defaultValue={Pv4} /></td>
        </tr>
        )}
        </tbody>
      
    </table>

    <div className="sheet-table-btns-grp">
            <button type="submit" className="sheet-table-btn">Valider</button>
            <button type="reset" className="sheet-table-btn" id="reset">Effacer</button>
            </div>

    </form>

    </div>
    </div>
  )
}

export default Fiche
