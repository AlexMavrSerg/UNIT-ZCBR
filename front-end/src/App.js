// import Form from "./component/Form/form";
import ProfileSidebar from "./component/Profile/profile";
import { Wrapper } from './component/Wrapper/wrapper'
import { Pagination } from './component/Pagination/pagination';
import { Post  } from './component/Post/post';
import {
  Route,
  Routes,
} from "react-router-dom";

function App() {
  return (
    <>
    <Wrapper className="App">
      {/* <Form/> */}
      {/* <ProfileSidebar/> 
      {/* <Pagination /> */}

      <Routes>
        <Route path="/" element={<Pagination/>} />
        <Route path="/post/:id" element={<Post/>} />
      </Routes>

    </Wrapper>
    
  

    </>
    
  );
}

export default App;
