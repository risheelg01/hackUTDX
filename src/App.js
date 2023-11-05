import "./App.css";
import Form from "./components/form";
import Game from "./components/game";
import Resources from "./components/resources";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Form />} />
        <Route path="/game" element={<Game />} />
        <Route path="/resources" element={<Resources />} />
      </Routes>
    </div>
  );
}

export default App;
