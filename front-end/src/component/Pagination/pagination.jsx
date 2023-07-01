import axios from 'axios';
import { useState } from 'react';
import { useEffect } from 'react';
import styles from './pagination.module.scss';
import { Link } from "react-router-dom";
import errImg from "../../UI-img/page-not-found-1011853308-5b8f17d146e0fb005045416c.jpg";
export const Pagination = () => {

    const [pages, setPages] = useState([])
    const [currentPage, setCurrentPage] = useState(1)
    const [fetching, setFetching] = useState(true)
    const [totalCount, setTotalCount] = useState(0)

    useEffect(() => {
        if (fetching) {
            console.log('fetching')
            const getPosts = async ()  => {
                // https://jsonplaceholder.typicode.com/photos ссылка для демонстрации работы пагинации и роутинга между постами на случай если сервер не будет готов
                axios.get(`https://raw.githubusercontent.com/AlexMavrSerg/UNIT-ZCBR/BVD_Parser/output.json?_page=${currentPage}`) 
            .then(response => {
                setPages([...pages, ...response.data])
                setCurrentPage(prevState => prevState + 1) 
                setTotalCount(response.headers['x-total-count']) 
            })
            .catch(err => console.log("error:", err))
            .finally( () => setFetching(false));
            }
            getPosts()
    }
}, [fetching])

    useEffect(()=> {
        document.addEventListener('scroll', scrollHandler)
        return function() {
            document.removeEventListener('scroll', scrollHandler)
        };

    }, [totalCount])

    const scrollHandler = (e) => {
        if (e.target.documentElement.scrollHeight - ( e.target.documentElement.scrollTop + window.innerHeight) < 100 
        && pages.length < totalCount) {
            setFetching(true)
        }    
    }


    return(
 

<div className={styles.container}>{pages.map(page => 
            <div className={styles.page} key={page.id}>
                 <img className={styles.image} src={page.images} alt={errImg} />
                <h5>{page.date}</h5>
                <div className='title'>
                    <p>{page.name}</p>
                </div>
                   
            <div className={styles.link}>
            <Link key={page.id} to={`/post/${page.id}`}> <p className={styles.text}>Подробнее...</p></Link>
            </div>
                    
            </div>
            )}
        </div> 

     
    );
}