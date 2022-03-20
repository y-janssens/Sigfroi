import { useState, useEffect, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { getToken } from "../context/Actions";
import Context from "../context/Context";
import '../styles/login.css'

function Login() {
  const navigate = useNavigate();
  const [access, setAccess] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { dispatch } = useContext(Context);

  const onSubmit = (e) => {
    e.preventDefault();
    setAccess(true);
  };

  useEffect(() => {
    if (localStorage.getItem("authToken")) {
      navigate("/");
    } 

    if (access) {
      const getTokenAccess = async () => {
        const token = await getToken(username, password);

        try {
          dispatch({ type: "GET_TOKEN", payload: token });
          localStorage.setItem("authToken", JSON.stringify(token.access));
          navigate("/");
        } catch (error) {
          console.log(error);          
        }
      };

      getTokenAccess();
      setAccess(false);
      
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dispatch, access]);

  return (
    <div className="container">
      <form action="" className="login-form" onSubmit={onSubmit}>
        <input
          type="text"
          className="username-input"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          className="password-input"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" className="login-form-submit">
          Login
        </button>
      </form>
    </div>
  );
}

export default Login;
