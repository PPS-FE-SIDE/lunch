import React, { useState } from 'react'
import './App.css'
import axios, { AxiosResponse } from 'axios'

const navi = ['1', '2', '3']
const footerText = ['4', '5', '6']

type menuType = {
  menu: string[]
  price: string[]
}

type responseDataType = {
  [key: string]: menuType[]
}

const App = () => {
  const [store, setStore] = useState<responseDataType | null>(null)
  const [selectedStore, setSelectedStore] = useState<responseDataType | null>(null)
  React.useEffect(() => {
    axios.get('http://127.0.0.1:8000/').then((res: AxiosResponse<responseDataType>) => {
      console.log(res.data)
      const { data } = res
      setStore(data)
    })
  }, [])
  React.useEffect(() => {
    console.log(selectedStore)
  }, [selectedStore])

  const btn = () => {
    if (!store) return
    const storeKeys = Object.keys(store)
    const random = Math.floor(Math.random() * storeKeys.length)
    const storeName = storeKeys[random]
    const menu = store[storeName]
    setSelectedStore({ [storeName]: menu })
  }
  return (
    <>
      <header style={{ width: '100%', height: 70, marginTop: 50 }}>
        <div style={{ width: 1200, height: '100%', margin: '0 auto', display: 'flex' }}>
          <div style={{ width: 200 }}>
            <div style={{ width: 200, height: 42, marginTop: 13 }}>
              <img src='/logo.png' />
            </div>
          </div>
          <div style={{ width: 800, alignItems: 'center', display: 'flex' }}>
            <ul>
              {navi.map((item, index) => (
                <li key={index} style={{ paddingLeft: 30, display: 'inline-block' }}>
                  {item}
                </li>
              ))}
            </ul>
          </div>
          <div style={{ width: 200, fontWeight: 'bold', fontSize: 25, display: 'flex', alignItems: 'center' }}>
            LOG IN
          </div>
        </div>
      </header>
      <main style={{ width: '100%', height: 420, backgroundColor: '#efefef' }}>
        <div style={{ width: 1200, display: 'flex', margin: '0 auto' }}>
          <div style={{ width: '40%', height: 420, display: 'flex' }}>
            <div
              style={{
                width: '80%',
                margin: '10%',

                display: 'flex',
                justifyContent: 'center',

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
          <div style={{ width: '60%', height: 420 }}>
            {selectedStore ? (
              <ul>
                <li>{Object.keys(selectedStore)[0]}</li>
                {selectedStore[Object.keys(selectedStore)[0]].map((item, index) => {
                  return (
                    <li key={item.menu + String(index)}>
                      <span>{item.menu}</span>
                      <span>{item.price}</span>
                    </li>
                  )
                })}
              </ul>
            ) : (
              <div style={{ width: '88%', marginLeft: '6%', marginRight: '6%', height: '100%', overflow: 'hidden' }}>
                <img src='/delivery.jpg' alt='사진공간' />
              </div>
            )}
          </div>
        </div>
      </main>
      <footer style={{ width: '100%', height: 100 }}>
        <div
          style={{
            height: 100,
            alignItems: 'center',
            display: 'flex',
            justifyContent: 'center',
          }}
        >
          <ul>
            {footerText.map((item, index) => (
              <li key={index + item} style={{ paddingLeft: 30, display: 'inline-block', fontWeight: 'bold' }}>
                {item}
              </li>
            ))}
          </ul>
        </div>
      </footer>
    </>
  )
}

export default App
