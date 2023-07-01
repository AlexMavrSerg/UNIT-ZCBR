import React, { useState, useEffect } from "react";
import { Link,
useParams, } from "react-router-dom";
import axios from "axios";
import styles from './post.module.scss';
import errImg from "../../UI-img/page-not-found-1011853308-5b8f17d146e0fb005045416c.jpg";

export const Post = () => {

  const [page, setPage] = useState(null);

  const {id} = useParams();

  useEffect(() => {
    const fetchData = async ()  => {

      axios.get(` https://jsonplaceholder.typicode.com/photos/${id}`)
      .then(res => setPage(res.data))
      .catch(err => console.log(err));

    }
    fetchData()
  }, [id]);

  return (
    <>
    
    <div className={styles.container} >
      <div className={styles.wrapper}>

      {page && (
        <div className={styles.page}>
         
          <h1>{page.name}Более 10 тысяч человек приняли участие в обсуждении проекта программы воспитательной работы Движения Первых</h1>

          <h4 className={styles.date}>22 июня 2023</h4>

          <img src={errImg} alt={errImg} className={styles.image}/>
          <p className={styles.discription}>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellat nisi velit unde reiciendis. Explicabo facilis quis, repellendus necessitatibus hic voluptate commodi atque animi excepturi debitis aspernatur laborum eius repellat autem?
          Cum numquam, perferendis aut inventore similique quasi, optio corporis consequuntur, aspernatur autem pariatur sunt. Praesentium, cum asperiores. Fuga veritatis, eaque, nisi voluptas officia in reiciendis doloremque saepe inventore suscipit excepturi?
          Doloribus rem pariatur culpa quaerat hic nemo sequi suscipit asperiores impedit, ad laborum ex aliquid perspiciatis, necessitatibus vero? Et nobis, doloremque perferendis dolorum natus iure repellat laboriosam temporibus porro est!
          Omnis debitis ipsa consequatur similique optio sapiente officia eligendi modi deserunt! Veniam cupiditate laudantium repudiandae dolore, sunt, provident quis dicta accusantium exercitationem, voluptatem illo? Sapiente ipsam commodi libero mollitia pariatur!
          Alias magni qui consectetur labore beatae cumque! Vitae sequi sit recusandae laudantium iure aspernatur ratione iste laborum. Amet cupiditate tempore commodi praesentium dicta molestiae accusantium, quia repellendus libero delectus esse!
          Repellendus odit quae adipisci optio quod sit debitis amet a accusantium cumque saepe explicabo facere, quisquam repellat unde tenetur corrupti, iusto quas! Ullam deleniti neque voluptatum quidem tenetur quam sed!
          Saepe dolorum, modi eaque architecto, dolor praesentium rem atque fugiat sunt at expedita quos corporis, deserunt facere id perspiciatis. Aspernatur sapiente autem eos deleniti pariatur illum quo laudantium deserunt accusantium!
          Eligendi cum vel ea natus fuga tenetur id atque saepe reiciendis, nulla aperiam minima architecto beatae voluptatum accusamus totam in debitis eius voluptatibus explicabo exercitationem laudantium sit tempora. Sequi, itaque.
          Exercitationem ipsum voluptates laboriosam id praesentium eius sed consequuntur fugit doloremque. Omnis nam sunt culpa maiores dolores. Dolores asperiores, sint fugiat aut neque laboriosam? Ab aspernatur facilis cumque dolores temporibus.
          Nostrum recusandae itaque quas dolores. Inventore fugit laborum maiores voluptates excepturi, nulla dolor quisquam labore nisi unde rem modi assumenda ad aspernatur, recusandae tempora possimus? Quae dolor veritatis optio aspernatur.
          Vero, reprehenderit unde itaque saepe mollitia non vel voluptatibus eveniet expedita voluptas soluta rem dolorum cum laborum totam corporis, nisi porro nemo fugit rerum aliquid? Aliquam excepturi voluptatum itaque beatae?
          Labore aliquid similique quis, sequi porro blanditiis exercitationem nostrum sunt quod, magni rerum est, earum modi sapiente dolore? Iste, quasi rem omnis quo quos qui fuga alias nam veniam aliquid!
          Optio ex expedita dolor nulla obcaecati nemo soluta blanditiis illum eveniet, possimus iusto totam id tenetur! Laudantium eligendi iste unde nobis eius dolore alias ea. Magnam illo similique eaque sequi?
          Repudiandae soluta at illum recusandae, amet incidunt sapiente id nostrum fuga labore similique dicta earum. Explicabo ea ratione, totam et commodi deleniti eos, reiciendis facere corrupti, aliquam iure obcaecati temporibus.
          Magnam corporis doloribus fugit vel corrupti sint fugiat recusandae ducimus necessitatibus, voluptatibus in, ipsa, suscipit dolor consequuntur quisquam nobis vero iusto officiis soluta provident aspernatur? Fugit voluptas fugiat dolorum esse?
          Mollitia dolore officia placeat facilis vero quibusdam quas deserunt, omnis repellendus expedita quia nam ut delectus tempore, vitae cupiditate minima possimus. Nostrum, quibusdam. Fugiat sint nostrum expedita voluptatum voluptates porro.
          Animi, reprehenderit officia harum, consequuntur, aspernatur earum explicabo dolorum saepe non tenetur itaque? Enim, eos sit ullam voluptatibus, placeat eius asperiores totam, sequi rerum iusto quod voluptatum saepe minus? Vel.
          Exercitationem laboriosam impedit ab quos obcaecati ad culpa rerum aut consequuntur aliquam blanditiis, tenetur aperiam quia amet minima pariatur molestiae earum corrupti? Tempore necessitatibus accusamus accusantium! Ab ut totam nostrum.
          Error corrupti blanditiis vero praesentium dolor in, ea suscipit reiciendis eligendi, distinctio rem! Corporis soluta nam numquam dolorem ex nesciunt dolorum saepe magni consequuntur nisi, sequi recusandae, a, molestiae dolore.
          Consectetur nemo quam, obcaecati vitae incidunt fuga qui a ex placeat aliquam quasi! Corrupti aliquid temporibus dignissimos, quibusdam voluptatibus sed quas cum pariatur nulla consectetur error, facere autem eum nesciunt.</p>
        </div>
      )}
      
      
      <div className={styles.link}>
      <Link to="/" className={styles.text}>Назад к списку постов</Link>
      </div>

      </div>
    </div>
    
    </>
  )
}

