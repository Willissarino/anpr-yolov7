# ANPR System using Yolov7 & FastAPI

![](https://github.com/Willissarino/anpr_yolov7_fastAPI/blob/master/results/test.gif)


## Deployment

To deploy this project run

```bash
  uvicorn main:app --reload
```


## API Reference

#### Get plate number, bounding box coordinates, confidence

```bash
  POST /object-to-json
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| ``file`` |``file: jpg/png`` | Your image input|

#### Get image with bounding box & plate number

```bash
  POST /object-to-img
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `file`      | `string` | Your image input |

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
