import './assets/main.css'
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="bg-gradient-to-r from-indigo-500 to-green-500 h-screen w-screen">
      <div className="flex flex-col h-screen">
        <div className="h-2/3 container mx-auto">
          <div className="container mt-72 mx-auto">
            <label className="block text-md font-medium text-gray-700">
              Search a song
              <input id="search"className="border-4 border-transparent focus:border-teal-400 w-full h-12 mx-auto rounded-md"></input>
            </label>
            </div>
          </div>
        <div className='h-1/3 bg-white'>
          <p>footer</p>
        </div>
      </div>
    </div>
  );
}

export default App;
