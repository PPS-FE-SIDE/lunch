import React from 'react'
import './App.css'

const App = () => {
  const btn = () => {
    const random = Math.floor(Math.random() * 11)
    console.log(random)
  }

  return (
    <>
      <header style={{ width: '100%', height: 100, backgroundColor: 'tomato' }} />
      <div style={{ width: '100%' }}>
        <div style={{ width: 1200, display: 'flex', margin: '0 auto' }}>
          <div style={{ width: '40%', height: 500, backgroundColor: '#efefef', display: 'flex' }}>
            <div
              style={{
                width: '80%',
                margin: '10%',

                display: 'flex',
                justifyContent: 'center',
                backgroundColor: 'yellow',
                alignItems: 'center',
              }}
            >
              <div style={{ display: 'flex', flexDirection: 'column' }}>
                <div style={{ width: 300, height: 200, fontWeight: 700, fontSize: 50 }}>If You Lazy, Just Call Us</div>
                <div
                  style={{
                    width: 300,
                    height: 60,
                    position: 'relative',
                    borderRadius: 100,
                    backgroundColor: 'white',
                  }}
                >
                  <div style={{ width: 40, height: 50, marginLeft: 10, marginTop: 10, display: 'inline-block' }}>
                    <img src='/logo192.png' />
                  </div>
                  <input
                    type='button'
                    style={{ width: 220, height: 50, outline: 0, position: 'absolute', left: 30, top: 5 }}
                    value='search restaurants ..'
                    onClick={btn}
                  />
                </div>
              </div>
            </div>
          </div>
          <div style={{ width: '60%', height: 500 }}>
            <div style={{ width: '88%', marginLeft: '6%', marginRight: '6%', height: '100%', overflow: 'hidden' }}>
              <img src='/delivery.jpg' alt='사진공간' />
            </div>
          </div>
        </div>
      </div>
      <footer style={{ width: '100%', height: 100, backgroundColor: 'tomato' }} />
    </>
  )
}

export default App
