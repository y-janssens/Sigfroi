import Terminal from 'react-bash';

function App() {
  const clear = {
    exec: ({ structure, history, cwd }, command) => {
        return { structure, cwd, history: [] };
    },
};



const extensions = { clear };

const history = [
    { value: 'ls' },
    { value: 'Type `help` to begin' },
];
  return (
    <div className="App">
    <p>I'm TerminalScreen</p>
    <Terminal  history={history} command={'ls'} />
  </div>
  );
}

export default App;
