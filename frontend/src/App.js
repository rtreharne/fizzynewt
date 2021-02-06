import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom"

import Navbar from "./components/Navbar/Navbar"
import Home from "./components/Home/Home"
import Create from "./components/Create/Create"


export default function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <br/>
        <Switch>
          <Route exact path="/">
            <Home/>
          </Route>
          <Route path="/create">
            <Create/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}