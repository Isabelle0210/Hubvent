import { Route, BrowserRouter as Router, Routes } from "react-router-dom"
import Login from "./pages/Login"



function App() {


  return (
      <Router>
        <nav>
          <link rel="stylesheet" href="teste" />
          <link rel="stylesheet" href="teste" />
        </nav>

        <Routes>
          <Route path="/" element={<Login/>} />
        </Routes>
      </Router>
  )
}

export default App
