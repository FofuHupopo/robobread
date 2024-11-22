import ReactDOM from 'react-dom/client'
import App from './app/App.tsx'
import './app/styles/index.css'
import {BrowserRouter} from "react-router-dom";
import {Contacts} from "src/entities/contacts";
import {Error} from "src/entities/error";

ReactDOM.createRoot(document.getElementById('root')!).render(
    <BrowserRouter>
        <App/>
        <Error />
        <Contacts />
    </BrowserRouter>
)