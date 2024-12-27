import pandas as pd
from sqlalchemy import text
import dotenv
from app.logs import init_log, logging_msg
from app.database import connect, disconnect



####################################################################################################
####################################################################################################
####################################################################################################

############
### INIT ###
############
def init()->bool:
    log_prefix = '[crud | init]'
    try:
        init_log()
        dotenv.load_dotenv('.env', override=True)

        logging_msg(f"{log_prefix} OK")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False


####################################################################################################
####################################################################################################
####################################################################################################

###########
### API ###
###########

def pd_isna(value):
    if pd.isna(value):
        return None
    return value


def get_products():
    log_prefix = '[crud | get_products]'
    try:
        if init():
            engine = connect()
            
            request = f"""
   SELECT p.*,
          pc.name pc_name, pc.rowguid pc_rowguid, pc.modifieddate pc_modifieddate,
          pm.name pm_name, pm.catalogdescription pm_catalogdescription, pm.instructions pm_instructions, pm.rowguid pm_rowguid, pm.modifieddate pm_modifieddate,
          pmpdc.productdescriptionid pmpdc_productdescriptionid, pmpdc.cultureid pmpdc_cultureid, pmpdc.modifieddate pmpdc_modifieddate,
          pd.description pd_description, pd.rowguid pd_rowguid, pd.modifieddate pd_modifieddate
     FROM Production.Product p
LEFT JOIN Production.ProductCategory pc ON pc.ProductCategoryID = p.ProductSubCategoryID
LEFT JOIN Production.ProductModel pm ON pm.ProductModelID = p.ProductModelID
LEFT JOIN Production.ProductModelProductDescriptionCulture pmpdc ON pmpdc.ProductModelID = p.ProductModelID
LEFT JOIN Production.ProductDescription pd ON pd.ProductDescriptionID = pmpdc.ProductDescriptionID
 ORDER BY p.ProductID, pc.ProductCategoryID, pm.ProductModelID, pmpdc.ProductModelID, pd.ProductDescriptionID
        """

            df_result = pd.read_sql_query(text(request), engine)
            json_result_tmp = None
            json_result = []
            json_productmodel = [{}]
            productid = 0
            for index, row in df_result.iterrows():
                product_productid = row['ProductID']
                product_name = row['Name']
                product_productnumber = row['ProductNumber']
                product_makeflag = row['MakeFlag']
                product_finishedgoodsflag = row['FinishedGoodsFlag']
                product_color = row['Color']
                product_safetystocklevel = row['SafetyStockLevel']
                product_reorderpoint = row['ReorderPoint']
                product_standardcost = row['StandardCost']
                product_listprice = row['ListPrice']
                product_size = row['Size']
                product_sizeunitmeasurecode = row['SizeUnitMeasureCode']
                product_weightunitmeasurecode = row['WeightUnitMeasureCode']
                product_weight = pd_isna(row['Weight'])
                product_daystomanufacture = row['DaysToManufacture']
                product_productline = row['ProductLine']
                product_class = row['Class']
                product_style = row['Style']
                product_productsubcategoryid = pd_isna(row['ProductSubcategoryID'])
                product_productmodelid = pd_isna(row['ProductModelID'])
                product_sellstartdate = row['SellStartDate']
                product_sellenddate = row['SellEndDate']
                product_discontinueddate = row['DiscontinuedDate']
                product_rowguid = row['rowguid']
                product_modifieddate = row['ModifiedDate']
                productcategory_name = row['pc_name']
                productcategory_rowguid = row['pc_rowguid']
                productcategory_modifieddate = row['pc_modifieddate']
                productmodel_name = row['pm_name']
                productmodel_catalogdescription = row['pm_catalogdescription']
                productmodel_instructions = row['pm_instructions']
                productmodel_rowguid = row['pm_rowguid']
                productmodel_modifieddate = row['pm_modifieddate']
                pmpdc_productdescriptionid = pd_isna(row['pmpdc_productdescriptionid'])
                pmpdc_cultureid = row['pmpdc_cultureid']
                pmpdc_modifieddate = row['pmpdc_modifieddate']
                pd_description = row['pd_description']
                pd_rowguid = row['pd_rowguid']
                pd_modifieddate = row['pd_modifieddate']

                if productid != product_productid:
                    if json_result_tmp:
                        json_result.append(json_result_tmp)

                    productid = product_productid

                    json_result_tmp = {
                        'ProductID': product_productid,
                        'Name': product_name,
                        'ProductNumber': product_productnumber,
                        'MakeFlag': product_makeflag,
                        'FinishedGoodsFlag': product_finishedgoodsflag,
                        'Color': product_color,
                        'SafetyStockLevel': product_safetystocklevel,
                        'ReorderPoint': product_reorderpoint,
                        'StandardCost': product_standardcost,
                        'ListPrice': product_listprice,
                        'Size': product_size,
                        'SizeUnitMeasureCode': product_sizeunitmeasurecode,
                        'WeightUnitMeasureCode': product_weightunitmeasurecode,
                        'Weight': product_weight,
                        'DaysToManufacture': product_daystomanufacture,
                        'ProductLine': product_productline,
                        'Class': product_class,
                        'Style': product_style,
                        'ProductSubcategoryID': product_productsubcategoryid,
                        'ProductModelID': product_productmodelid,
                        'SellStartDate': product_sellstartdate,
                        'SellEndDate': product_sellenddate,
                        'DiscontinuedDate': product_discontinueddate,
                        'rowguid': product_rowguid,
                        'ModifiedDate': product_modifieddate,
                        'ProductCategoryName': productcategory_name,
                        'ProductCategoryrowguid': productcategory_rowguid,
                        'ProductCategoryModifiedDate': productcategory_modifieddate,
                    }

                    json_productmodel = []
                    json_productmodel.append({
                            'Name': productmodel_name,
                            'CatalogDescription': productmodel_catalogdescription,
                            'Instructions': productmodel_instructions,
                            'rowguid': productmodel_rowguid,
                            'ModifiedDate': productmodel_modifieddate,
                            'pmpdc_productdescriptionid': pmpdc_productdescriptionid,
                            'pmpdc_cultureid': pmpdc_cultureid,
                            'pmpdc_modifieddate': pmpdc_modifieddate,
                            'pd_description': pd_description,
                            'pd_rowguid': pd_rowguid,
                            'pd_modifieddate': pd_modifieddate,
                        })
                    json_result_tmp['ProductModel'] = json_productmodel
                else:
                    json_productmodel.append({
                            'Name': productmodel_name,
                            'CatalogDescription': productmodel_catalogdescription,
                            'Instructions': productmodel_instructions,
                            'rowguid': productmodel_rowguid,
                            'ModifiedDate': productmodel_modifieddate,
                            'pmpdc_productdescriptionid': pmpdc_productdescriptionid,
                            'pmpdc_cultureid': pmpdc_cultureid,
                            'pmpdc_modifieddate': pmpdc_modifieddate,
                            'pd_description': pd_description,
                            'pd_rowguid': pd_rowguid,
                            'pd_modifieddate': pd_modifieddate,
                        })
                
            disconnect(engine)
            return json_result

        else:
            return None            
    
    except Exception as e:
        logging_msg(f"{log_prefix} Error: {e}", 'CRITICAL')
        return None


# def get_product_by_id(session: Session, product_id: int):
#     return session.query(Product).filter(Product.id == product_id).first()


# def create_product(session: Session, product: Product):
#     session.add(product)
#     session.commit()
#     session.refresh(product)
#     return product


# def update_product(session: Session, product_id: int, product_data: Product):
#     product = session.query(Product).filter(Product.id == product_id).first()
#     if product:
#         for key, value in product_data.dict(exclude_unset=True).items():
#             setattr(product, key, value)
#         session.commit()
#         session.refresh(product)
#         return product
#     return None


# def delete_product(session: Session, product_id: int):
#     product = session.query(Product).filter(Product.id == product_id).first()
#     if product:
#         session.delete(product)
#         session.commit()
#         return product
#     return None

####################################################################################################
####################################################################################################
####################################################################################################