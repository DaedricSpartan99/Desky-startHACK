import SearchBar from './searchbar'
import './home.css'

import { useSelector, useDispatch } from 'react-redux'
import { setLocation } from './redux/slices/search'

import { useNavigate } from 'react-router-dom'

import sx_image from "./assets/sx.png"
import dx_image from "./assets/dx.png"
import background_video from "./assets/background.mp4"

export default function Home() {

  const dispatch = useDispatch()
  const navigate = useNavigate()

  function confirm(input) {
    if (input) {
      // switch page with router
      dispatch(setLocation(input));
      // navigate to other router
      navigate('/results');
    }
  }


  //<SearchBar confirm={confirm}/>
  return (
    <div>
      <video id='background-video' autoPlay loop muted>
        <source src={background_video} type='video/mp4' />
      </video>
      <div id="background-div">
        <div id="left-container">
          <img  id="left-image" src={sx_image} />
          <div id="left-filler"></div>
          <div id="left-padder">
            <SearchBar confirm={confirm}/>
          </div>
        </div>
        <img id="right-image" src={dx_image} />
      </div>
    </div>
  );
}
