import Terminal from 'react-console-emulator'

function Shell() {
    const commands = {
        echo: {
          description: 'Echo a passed string.',
          usage: 'echo <string>',
          fn: (...args) => args.join(' ')
        }
      }
  return (
    <Terminal
        commands={commands}
        welcomeMessage={'Welcome to the React terminal!'}
        promptLabel={'me@React:~$'}
      />
  )
}

export default Shell