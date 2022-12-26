# ANPR System using Yolov7 & FastAPI

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

![](https://github.com/Willissarino/ANPR-yolov7-fastAPI/results/test.gif)


## Deployment

To deploy this project run

```bash
  uvicorn main:app --reload
```


## API Reference

#### Get plate number, bounding box coordinates, confidence

````http
  POST /object-to-json
````

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| ``file`` |``file: jpg/png`` | **Required**. Your image input|

#### Get image with bounding box & plate number

````http
  POST /object-to-img
````

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `file`      | `string` | **Required**. Your image input |

## Results

![Alt text](results/test.jpg?raw=true "Title")
```javascript
{
    "result": [
        {
            "xmin": 627.2541503906,
            "ymin": 559.2532348633,
            "xmax": 793.0282592773,
            "ymax": 606.4913330078,
            "confidence": 0.8642558455,
            "class": 0,
            "name": "number-plate",
            "num_plate": "BQS 99"
        }
    ]
}
```


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.linkedin.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)
