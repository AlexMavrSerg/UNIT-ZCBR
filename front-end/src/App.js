// import Form from "./component/Form/form";
import ProfileSidebar from "./component/Profile/profile";
import { Wrapper } from './component/Wrapper/wrapper'
import { Pages } from './component/Pages/pages';

function App() {
  return (
    <Wrapper className="App">
      {/* <Form/> */}
      <ProfileSidebar/>
      <Pages />
    </Wrapper>
  );
}

export default App;
