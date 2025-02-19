import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';
import Home from '../pages/Home';
import ResponseDisplay from './ResponseDisplay';

const App: React.FC = () => {
    return (
        <Router>
            <div className="app-container">
                <Header />
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/responses" component={ResponseDisplay} />
                </Switch>
                <Footer />
            </div>
        </Router>
    );
};

export default App;