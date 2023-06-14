import { useState } from 'react';
import '../Profile/profile.scss';
import sidebar from '../../UI-img/sidebar-arrow.png';

function ProfileSidebar() {
    const [isOpen, setIsOpen] = useState('');

  
    const handleToggle = () => {
      setIsOpen(!isOpen);
    };
  

  
    return (
      <div className='profile-container'>

        <div className={`profile-sidebar ${isOpen ? 'open' : ''}`}>


<div className="client">
  <div className="client-icon"> 
       {/*  <img src="" alt="" /> */}
  </div>
  <div className="client-info">
    <span className="client-name">Антон Чигур</span>
    <span className="client-birthday">11 11 1111</span>
    <span className="client-id">DWIN: Gorter</span>
    <span className="client-supp">Supporters 9999</span>
  </div>
  

</div>

<div className="profile__stickers"></div>

<div className="profile__training"></div>

<div className="profile__notification"></div>

      </div>

      <button className="toggle-button" onClick={handleToggle}>

       <img src={sidebar} alt="" className={`profile-sidebar__arrow ${isOpen ? 'arrowOff' : ''}`}/>
       <img src={sidebar} alt="" className={`profile-sidebar__arrow ${isOpen ? 'arrowOff' : ''}`}/>
       <img src={sidebar} alt="" className={`profile-sidebar__arrow ${isOpen ? 'arrowOff' : ''}`}/>
        </button>

      </div>
    );
  }
  
  export default ProfileSidebar;