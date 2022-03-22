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
  const {name, group, rank, path, For, End, Hab, Char, Int, Ini, Att, Par, Tir, Na, Pv, For1V, End1V, Hab1V, Char1V, Int1V, Ini1V, Att1V, Par1V, Tir1V, Na1V, Pv1V, For2V, End2V, Hab2V, Char2V, Int2V, Ini2V, Att2V, Par2V, Tir2V, Na2V, Pv2V, For3V, End3V, Hab3V, Char3V, Int3V, Ini3V, Att3V, Par3V, Tir3V, Na3V, Pv3V, For4V, End4V, Hab4V, Char4V, Int4V, Ini4V, Att4V, Par4V, Tir4V, Na4V, Pv4V} = fiche;
  const{For1, End1, Hab1, Char1, Int1, Ini1, Att1, Par1, Tir1, Na1, Pv1, For2, End2, Hab2, Char2, Int2, Ini2, Att2, Par2, Tir2, Na2, Pv2, For3, End3, Hab3, Char3, Int3, Ini3, Att3, Par3, Tir3, Na3, Pv3, For4, End4, Hab4, Char4, Int4, Ini4, Att4, Par4, Tir4, Na4, Pv4} = carriere;

  const [state, setState] = useState({    
    fname: "",
    fgroup: "",
    frank: 1, 
    fpath: null, 
    fFor: 8, 
    fEnd: 8, 
    fHab: 8,
    fChar: 8,
    fInt: 8,
    fIni: 8,
    fAtt: 8,
    fPar: 8,
    fTir: 8,
    fNa: 1, 
    fPv: 60,
    fFor1V: 0, 
    fEnd1V: 0, 
    fHab1V: 0,
    fChar1V: 0,
    fInt1V: 0,
    fIni1V: 0,
    fAtt1V: 0,
    fPar1V: 0,
    fTir1V: 0,
    fNa1V: 0, 
    fPv1V: 0,
    fFor2V: 0, 
    fEnd2V: 0, 
    fHab2V: 0,
    fChar2V: 0,
    fInt2V: 0,
    fIni2V: 0,
    fAtt2V: 0,
    fPar2V: 0,
    fTir2V: 0,
    fNa2V: 0, 
    fPv2V: 0,
    fFor3V: 0, 
    fEnd3V: 0, 
    fHab3V: 0,
    fChar3V: 0,
    fInt3V: 0,
    fIni3V: 0,
    fAtt3V: 0,
    fPar3V: 0,
    fTir3V: 0,
    fNa3V: 0, 
    fPv3V: 0,
    fFor4V: 0, 
    fEnd4V: 0, 
    fHab4V: 0,
    fChar4V: 0,
    fInt4V: 0,
    fIni4V: 0,
    fAtt4V: 0,
    fPar4V: 0,
    fTir4V: 0,
    fNa4V: 0, 
    fPv4V: 0,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const editFicheData = await editFiche(id, state.fname, state.fgroup, state.frank, state.fpath, state.fFor, state.fEnd, state.fHab, state.fChar, state.fInt, state.fIni, state.fAtt, state.fPar, state.fTir, state.fNa, state.fPv, state.fFor1V, state.fEnd1V, state.fHab1V, state.fChar1V, state.fInt1V, state.fIni1V, state.fAtt1V, state.fPar1V, state.fTir1V, state.fNa1V, state.fPv1V, state.fFor2V, state.fEnd2V, state.fHab2V, state.fChar2V, state.fInt2V, state.fIni2V, state.fAtt2V, state.fPar2V, state.fTir2V, state.fNa2V, state.fPv2V, state.fFor3V, state.fEnd3V, state.fHab3V, state.fChar3V, state.fInt3V, state.fIni3V, state.fAtt3V, state.fPar3V, state.fTir3V, state.fNa3V, state.fPv3V, state.fFor4V, state.fEnd4V, state.fHab4V, state.fChar4V, state.fInt4V, state.fIni4V, state.fAtt4V, state.fPar4V, state.fTir4V, state.fNa4V, state.fPv4V);
    dispatch({ type: "GET_FICHE", payload: editFicheData });
    //navigate(`/${id}`);
    window.location.reload();
  };

  const handleChange = async () => {
    const editFicheData = await editFiche(id, state.fname, state.fgroup, state.frank, state.fpath, state.fFor, state.fEnd, state.fHab, state.fChar, state.fInt, state.fIni, state.fAtt, state.fPar, state.fTir, state.fNa, state.fPv);
    dispatch({ type: "GET_FICHE", payload: editFicheData });
  }

  const handleRank = (e) => {
    setState((prevState) => ({...prevState, frank: e.target.value}))
    //handleChange()
  }

  useEffect(() => {
    dispatch({ type: "SET_LOADING" })

    const getFicheData = async () => {
      const ficheData = await getFiche(id);
      dispatch({ type: "GET_FICHE", payload: ficheData });
      setState((prevState) => ({
        ...prevState,
        fname: name,
        fgroup: group,
        frank: 1, 
        fpath: path, 
        fFor: For, 
        fEnd: End, 
        fHab: Hab,
        fChar: Char,
        fInt: Int,
        fIni: Ini,
        fAtt: Att,
        fPar: Par,
        fTir: Tir,
        fNa: Na, 
        fPv: Pv,
        fFor1V: For1V, 
        fEnd1V: End1V, 
        fHab1V: Hab1V,
        fChar1V: Char1V,
        fInt1V: Int1V,
        fIni1V: Ini1V,
        fAtt1V: Att1V,
        fPar1V: Par1V,
        fTir1V: Tir1V,
        fNa1V: Na1V, 
        fPv1V: Pv1V,
        fFor2V: For2V, 
        fEnd2V: End2V, 
        fHab2V: Hab2V,
        fChar2V: Char2V,
        fInt2V: Int2V,
        fIni2V: Ini2V,
        fAtt2V: Att2V,
        fPar2V: Par2V,
        fTir2V: Tir2V,
        fNa2V: Na2V, 
        fPv2V: Pv2V,
        fFor3V: For3V, 
        fEnd3V: End3V, 
        fHab3V: Hab3V,
        fChar3V: Char3V,
        fInt3V: Int3V,
        fIni3V: Ini3V,
        fAtt3V: Att3V,
        fPar3V: Par3V,
        fTir3V: Tir3V,
        fNa3V: Na3V, 
        fPv3V: Pv3V,
        fFor4V: For4V, 
        fEnd4V: End4V, 
        fHab4V: Hab4V,
        fChar4V: Char4V,
        fInt4V: Int4V,
        fIni4V: Ini4V,
        fAtt4V: Att4V,
        fPar4V: Par4V,
        fTir4V: Tir4V,
        fNa4V: Na4V, 
        fPv4V: Pv4V                
      })); 
    };   

    const getCarrieresData = async () => {
      const carrieresData = await getCarrieres();
      dispatch({ type: "GET_CARRIERES", payload: carrieresData });
    };

    const getCarriereData = async () => {
      if(path != null) {
        const carriereData = await getNamedCarriere(path.name);
        dispatch({ type: "GET_NAMED_CARRIERE", payload: carriereData });    
      }       
    };

    getFicheData();
    getCarrieresData();   
    getCarriereData();
  

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dispatch, name]);

  if (loading) {
    return <Spinner /> }

  return (
    <div className='container'>

    <div className="sheet-container">
      <form action="" method="POST" name="sheet-form" onSubmit={handleSubmit}>
        <table className="sheet-table">
          <tbody>
        
            <tr className="sheet-table-header">                    
                <td><input type="text" id="name" placeholder="Nom du joueur" defaultValue={name} onChange={(e) => {setState((prevState) => ({...prevState, fname: e.target.value}))}}/></td>
                  <td>
                    {path && (
                      <select name="path" id="id_path" defaultValue={path.name} onChange={(e) => {setState((prevState) => ({...prevState, fpath: e.target.value}))}} >
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
                          <select name="group" id="id_group" defaultValue={group} onChange={(e) => {setState((prevState) => ({...prevState, fgroup: e.target.value}))}}>                   
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
            <td><input type="number" id="For" min="8" max="16" defaultValue={For} onChange={(e) => {setState((prevState) => ({...prevState, fFor: e.target.value}))}} /></td>
            <td><input type="number" id="End" min="8" max="16" defaultValue={End} onChange={(e) => {setState((prevState) => ({...prevState, fEnd: e.target.value}))}} /></td>
            <td><input type="number" id="Hab" min="8" max="16" defaultValue={Hab} onChange={(e) => {setState((prevState) => ({...prevState, fHab: e.target.value}))}} /></td>
            <td><input type="number" id="Char" min="8" max="16" defaultValue={Char} onChange={(e) => {setState((prevState) => ({...prevState, fChar: e.target.value}))}} /></td>
            <td><input type="number" id="Int" min="8" max="16" defaultValue={Int} onChange={(e) => {setState((prevState) => ({...prevState, fInt: e.target.value}))}} /></td>
            <td><input type="number" id="Ini" min="8" max="16" defaultValue={Ini} onChange={(e) => {setState((prevState) => ({...prevState, fIni: e.target.value}))}} /></td>
            <td><input type="number" id="Att" min="8" max="16" defaultValue={Att} onChange={(e) => {setState((prevState) => ({...prevState, fAtt: e.target.value}))}} /></td>
            <td><input type="number" id="Par" min="8" max="16" defaultValue={Par} onChange={(e) => {setState((prevState) => ({...prevState, fPar: e.target.value}))}} /></td>
            <td><input type="number" id="Tir" min="8" max="16" defaultValue={Tir} onChange={(e) => {setState((prevState) => ({...prevState, fTir: e.target.value}))}} /></td>
            <td><input type="number" id="Na" min="1" max="16" defaultValue={Na} onChange={(e) => {setState((prevState) => ({...prevState, fNa: e.target.value}))}} /></td>
            <td><input type="number" id="Pv" min="60" max="120" step="5" defaultValue={Pv} onChange={(e) => {setState((prevState) => ({...prevState, fPv: e.target.value}))}} /></td>
        </tr>

        {rank === 1 ? (
        <tr className="sheet-table-stats">
          <td><input type="number" id="For1" disabled={For1 === null && (true)} min="0" max={For1} defaultValue={For1 !== null && (For1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fFor1V: e.target.value}))}}/>
            {For1 !== null && (<input className="sup" type="number" placeholder={`/ ${For1}`}/>)}</td>

          <td><input type="number" id="End1" disabled={End1 === null && (true)} min="0" max={End1} defaultValue={End1 !== null && (End1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fEnd1V: e.target.value}))}}/>
            {End1 !== null && (<input className="sup" type="number" placeholder={`/ ${End1}`}/>)}</td>

          <td><input type="number" id="Hab1" disabled={Hab1 === null && (true)} min="0"  max={Hab1} defaultValue={Hab1 !== null && (Hab1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fHab1V: e.target.value}))}}/>
            {Hab1 !== null && (<input className="sup" type="number" placeholder={`/ ${Hab1}`}/>)}</td>

          <td><input type="number" id="Char1" disabled={Char1 === null && (true)} min="0" max={Char1} defaultValue={Char1 !== null && (Char1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fChar1V: e.target.value}))}}/>
            {Char1 !== null && (<input className="sup" type="number" placeholder={`/ ${Char1}`}/>)}</td>

          <td><input type="number" id="Int1" disabled={Int1 === null && (true)} min="0" max={Int1} defaultValue={Int1 !== null && (Int1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fInt1V: e.target.value}))}}/>
            {Int1 !== null && (<input className="sup" type="number" placeholder={`/ ${Int1}`}/>)}</td>

          <td><input type="number" id="Ini1" disabled={Ini1 === null && (true)} min="0" max={Ini1} defaultValue={Ini1 !== null && (Ini1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fIni1V: e.target.value}))}}/>
            {Ini1 !== null && (<input className="sup" type="number" placeholder={`/ ${Ini1}`}/>)}</td>

          <td><input type="number" id="Att1" disabled={Att1 === null && (true)} min="0" max={Att1} defaultValue={Att1 !== null && (Att1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fAtt1V: e.target.value}))}}/>
            {Att1 !== null && (<input className="sup" type="number" placeholder={`/ ${Att1}`}/>)}</td>

          <td><input type="number" id="Par1" disabled={Par1 === null && (true)} min="0" max={Par1} defaultValue={Par1 !== null && (Par1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPar1V: e.target.value}))}}/>
            {Par1 !== null && (<input className="sup" type="number" placeholder={`/ ${Par1}`}/>)}</td>

          <td><input type="number" id="Tir1" disabled={Tir1 === null && (true)} min="0" max={Tir1} defaultValue={Tir1 !== null && (Tir1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fTir1V: e.target.value}))}}/>
            {Tir1 !== null && (<input className="sup" type="number" placeholder={`/ ${Tir1}`}/>)}</td>

          <td><input type="number" id="Na1" disabled={Na1 === null && (true)} min="0" max={Na1} defaultValue={Na1 !== null && (Na1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fNa1V: e.target.value}))}}/>
            {Na1 !== null && (<input className="sup" type="number" placeholder={`/ ${Na1}`}/>)}</td>

          <td><input type="number" id="Pv1" disabled={Pv1 === null && (true)} min="0" max={Pv1} step="5" defaultValue={Pv1 !== null && (Pv1V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPv1V: e.target.value}))}}/>
            {Pv1 !== null && (<input className="sup" type="number" placeholder={`/ ${Pv1}`}/>)}</td>
        </tr>
        ) : rank === 2 ? (
          <tr className="sheet-table-stats">
          <td><input type="number" id="For2" disabled={For2 === null && (true)} min="0" max={For2} defaultValue={For2 !== null && (For2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fFor2V: e.target.value}))}}/>
            {For2 !== null && (<input className="sup" type="number" placeholder={`/ ${For2}`}/>)}</td>

          <td><input type="number" id="End2" disabled={End2 === null && (true)} min="0" max={End2} defaultValue={End2 !== null && (End2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fEnd2V: e.target.value}))}}/>
            {End2 !== null && (<input className="sup" type="number" placeholder={`/ ${End2}`}/>)}</td>

          <td><input type="number" id="Hab2" disabled={Hab2 === null && (true)} min="0"  max={Hab2} defaultValue={Hab2 !== null && (Hab2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fHab2V: e.target.value}))}}/>
            {Hab2 !== null && (<input className="sup" type="number" placeholder={`/ ${Hab2}`}/>)}</td>

          <td><input type="number" id="Char2" disabled={Char2 === null && (true)} min="0" max={Char2} defaultValue={Char2 !== null && (Char2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fChar2V: e.target.value}))}}/>
            {Char2 !== null && (<input className="sup" type="number" placeholder={`/ ${Char2}`}/>)}</td>

          <td><input type="number" id="Int2" disabled={Int2 === null && (true)} min="0" max={Int2} defaultValue={Int2 !== null && (Int2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fInt2V: e.target.value}))}}/>
            {Int2 !== null && (<input className="sup" type="number" placeholder={`/ ${Int2}`}/>)}</td>

          <td><input type="number" id="Ini2" disabled={Ini2 === null && (true)} min="0" max={Ini2} defaultValue={Ini2 !== null && (Ini2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fIni2V: e.target.value}))}}/>
            {Ini2 !== null && (<input className="sup" type="number" placeholder={`/ ${Ini2}`}/>)}</td>

          <td><input type="number" id="Att2" disabled={Att2 === null && (true)} min="0" max={Att2} defaultValue={Att2 !== null && (Att2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fAtt2V: e.target.value}))}}/>
            {Att2 !== null && (<input className="sup" type="number" placeholder={`/ ${Att2}`}/>)}</td>

          <td><input type="number" id="Par2" disabled={Par2 === null && (true)} min="0" max={Par2} defaultValue={Par2 !== null && (Par2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPar2V: e.target.value}))}}/>
            {Par2 !== null && (<input className="sup" type="number" placeholder={`/ ${Par2}`}/>)}</td>

          <td><input type="number" id="Tir2" disabled={Tir2 === null && (true)} min="0" max={Tir2} defaultValue={Tir2 !== null && (Tir2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fTir2V: e.target.value}))}}/>
            {Tir2 !== null && (<input className="sup" type="number" placeholder={`/ ${Tir2}`}/>)}</td>

          <td><input type="number" id="Na2" disabled={Na2 === null && (true)} min="0" max={Na2} defaultValue={Na2 !== null && (Na2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fNa2V: e.target.value}))}}/>
            {Na2 !== null && (<input className="sup" type="number" placeholder={`/ ${Na2}`}/>)}</td>

          <td><input type="number" id="Pv2" disabled={Pv2 === null && (true)} min="0" max={Pv2} step="5" defaultValue={Pv2 !== null && (Pv2V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPv2V: e.target.value}))}}/>
            {Pv2 !== null && (<input className="sup" type="number" placeholder={`/ ${Pv2}`}/>)}</td>
        </tr>
        ) : rank === 3 ? (
          <tr className="sheet-table-stats">
          <td><input type="number" id="For3" disabled={For3 === null && (true)} min="0" max={For3} defaultValue={For3 !== null && (For3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fFor3V: e.target.value}))}}/>
            {For3 !== null && (<input className="sup" type="number" placeholder={`/ ${For3}`}/>)}</td>

          <td><input type="number" id="End3" disabled={End3 === null && (true)} min="0" max={End3} defaultValue={End3 !== null && (End3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fEnd3V: e.target.value}))}}/>
            {End3 !== null && (<input className="sup" type="number" placeholder={`/ ${End3}`}/>)}</td>

          <td><input type="number" id="Hab3" disabled={Hab3 === null && (true)} min="0"  max={Hab3} defaultValue={Hab3 !== null && (Hab3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fHab3V: e.target.value}))}}/>
            {Hab3 !== null && (<input className="sup" type="number" placeholder={`/ ${Hab3}`}/>)}</td>

          <td><input type="number" id="Char3" disabled={Char3 === null && (true)} min="0" max={Char3} defaultValue={Char3 !== null && (Char3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fChar3V: e.target.value}))}}/>
            {Char3 !== null && (<input className="sup" type="number" placeholder={`/ ${Char3}`}/>)}</td>

          <td><input type="number" id="Int3" disabled={Int3 === null && (true)} min="0" max={Int3} defaultValue={Int3 !== null && (Int3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fInt3V: e.target.value}))}}/>
            {Int3 !== null && (<input className="sup" type="number" placeholder={`/ ${Int3}`}/>)}</td>

          <td><input type="number" id="Ini3" disabled={Ini3 === null && (true)} min="0" max={Ini3} defaultValue={Ini3 !== null && (Ini3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fIni3V: e.target.value}))}}/>
            {Ini3 !== null && (<input className="sup" type="number" placeholder={`/ ${Ini3}`}/>)}</td>

          <td><input type="number" id="Att3" disabled={Att3 === null && (true)} min="0" max={Att3} defaultValue={Att3 !== null && (Att3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fAtt3V: e.target.value}))}}/>
            {Att3 !== null && (<input className="sup" type="number" placeholder={`/ ${Att3}`}/>)}</td>

          <td><input type="number" id="Par3" disabled={Par3 === null && (true)} min="0" max={Par3} defaultValue={Par3 !== null && (Par3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPar3V: e.target.value}))}}/>
            {Par3 !== null && (<input className="sup" type="number" placeholder={`/ ${Par3}`}/>)}</td>

          <td><input type="number" id="Tir3" disabled={Tir3 === null && (true)} min="0" max={Tir3} defaultValue={Tir3 !== null && (Tir3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fTir3V: e.target.value}))}}/>
            {Tir3 !== null && (<input className="sup" type="number" placeholder={`/ ${Tir3}`}/>)}</td>

          <td><input type="number" id="Na3" disabled={Na3 === null && (true)} min="0" max={Na3} defaultValue={Na3 !== null && (Na3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fNa3V: e.target.value}))}}/>
            {Na3 !== null && (<input className="sup" type="number" placeholder={`/ ${Na3}`}/>)}</td>

          <td><input type="number" id="Pv3" disabled={Pv3 === null && (true)} min="0" max={Pv3} step="5" defaultValue={Pv3 !== null && (Pv3V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPv3V: e.target.value}))}}/>
            {Pv3 !== null && (<input className="sup" type="number" placeholder={`/ ${Pv3}`}/>)}</td>
        </tr>
        ) : rank === 4 && (
          <tr className="sheet-table-stats">
          <td><input type="number" id="For4" disabled={For4 === null && (true)} min="0" max={For4} defaultValue={For4 !== null && (For4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fFor4V: e.target.value}))}}/>
            {For4 !== null && (<input className="sup" type="number" placeholder={`/ ${For4}`}/>)}</td>

          <td><input type="number" id="End4" disabled={End4 === null && (true)} min="0" max={End4} defaultValue={End4 !== null && (End4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fEnd4V: e.target.value}))}}/>
            {End4 !== null && (<input className="sup" type="number" placeholder={`/ ${End4}`}/>)}</td>

          <td><input type="number" id="Hab4" disabled={Hab4 === null && (true)} min="0"  max={Hab4} defaultValue={Hab4 !== null && (Hab4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fHab4V: e.target.value}))}}/>
            {Hab4 !== null && (<input className="sup" type="number" placeholder={`/ ${Hab4}`}/>)}</td>

          <td><input type="number" id="Char4" disabled={Char4 === null && (true)} min="0" max={Char4} defaultValue={Char4 !== null && (Char4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fChar4V: e.target.value}))}}/>
            {Char4 !== null && (<input className="sup" type="number" placeholder={`/ ${Char4}`}/>)}</td>

          <td><input type="number" id="Int4" disabled={Int4 === null && (true)} min="0" max={Int4} defaultValue={Int4 !== null && (Int4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fInt4V: e.target.value}))}}/>
            {Int4 !== null && (<input className="sup" type="number" placeholder={`/ ${Int4}`}/>)}</td>

          <td><input type="number" id="Ini4" disabled={Ini4 === null && (true)} min="0" max={Ini4} defaultValue={Ini4 !== null && (Ini4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fIni4V: e.target.value}))}}/>
            {Ini4 !== null && (<input className="sup" type="number" placeholder={`/ ${Ini4}`}/>)}</td>

          <td><input type="number" id="Att4" disabled={Att4 === null && (true)} min="0" max={Att4} defaultValue={Att4 !== null && (Att4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fAtt4V: e.target.value}))}}/>
            {Att4 !== null && (<input className="sup" type="number" placeholder={`/ ${Att4}`}/>)}</td>

          <td><input type="number" id="Par4" disabled={Par4 === null && (true)} min="0" max={Par4} defaultValue={Par4 !== null && (Par4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPar4V: e.target.value}))}}/>
            {Par4 !== null && (<input className="sup" type="number" placeholder={`/ ${Par4}`}/>)}</td>

          <td><input type="number" id="Tir4" disabled={Tir4 === null && (true)} min="0" max={Tir4} defaultValue={Tir4 !== null && (Tir4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fTir4V: e.target.value}))}}/>
            {Tir4 !== null && (<input className="sup" type="number" placeholder={`/ ${Tir4}`}/>)}</td>

          <td><input type="number" id="Na4" disabled={Na4 === null && (true)} min="0" max={Na4} defaultValue={Na4 !== null && (Na4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fNa4V: e.target.value}))}}/>
            {Na4 !== null && (<input className="sup" type="number" placeholder={`/ ${Na4}`}/>)}</td>

          <td><input type="number" id="Pv4" disabled={Pv4 === null && (true)} min="0" max={Pv4} step="5" defaultValue={Pv4 !== null && (Pv4V)}
           onChange={(e) => {setState((prevState) => ({...prevState, fPv4V: e.target.value}))}}/>
            {Pv4 !== null && (<input className="sup" type="number" placeholder={`/ ${Pv4}`}/>)}</td>
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
