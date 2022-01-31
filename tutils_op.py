# This program is distributed in the hope that it will be useful, but
# Wihtout any Warranty; without even the impied warranty of 
# Merchantibility or Fitness for a particular purpose. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# Along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Operator

class tutils_pnl_apply_all_op(Operator):
    bl_idname = "Apply all operator of the active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return true

            return False

        def execute(self, context):
            
            #Apply all modifiers of active object
            active_obj = context.view_layer.objects.active

            for mod in active_obj.modifiers:
                bpy.ops.object.modifier_apply(modifier=mod.name)

