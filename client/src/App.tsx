import React from 'react';
import BackgroundCheck from './components/BackgroundCheck';
import Origin from './components/Origin';
import FactChecker from './components/FactChecker';
import Summary from './components/Summary';
import LLM from './components/LLM';

const App: React.FC = () => {
    return (
        <div className="my-container">
            <BackgroundCheck />
            <Origin />
            <FactChecker />
            <Summary />
            <LLM />
        </div>
    );
};

export default App;
