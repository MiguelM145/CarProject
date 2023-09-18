import React, {useState} from 'react';
import {Link, useNavigate} from 'react-router-dom';
import axios from 'axios';

const NewStoreForm = ({stores, setStores}) => {
    const [storeName, setStoreName] = useState(""); 
    const [storeNumber, setStoreNumber] = useState("")
    const [isOpen, setIsOpen] = useState(false); 
    const navigate = useNavigate(); 
    const [errors, setErrors] = useState([]);

    const newStoreHandler = e => {
        e.preventDefault();

        axios.post("http://localhost:8000/api/stores", {
            storeName,
            storeNumber,
            isOpen
        })
        .then( res => {
            setStores([...stores, res.data]);
            navigate(`/stores/` + res.data._id)
        })
        .catch(err => {
            console.log(err.response.data);
            const errArray = []
            for ( const key of Object.keys(err.response.data.errors)) {
                errArray.push(err.response.data.errors[key].message);
            }
            setErrors(errArray);
        });
    }

    return(
        <form onSubmit={newStoreHandler}>
            <h1>Store Finder</h1>
            <h2>Add a new store!</h2>
            <Link to='/stores'>go back home</Link><br/><br/>
            <div style = {{color:"red"}}>
                {
                    errors.map((err, idx) => {
                        return(
                            <p key = {idx}>{err}</p>
                        )
                    }) 
                }
            </div>
            <label>Store Name </label>
            <input type='text' onChange ={e => setStoreName(e.target.value.length >= 3? e.target.value: null)}/><br/><br/>

            <label>Store Number </label>
            <input type='text' onChange ={e => setStoreNumber(e.target.value >= 1? e.target.value: null)}/><br/><br/>

            <input type='checkbox' checked={isOpen} onChange = {e => setIsOpen(e.target.checked)}/>
            <label> Open?</label><br/><br/>

            <button>Add a new Store</button>
        </form>
    );
}

export default NewStoreForm;