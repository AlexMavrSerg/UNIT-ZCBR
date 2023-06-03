import { useState } from 'react';
import '../Profile/profile.scss';
import sidebar from '../../UI-img/sidebar-arrow.svg';

// const Profile = () => {
//     const [profile, setProfile] = useState(false);
//     const [client, setClient] = useState(false);
//     const []

// }

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

<div className="profile-stickers"></div>

<div className="profile-stickers"></div>

      </div>

      <div className="toggle-button" onClick={handleToggle}>
       <img src={sidebar} alt="" className='profile-sidebar__arrow'/>
       <img src={sidebar} alt="" className='profile-sidebar__arrow'/>
       <img src={sidebar} alt="" className='profile-sidebar__arrow'/>
        </div>

      </div>
    );
  }
  
  export default ProfileSidebar;