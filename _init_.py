# This program is distributed in the hope that it will be useful, but
# Wihtout any Warranty; without even the impied warranty of 
# Merchantibility or Fitness for a particular purpose. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# Along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
        "name" : "tutils",
        "author" : "Trevor Smale",
        "description" : "Utility Panel",
        "blender" : (3, 00, 0),
        "version" : (0, 0, 1,),
        "location" : "view3D",
        "warning" : "",
        "category" : "Object"

    }

import bpy

#need to load in class name from 'OP'
from . tutils_op import 

#need to load in class name from 'PT panel'
from . tutils_pnl import 

#define classes again
classes

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.register_class(c)   ...

