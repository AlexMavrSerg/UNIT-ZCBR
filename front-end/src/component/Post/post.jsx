import React, { useState, useEffect } from "react";
import { Link,
useParams, } from "react-router-dom";
import axios from "axios";
import styles from './post.module.scss';

export const Post = () => {

  const [page, setPage] = useState(null);

  const {id} = useParams();

  useEffect(() => {
    axios.get(`https://jsonplaceholder.typicode.com/photos/${id}`)
      // .then(res => res.json())
      // .then(data => setPost(data))
      .then(res => setPage(res.data))
      .catch(err => console.log(err));
  }, [id]);

  return (
    <>
    
    <div className={styles.container}>
      {page && (
        <div className={styles.page}>
          <p>{id}</p>
          <h1>{page.title}</h1>
          <img src={page.thumbnailUrl} alt="" />
        </div>
      )}
      
      
      <Link to="/">Назад к списку постов</Link>
    </div>
    
    </>
  )
}

