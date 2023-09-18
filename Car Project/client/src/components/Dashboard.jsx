import React from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';

const Dashboard = ({stores, setStores}) => {

    const deleteStoreHandler = e => {
        const storeDelete = e.target.id; 
        axios.delete(`http://localhost:8000/api/stores/${storeDelete}`)
            .then(res => {
                const filteredStores = stores.filter( store => store._id !== storeDelete);
                setStores(filteredStores);
            })
            .catch(err => console.log(err));
    }

    return(
        <div> 
            <h1>Store Finder</h1>
            <h2>Find stores in your area!</h2>

            <table>
                <tr>
                    <th>Store</th>
                    <th>Store Number</th>
                    <th>Open</th>
                    <th>Remove</th>
                </tr>
                    
                    {  
                    stores.map(stores => {
                        return(
                            <tr key={stores._id}> 
                                <td><Link to={`/stores/${stores._id}`}>{stores.storeName}</Link></td>
                                <td>{stores.storeNumber}</td>
                                <td>{stores.isOpen? "True": "False"}</td>
                                <td><button onClick = {deleteStoreHandler} id={stores._id}>Delete</button></td>
                            </tr>
                        )
                    })
                    }
            </table>
            <br/>
            <Link to='/stores/add'><button>Cant find your store?</button></Link>
        </div>
    );
}

export default Dashboard; 