import React, { useState,useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../Header/Header';



const SearchCars = () => {
    const [cars, setCars] = useState([]);
    const [makes, setMakes] = useState([]);
    const [models, setModels] = useState([]);
    const [dealer, setDealer] = useState([]);
    const [message, setMessage] = useState([]);

    const { id } = useParams();

    let dealer_url = '/djangoapp/get_inventory/${id}';
    let fetch_url = '/djangoapp/dealer/${id}';

}