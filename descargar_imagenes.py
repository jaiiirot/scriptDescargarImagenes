from zipfile import ZipFile
from PIL import Image
import requests
from io import BytesIO

def descargar_imagenes_con_nombres(urls_con_nombres, ancho, alto):
    zip_filename = "imagenes.zip"
    with ZipFile(zip_filename, 'w') as zip:
        for obj in urls_con_nombres:
            response = requests.get(obj['image'])
            img = Image.open(BytesIO(response.content))
            img_resized = img.resize((ancho, alto))
            img_byte_array = BytesIO()
            img_resized.save(img_byte_array, format='PNG')
            img_data = img_byte_array.getvalue()
            filename = obj['title'] + '.png'
            zip.writestr(filename, img_data)

if __name__ == "__main__":
    urls_con_nombres = [
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8055bco-2-739b6b38d0e6e6c7b017029067485567-480-0.webp",
        "title": "MUSCULOSA_OVERISIZE_SLUSH_X5L1MZ"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/001a-38-63741ce827b1847bf017024062814063-480-0.webp",
        "title": "MUSCULOSA_OVERSIZE_KETCHUP_1CFVR4"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8055mar-3-09e17290026d349a7f17029066767700-480-0.webp",
        "title": "MUSCULOSA_OVERISIZE_SLUSH_GBBT00"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8041slm-1-1-bf9bf8fb080781921317018030394308-480-0.webp",
        "title": "MUSCULOSA_TRI_7Y5EBP"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8041vds-874a904783d0b8e28d16999798615982-480-0.jpg",
        "title": "MUSCULOSA_TRI_EC9H0K"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8041cml-3-018519da1d5ccf90d116999783402240-480-0.webp",
        "title": "MUSCULOSA_TRI_UF4VTC"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8057cru-1-99ad1aa89ef537fa7017030994157369-480-0.webp",
        "title": "MUSCULOSA_WAFFLE_SIDARTHUR_PRZC02"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8051bco-2-05aa4f568070cb707017024076898771-480-0.webp",
        "title": "MUSCULOSA_OVERSIZE_FRESH_8ML7IT"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8041ros-e7752f2437547cfa9d16999776390344-480-0.webp",
        "title": "MUSCULOSA_TRI_6LUJGO"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/mu8051vdm-4-2ce9b59451953f95ce17024009275545-480-0.webp",
        "title": "MUSCULOSA_OVERSIZE_FRESH_74JFTI"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/kazuma-201-fca6cf233baacc592f17049788690788-480-0.webp",
        "title": "JOGGER_JEAN_CARGO_BASSET_QHM15R"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/jj7900azm-1-d751712aedb4a78d3117017116087397-480-0.webp",
        "title": "JOGGER_JEAN_CARGO_COVENT_BH3JQS"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/kazuma-360-1-337987944c1d4e8f9416987709482550-480-0.webp",
        "title": "JOGGER_JEAN_CARGO_PITBULL_DI7LJP"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1643ngo-4-ec7823c976dd0efb0717030790098640-480-0.webp",
        "title": "JOGGER_JEAN_CARGO_HOLBORN_ILB3PY"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/pantalon-jogger-chino-negro-0212d2926b159f72dc16942250052037-480-0.webp",
        "title": "JOGGER_GABARDINA_DEMPSEY_[_NEGRO_]_JILUGD"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/pantalon-jogger-basic-camel1-8a156269f2fe282d9f16941195321328-480-0.webp",
        "title": "JOGGER_GABARDINA_DEMPSEY_[_BEIGE_]_MOAM4T"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/pg5020-8-8ec0ca15f880357d5216969507089874-480-0.webp",
        "title": "JOGGER_CARGO_GABARDINA_N0E2XK"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/kazuma-4-ae4217715229f3db2e17049798944000-480-0.webp",
        "title": "JOGGER_CARGO_GABARDINA_GXM7VI"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/kazuma-169-1-4799d9180a31d6957f17049801018348-480-0.webp",
        "title": "JOGGER_CARGO_GABARDINA_0S2XGH"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/5020vdm-d57ff43c059cec2b2a17049829817097-480-0.webp",
        "title": "JOGGER_CARGO_GABARDINA_H6WNA0"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1680bco-1-cc7fcde1fa6ef34c8f17029105742448-480-0.webp",
        "title": "REMERA_OVERSIZE_FESTIVE_0ZSVHV"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1619azf-3-65f3d9766a02d9a56c17029103633172-480-0.webp",
        "title": "REMERA_OVERSIZE_BOTTLE_VDPAZ5"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1619ngo-1-b8c07b34462e14a3ce17030158403809-480-0.webp",
        "title": "REMERA_OVERSIZE_BOTTLE_DW99VV"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1619bco-c871330b66e49e6c2d17030158140329-480-0.webp",
        "title": "REMERA_OVERSIZE_BOTTLE_AJCT1K"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1623cml-1-d89b34f7f99abdf99117024023081750-480-0.webp",
        "title": "REMERA_OVERSIZE_HERE_I3V22T"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1676bco-1-94e640dfdbe7a4832917019729261811-480-0.webp",
        "title": "REMERA_OVERSIZE_LOBSTER_F7YCO3"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1625bco-1-52721e970801f397e417019724983928-480-0.webp",
        "title": "REMERA_OVERSIZE_OWN_BAG_8Y0PF0"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/ro1644cru-4-223d2447838f7238f517017102777884-480-0.webp",
        "title": "REMERA_OVERSIZE_SUSHI_WPDRHL"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/001-4-e3b728e6cf07332f4f17024065002474-480-0.webp",
        "title": "REMERA_OVERSIZE_SUSHI_T8BJ8T"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/001-7-9103ce3d0423c4748217024064291073-480-0.webp",
        "title": "REMERA_OVERSIZE_SUSHI_TGSJFP"
    },
    {
        "image": "https://acdn.mitiendanube.com/stores/002/580/475/products/cl4797bco-1-fc8d72aa79b14dc66717018001149645-480-0.webp",
        "title": "CAMISA_BALANDRA_3239S8"
    }
]
    ancho = 250
    alto = 440
    descargar_imagenes_con_nombres(urls_con_nombres, ancho, alto)
