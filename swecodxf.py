
import ezdxf

def create_mur(faces, btmLeft, btmRight, topRight, topLeft):
    doc = ezdxf.new()
    msp = doc.modelspace()

    polyface = msp.add_polyface(dxfattribs={'layer': '3D-Mur'})

    polyface.append_faces(faces, dxfattribs={'layer': '3D-Mur'})
    
    msp.add_polyline3d(btmLeft, dxfattribs={'layer': 'stikning-mur-ytterkant-bunn'})
    msp.add_polyline3d(btmRight, dxfattribs={'layer': 'stikning-mur-innerkant-bunn'})
    msp.add_polyline3d(topRight, dxfattribs={'layer': 'stikning-mur-innerkant-topp'})
    msp.add_polyline3d(topLeft, dxfattribs={'layer': 'stikning-mur-ytterkant-bunn'})

    doc.saveas('new_name.dxf')

    return 1