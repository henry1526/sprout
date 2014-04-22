# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Item.color'
        db.delete_column(u'public_item', 'color')

        # Deleting field 'Item.is_inventory'
        db.delete_column(u'public_item', 'is_inventory')

        # Deleting field 'Item.low_point'
        db.delete_column(u'public_item', 'low_point')

        # Deleting field 'Item.dens_den_unit_id'
        db.delete_column(u'public_item', 'dens_den_unit_id')

        # Deleting field 'Item.min_ord_freq'
        db.delete_column(u'public_item', 'min_ord_freq')

        # Deleting field 'Item.inventory_scaler'
        db.delete_column(u'public_item', 'inventory_scaler')

        # Deleting field 'Item.width'
        db.delete_column(u'public_item', 'width')

        # Deleting field 'Item.location'
        db.delete_column(u'public_item', 'location')

        # Deleting field 'Item.demand_qrt'
        db.delete_column(u'public_item', 'demand_qrt')

        # Deleting field 'Item.dens_num_unit_id'
        db.delete_column(u'public_item', 'dens_num_unit_id')

        # Deleting field 'Item.dens_num'
        db.delete_column(u'public_item', 'dens_num')

        # Deleting field 'Item.purchase_unit_id'
        db.delete_column(u'public_item', 'purchase_unit_id')

        # Deleting field 'Item.lead_time'
        db.delete_column(u'public_item', 'lead_time')

        # Deleting field 'Item.transfer_sheet_id'
        db.delete_column(u'public_item', 'transfer_sheet_id')

        # Deleting field 'Item.mpn'
        db.delete_column(u'public_item', 'mpn')

        # Deleting field 'Item.moq'
        db.delete_column(u'public_item', 'moq')

        # Deleting field 'Item.material'
        db.delete_column(u'public_item', 'material_id')

        # Deleting field 'Item.is_active'
        db.delete_column(u'public_item', 'is_active')

        # Deleting field 'Item.volume'
        db.delete_column(u'public_item', 'volume')

        # Deleting field 'Item.demand_dly'
        db.delete_column(u'public_item', 'demand_dly')

        # Deleting field 'Item.height'
        db.delete_column(u'public_item', 'height')

        # Deleting field 'Item.is_figure_cost'
        db.delete_column(u'public_item', 'is_figure_cost')

        # Deleting field 'Item.purchase_amt'
        db.delete_column(u'public_item', 'purchase_amt')

        # Deleting field 'Item.is_direct_cost'
        db.delete_column(u'public_item', 'is_direct_cost')

        # Deleting field 'Item.is_warehouse'
        db.delete_column(u'public_item', 'is_warehouse')

        # Deleting field 'Item.is_template'
        db.delete_column(u'public_item', 'is_template')

        # Deleting field 'Item.min_on_hand'
        db.delete_column(u'public_item', 'min_on_hand')

        # Deleting field 'Item.drawings'
        db.delete_column(u'public_item', 'drawings')

        # Deleting field 'Item.create_date'
        db.delete_column(u'public_item', 'create_date')

        # Deleting field 'Item.weight'
        db.delete_column(u'public_item', 'weight')

        # Deleting field 'Item.recomb_ratio'
        db.delete_column(u'public_item', 'recomb_ratio')

        # Deleting field 'Item.cost'
        db.delete_column(u'public_item', 'cost')

        # Deleting field 'Item.common_name'
        db.delete_column(u'public_item', 'common_name')

        # Deleting field 'Item.description'
        db.delete_column(u'public_item', 'description')

        # Deleting field 'Item.template'
        db.delete_column(u'public_item', 'template_id')

        # Deleting field 'Item.supplier'
        db.delete_column(u'public_item', 'supplier_id')

        # Deleting field 'Item.reorder_point'
        db.delete_column(u'public_item', 'reorder_point')

        # Deleting field 'Item.critical_features'
        db.delete_column(u'public_item', 'critical_features')

        # Deleting field 'Item.revision'
        db.delete_column(u'public_item', 'revision_id')

        # Deleting field 'Item.is_update'
        db.delete_column(u'public_item', 'is_update')

        # Deleting field 'Item.attribute_id_3'
        db.delete_column(u'public_item', 'attribute_id_3')

        # Deleting field 'Item.attribute_id_2'
        db.delete_column(u'public_item', 'attribute_id_2')

        # Deleting field 'Item.attribute_id_1'
        db.delete_column(u'public_item', 'attribute_id_1')

        # Deleting field 'Item.is_recomb'
        db.delete_column(u'public_item', 'is_recomb')

        # Deleting field 'Item.reorder_qty'
        db.delete_column(u'public_item', 'reorder_qty')

        # Deleting field 'Item.item_type'
        db.delete_column(u'public_item', 'item_type_id')

        # Deleting field 'Item.depth'
        db.delete_column(u'public_item', 'depth')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Item.color'
        raise RuntimeError("Cannot reverse this migration. 'Item.color' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.color'
        db.add_column(u'public_item', 'color',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_inventory'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_inventory' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_inventory'
        db.add_column(u'public_item', 'is_inventory',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.low_point'
        raise RuntimeError("Cannot reverse this migration. 'Item.low_point' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.low_point'
        db.add_column(u'public_item', 'low_point',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.dens_den_unit_id'
        raise RuntimeError("Cannot reverse this migration. 'Item.dens_den_unit_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.dens_den_unit_id'
        db.add_column(u'public_item', 'dens_den_unit_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.min_ord_freq'
        raise RuntimeError("Cannot reverse this migration. 'Item.min_ord_freq' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.min_ord_freq'
        db.add_column(u'public_item', 'min_ord_freq',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.inventory_scaler'
        raise RuntimeError("Cannot reverse this migration. 'Item.inventory_scaler' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.inventory_scaler'
        db.add_column(u'public_item', 'inventory_scaler',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.width'
        raise RuntimeError("Cannot reverse this migration. 'Item.width' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.width'
        db.add_column(u'public_item', 'width',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.location'
        raise RuntimeError("Cannot reverse this migration. 'Item.location' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.location'
        db.add_column(u'public_item', 'location',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.demand_qrt'
        raise RuntimeError("Cannot reverse this migration. 'Item.demand_qrt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.demand_qrt'
        db.add_column(u'public_item', 'demand_qrt',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.dens_num_unit_id'
        raise RuntimeError("Cannot reverse this migration. 'Item.dens_num_unit_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.dens_num_unit_id'
        db.add_column(u'public_item', 'dens_num_unit_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.dens_num'
        raise RuntimeError("Cannot reverse this migration. 'Item.dens_num' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.dens_num'
        db.add_column(u'public_item', 'dens_num',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.purchase_unit_id'
        raise RuntimeError("Cannot reverse this migration. 'Item.purchase_unit_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.purchase_unit_id'
        db.add_column(u'public_item', 'purchase_unit_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.lead_time'
        raise RuntimeError("Cannot reverse this migration. 'Item.lead_time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.lead_time'
        db.add_column(u'public_item', 'lead_time',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.transfer_sheet_id'
        raise RuntimeError("Cannot reverse this migration. 'Item.transfer_sheet_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.transfer_sheet_id'
        db.add_column(u'public_item', 'transfer_sheet_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.mpn'
        raise RuntimeError("Cannot reverse this migration. 'Item.mpn' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.mpn'
        db.add_column(u'public_item', 'mpn',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.moq'
        raise RuntimeError("Cannot reverse this migration. 'Item.moq' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.moq'
        db.add_column(u'public_item', 'moq',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.material'
        raise RuntimeError("Cannot reverse this migration. 'Item.material' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.material'
        db.add_column(u'public_item', 'material',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Material']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_active'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_active' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_active'
        db.add_column(u'public_item', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.volume'
        raise RuntimeError("Cannot reverse this migration. 'Item.volume' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.volume'
        db.add_column(u'public_item', 'volume',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.demand_dly'
        raise RuntimeError("Cannot reverse this migration. 'Item.demand_dly' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.demand_dly'
        db.add_column(u'public_item', 'demand_dly',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.height'
        raise RuntimeError("Cannot reverse this migration. 'Item.height' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.height'
        db.add_column(u'public_item', 'height',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_figure_cost'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_figure_cost' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_figure_cost'
        db.add_column(u'public_item', 'is_figure_cost',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.purchase_amt'
        raise RuntimeError("Cannot reverse this migration. 'Item.purchase_amt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.purchase_amt'
        db.add_column(u'public_item', 'purchase_amt',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_direct_cost'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_direct_cost' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_direct_cost'
        db.add_column(u'public_item', 'is_direct_cost',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_warehouse'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_warehouse' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_warehouse'
        db.add_column(u'public_item', 'is_warehouse',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_template'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_template' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_template'
        db.add_column(u'public_item', 'is_template',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.min_on_hand'
        raise RuntimeError("Cannot reverse this migration. 'Item.min_on_hand' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.min_on_hand'
        db.add_column(u'public_item', 'min_on_hand',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.drawings'
        raise RuntimeError("Cannot reverse this migration. 'Item.drawings' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.drawings'
        db.add_column(u'public_item', 'drawings',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.create_date'
        raise RuntimeError("Cannot reverse this migration. 'Item.create_date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.create_date'
        db.add_column(u'public_item', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.weight'
        raise RuntimeError("Cannot reverse this migration. 'Item.weight' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.weight'
        db.add_column(u'public_item', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.recomb_ratio'
        raise RuntimeError("Cannot reverse this migration. 'Item.recomb_ratio' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.recomb_ratio'
        db.add_column(u'public_item', 'recomb_ratio',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.cost'
        raise RuntimeError("Cannot reverse this migration. 'Item.cost' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.cost'
        db.add_column(u'public_item', 'cost',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.common_name'
        raise RuntimeError("Cannot reverse this migration. 'Item.common_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.common_name'
        db.add_column(u'public_item', 'common_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.description'
        raise RuntimeError("Cannot reverse this migration. 'Item.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.description'
        db.add_column(u'public_item', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.template'
        raise RuntimeError("Cannot reverse this migration. 'Item.template' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.template'
        db.add_column(u'public_item', 'template',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Template']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.supplier'
        raise RuntimeError("Cannot reverse this migration. 'Item.supplier' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.supplier'
        db.add_column(u'public_item', 'supplier',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Supplier']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.reorder_point'
        raise RuntimeError("Cannot reverse this migration. 'Item.reorder_point' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.reorder_point'
        db.add_column(u'public_item', 'reorder_point',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.critical_features'
        raise RuntimeError("Cannot reverse this migration. 'Item.critical_features' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.critical_features'
        db.add_column(u'public_item', 'critical_features',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.revision'
        raise RuntimeError("Cannot reverse this migration. 'Item.revision' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.revision'
        db.add_column(u'public_item', 'revision',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Revision']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_update'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_update' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_update'
        db.add_column(u'public_item', 'is_update',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.attribute_id_3'
        raise RuntimeError("Cannot reverse this migration. 'Item.attribute_id_3' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.attribute_id_3'
        db.add_column(u'public_item', 'attribute_id_3',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.attribute_id_2'
        raise RuntimeError("Cannot reverse this migration. 'Item.attribute_id_2' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.attribute_id_2'
        db.add_column(u'public_item', 'attribute_id_2',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.attribute_id_1'
        raise RuntimeError("Cannot reverse this migration. 'Item.attribute_id_1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.attribute_id_1'
        db.add_column(u'public_item', 'attribute_id_1',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.is_recomb'
        raise RuntimeError("Cannot reverse this migration. 'Item.is_recomb' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.is_recomb'
        db.add_column(u'public_item', 'is_recomb',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.reorder_qty'
        raise RuntimeError("Cannot reverse this migration. 'Item.reorder_qty' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.reorder_qty'
        db.add_column(u'public_item', 'reorder_qty',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.item_type'
        raise RuntimeError("Cannot reverse this migration. 'Item.item_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.item_type'
        db.add_column(u'public_item', 'item_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.ItemType']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Item.depth'
        raise RuntimeError("Cannot reverse this migration. 'Item.depth' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Item.depth'
        db.add_column(u'public_item', 'depth',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


    models = {
        u'public.attributetype': {
            'Meta': {'object_name': 'AttributeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'abb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inventory': ('django.db.models.fields.BooleanField', [], {}),
            'is_non_inventory_item': ('django.db.models.fields.BooleanField', [], {}),
            'is_recoup': ('django.db.models.fields.BooleanField', [], {}),
            'is_template': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.revision': {
            'Meta': {'object_name': 'Revision'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'public.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Material']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.template': {
            'Meta': {'object_name': 'Template'},
            'attribute1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attribute2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']