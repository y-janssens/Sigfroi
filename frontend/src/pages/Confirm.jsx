import '../styles/confirm.css';
import { useContext } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import Context from '../context/Context';
import { deleteItem } from '../context/Actions';

function Confirm(props) {
    const location = useLocation()
    const {item, id} = useParams();
    const navigate = useNavigate();
    const {name, path} = location.state;
    const { dispatch } = useContext(Context)
    
    const handleDelete = async () => {
        const itemData = await deleteItem(item, id);
        dispatch({type: 'DELETE_ITEM', payload: itemData});
        if (item === "fiche") {
            navigate('/');
        } else {
        navigate(`/${item}s`);
        }
    }; 

  return (
    <div id="prompt_wrapper">
        
        <div id="prompt_text">Voulez-vous vraiment supprimer cet élément? 
            {item === 'fiche' ? (<p>{name} - {path}</p>) 
            : item === 'carriere' && (<p>{name}</p>)}
            
        </div>
        
        <div id="prompt_btn_grp">

            <button className="prompt_action" id="prompt_confirm" onClick={handleDelete}>Oui</button>  
            <button className="prompt_action" id="prompt_deny" onClick={() => navigate(-1)}>Non</button>

            
        </div>
    </div>
  )
}

export default Confirm