import React from 'react'
import { Outlet, Link } from 'react-router-dom'

const Profiles = () => {
  return (
    <div>
        <h1>Profiles</h1>
        <nav className='navbar'>
            <Link to='/me' className='btn'>My Profile</Link>
            <Link to='/1' className='btn'>User 1</Link>
            <Link to='/2' className='btn'>User 2</Link>
            <Link to='/3' className='btn'>User 3</Link>
        </nav>
      <div><Outlet></Outlet></div>
    </div>
  )
}

export default Profiles
