import logo from './logo.svg';
import './App.css';
import Home from './home'
import { ChakraProvider } from '@chakra-ui/react'
import searchStore from './redux/search_store'
import { Provider } from 'react-redux'
import React, { Suspense } from 'react';

import ReactDOM from 'react-dom'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

const LazyResults = React.lazy(() => import('./results'));

function App() {
  return (
    <ChakraProvider>
      <Provider store={searchStore}>
        <BrowserRouter>
          <Suspense fallback={<div>Loading...</div>}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/results" element={<LazyResults />} />
            </Routes>
          </Suspense>
        </BrowserRouter>
      </Provider>
    </ChakraProvider>
  );
}

export default App;
