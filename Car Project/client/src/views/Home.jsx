import React, {useState, useEffect}from 'react';
import Dashboard from '../components/Dashboard';
import {Routes, Route} from 'react-router-dom';
import NewStoreForm from '../components/NewStoreForm';
import StoreView from '../components/StoreView';
import axios from 'axios';
import EditStore from '../components/EditStore';

const Home = (props) => {
    const [stores, setStores] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/stores')
            .then( res => setStores(res.data))
            .catch(err => console.log(err))
    }, [])

    return(
        <Routes> 
            <Route path="/" element={<Dashboard stores = {stores} setStores = {setStores}/>} />
            <Route path="/add" element={<NewStoreForm stores = {stores} setStores = {setStores}/>} />
            <Route path="/:id" element={<StoreView/>}/>
            <Route path="/edit/:id" element={<EditStore stores = {stores} setStores = {setStores}/>}/>
        </Routes>
    );
}

export default Home; 