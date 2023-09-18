import React, {useState, useEffect} from 'react';
import {Link, useParams, useNavigate} from 'react-router-dom';
import axios from 'axios';


const EditStore = ({stores, setStores}) => {
    const {id} = useParams(); 
    const navigate = useNavigate(); 
    const [storeName, setStoreName] = useState("");
    const [storeNumber, setStoreNumber] = useState("");
    const [isOpen, setIsOpen] = useState(false);
    

    useEffect(() => {
        axios.get(`http://localhost:8000/api/stores/${id}`)
            .then((res) => {
                setStoreName(res.data.storeName);
                setStoreNumber(res.data.storeNumber);
                setIsOpen(res.data.isOpen);
            })
            .catch(err=> console.log(err));
    },[id])

    const newStoreHandler = e => {
        e.preventDefault();
        
        axios.put(`http://localhost:8000/api/stores/${id}`,{
            storeName,
            storeNumber,
            isOpen
    })  
            .then(res => {
                navigate('/stores/');
            })
            .catch(err => console.log(err));
    }

    return(
        <form onSubmit={newStoreHandler}>
            <h1>Store Finder</h1>
            <h2>Edit This Store!</h2>
            <Link to='/stores'>go back home</Link><br/><br/>

            <label>Store Name </label>
            <input type='text' value={storeName} onChange ={e => setStoreName(e.target.value)}/><br/><br/>

            <label>Store Number </label>
            <input type='text' value={storeNumber} onChange ={e => setStoreNumber(e.target.value)}/><br/><br/>

            <input type='checkbox' checked = {isOpen} onChange ={e => setIsOpen(e.target.checked)}/>
            <label> Open?</label><br/><br/>
            
            <button>Edit Store</button>
        </form>
    );
}

export default EditStore;