import React from 'react'
import './App.css'

import axios from 'axios'

const App = () => {
  React.useEffect(() => {
    axios.get('http://127.0.0.1:8000/').then((res) => console.log(res))
  }, [])
  return (
    <div className='App'>
      <div className='bg-orange-400'>안녕</div>
    </div>
  )
}

export default App
