import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { Redirect } from "react-router-dom";
import { addProductPhotos, addProduct } from "../../store/product";
import './ProductForm.css';


const ProductForm = () => {
    const dispatch = useDispatch()
    const [name, setName] = useState("");
    const [image, setImage] = useState(null);
    const [price, setPrice] = useState("");
    const [quantity, setQuantity] = useState(1);
    const [description, setDescription] = useState("");

    const store = useSelector(state => state.session.user.store)

    let store_id;
    if (store) {
        store_id = store.id
    }

    const productCreate = async (e) => {
        e.preventDefault();
        await dispatch(addProduct(name, store_id, price, quantity, description, image))
    }
    //we needed to check how many products we had so that the new products id does not conflict with the ones we have
    const updateName = (e) => {
        setName(e.target.value);
    };

    const updatePrice = (e) => {
    setPrice(e.target.value);
    };

    const updateQuantity = (e) => {
    setQuantity(e.target.value);
    };

    const updateDescription = (e) => {
    setDescription(e.target.value);
    };

    const updateImage = (e) => {
        const file = e.target.files[0];
        setImage(file);
    }


    return (
        <>
            {store_id &&
            <form onSubmit={productCreate}>
                <div>
                    <label>Name</label>
                    <input
                    type="text"
                    name="name"
                    onChange={updateName}
                    value={name}
                    ></input>
                </div>
                <div>
                    <label>Price</label>
                    <input
                    type="text"
                    name="price"
                    onChange={updatePrice}
                    value={price}
                    ></input>
                </div>
                <div>
                    <label>Quantity</label>
                    <input
                    type="number"
                    name="quantity"
                    onChange={updateQuantity}
                    value={quantity}
                    ></input>
                </div>
                <div>
                    <label>Description</label>
                    <input
                    type="text"
                    name="description"
                    onChange={updateDescription}
                    value={description}
                    ></input>
                </div>
                <div>
                    <label>Photo Url</label>
                    <input
                    type="file"
                    accept="image/*"
                    onChange={updateImage}
                    ></input>
                </div>
                <button type="submit">Add Product</button>
            </form>
            }
        </>
    )
}

export default ProductForm;
