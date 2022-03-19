import { useEffect, useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "../styles/header.css";

function Header() {
  const navigate = useNavigate();
  const [isLogged, setIsLogged] = useState(false);
  const token = localStorage.getItem("authToken");
  useEffect(() => {
    const checkStatus = async () => {
      if (token) {
        setIsLogged(true);
      }
    };
    checkStatus();
  }, [isLogged, token]);

  const logout = () => {
    if (localStorage.getItem("authToken")) {
      localStorage.removeItem("authToken");
      setIsLogged(false);
      navigate("/login");
    }
  };

  return (
    <div id="navHeader">

        <a className="forum-title" href="https://marbrume.forumactif.com/">Marbrume - La ville des damnés</a>

    <div className="header-links-grp">       
        
        <Link to="/"><p>Fiches</p></Link>
        <Link to="carrieres/"><p>Carrières</p></Link>
        
    </div>
    {isLogged && (<button className="header-btn" onClick={logout}>Déconnexion</button> )}
    
</div>
  )
}

export default Header
