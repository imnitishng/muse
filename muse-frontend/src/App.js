import './assets/main.css'
import React from 'react'

import './App.css'
import Search from './components/search'

const App = () => {

  return (
    <div className="flex flex-col h-screen">
      <div className="h-2/3 container mx-auto">
        <div className="container mt-72 mx-auto">
          <Search />
        </div>
      </div>
      <div className='h-1/3 bg-white'>
        <p>footer</p>
      </div>
    </div>
  )
}

export default App
