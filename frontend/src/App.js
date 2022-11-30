import './App.css';
import {useState} from "react";
import axios from "axios";

const baseURL = "http://127.0.0.1:8000/download/youtube/";

function App() {

  const [payload, setPayload] = useState(null)
  const [data, setData] = useState({title: '', duration: '', url: ''})
  const [isLoaded, setIsLoaded] = useState(false)

  const handleChange = event => {
    setPayload({...payload, type: event.target.value})
  };

  const handleText = event => {
    setPayload({...payload, url: event.target.value})
  };

  const handleClick = () => {
      axios.get(baseURL, {
        params: {
          type: payload.type,
          url: payload.url
        }
      }).then((response) => {
        setData(response.data);
      });
    setIsLoaded(true)
  }

  return (
    <div className="App">
      <h3>YouTube Downloader</h3>

      <div>
        <p>
          Enter URL for a YouTube video to download.
        </p>
        <input className="input-text" type="text" onChange={handleText}/>

        <p>
          Choose the format to download: audio or video file.
        </p>
      <div>
        <input type="radio" value="video" name="type" onChange={handleChange}/> Video
        <input type="radio" value="audio" name="type" onChange={handleChange}/> Audio
      </div>

        <div>
          <button className="button" onClick={handleClick}>
            Download
          </button>
        </div>

      </div>

      {isLoaded ?
          <div>
            <p>
              Information about the video:
            </p>
            <p>
              Title: {data.title}
            </p>
            <p>
              Duration: {data.duration}
            </p>
            <p>
              Direct link to download a video or audio:
            </p>
            <a className="link" href={data.link}>LINK</a>
          </div>
          :
          <div/>
      }
    </div>
  );
}

export default App;
