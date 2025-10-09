import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from "./Home"
import About from "./About"
import Profiles from './Profiles'
import SingleProfile from './SingleProfile'
import MyProfile from './MyProfile'
import ErrorPage from './ErrorPage'

const ProvaRoutes = () => {
  return (
    <div className='container'>
      <h1>Prova Routes</h1>
      <BrowserRouter>
        <nav className='navbar'>
          <Link to='/' className='btn'>Home</Link>
          <Link to='/about' className='btn'>About</Link>
          <Link to='/profiles' className='btn'>Profiles</Link>
        </nav>
        {/*<Routes>
          <Route path='/' element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/profiles/' element={<Profiles />} />
            <Route path='/:id' element={<SingleProfile />} />
            <Route path='/me' element={<MyProfile />} />
          <Route path="*" element={<ErrorPage></ErrorPage>} />
        </Routes>*/}
      </BrowserRouter>
    </div>
  )
}

export default ProvaRoutes