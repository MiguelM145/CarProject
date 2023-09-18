import React, {useEffect, useState} from 'react';
import {Link, useParams} from 'react-router-dom';
import axios from 'axios';

const StoreView = (props) => {
    const {id} = useParams(); 
    const [store, setStore] = useState({}); 

    useEffect(() => {
        axios.get(`http://localhost:8000/api/stores/${id}`)
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setStore(res.data); 
            })
            .catch(err=> console.log(err));
    },[id])

    return(
        <div>
            <h1>Store Finder</h1>
            <Link to='/stores'>go back home?</Link><br/>
            <h2>{store.storeName}</h2>
            <h2>{store.storeNumber}</h2>
            <h2>{store.isOpen? "Open" : "Closed"}</h2>

            <Link to={`/stores/edit/${id}`}><button>Edit Store Details</button></Link>
            
        </div>
    )
}

export default StoreView; 