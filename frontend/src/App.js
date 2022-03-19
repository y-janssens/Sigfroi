import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from "./context/Context";
import Header from "./components/Header";
import Background from "./components/Background";
import Fiches from "./pages/Fiches";
import Fiche from "./pages/Fiche";
import Carrieres from "./pages/Carrieres";
import Carriere from "./pages/Carriere";
import Login from "./pages/Login";
import PrivateRoute from "./components/PrivateRoute";
import Confirm from "./pages/Confirm";

function App() {
  return (
    <Provider>
      <Router>
        <Header />
        <Background />
        <Routes>
          <Route path="/login" element={<Login />} />

          <Route path="/confirm" element={<PrivateRoute />}>
          <Route path="/confirm/:item/:id" element={<Confirm />} />
          </Route>

          <Route path="/" element={<PrivateRoute />}>
            <Route path="/" element={<Fiches />} />
            <Route path="/:id" element={<Fiche />} />
          </Route>

          <Route path="/carrieres" element={<PrivateRoute />}>
            <Route path="/carrieres" element={<Carrieres />} />
            <Route path="/carrieres/:id" element={<Carriere />} />
          </Route>
        </Routes>
        
      </Router>
    </Provider>
  );
}

export default App;
