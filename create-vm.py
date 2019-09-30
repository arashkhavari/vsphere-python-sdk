from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import vmutils
import ssl
import csv
path = raw_input("get the fakin path :\n")
with open( path, "r") as f:
  reader = csv.reader(f, delimiter=':')
  line_counter = 0
  for i in reader:
    if line_counter == 0:
      vcenter = i[0]
      username = i[1]
      password = i[2]
      template_name = i[3]
      new_vm_name = i[4]
      pool_resource = i[5]
      cpu_number = i[6]
      memory_on_mb = i[7]
      si = None
      try:
        si = SmartConnect(host=vcenter, user=username, pwd=password, port=443, sslContext=ssl._create_unverified_context())
      except IOError, e:
        pass
      template_vm = vmutils.get_vm_by_name(si, template_name)
      vmconf = vim.vm.ConfigSpec(numCPUs=int(cpu_number), memoryMB=int(memory_on_mb))
      adaptermap = vim.vm.customization.AdapterMapping()
      adaptermap.adapter = vim.vm.customization.IPSettings(ip=vim.vm.customization.DhcpIpGenerator(), dnsDomain='domain.local')
      globalip = vim.vm.customization.GlobalIPSettings()
      ident = vim.vm.customization.LinuxPrep(domain='domain.local', hostName=vim.vm.customization.FixedName(name=new_vm_name))
      customspec = vim.vm.customization.Specification(nicSettingMap=[adaptermap], globalIPSettings=globalip, identity=ident)
      resource_pool = vmutils.get_resource_pool(si, pool_resource)
      relocateSpec = vim.vm.RelocateSpec(pool=resource_pool)
      cloneSpec = vim.vm.CloneSpec(powerOn=True, template=False, location=relocateSpec, customization=None, config=vmconf)
      clone = template_vm.Clone(name=new_vm_name, folder=template_vm.parent, spec=cloneSpec)
      Disconnect(si)
      line_counter += 1
    else:
      vcenter = i[0]
      username = i[1]
      password = i[2]
      template_name = i[3]
      new_vm_name = i[4]
      pool_resource = i[5]
      cpu_number = i[6]
      memory_on_mb = i[7]
      si = None
      try:
        si = SmartConnect(host=vcenter, user=username, pwd=password, port=443, sslContext=ssl._create_unverified_context())
      except IOError, e:
        pass
      template_vm = vmutils.get_vm_by_name(si, template_name)
      vmconf = vim.vm.ConfigSpec(numCPUs=int(cpu_number), memoryMB=int(memory_on_mb))
      adaptermap = vim.vm.customization.AdapterMapping()
      adaptermap.adapter = vim.vm.customization.IPSettings(ip=vim.vm.customization.DhcpIpGenerator(), dnsDomain='domain.local')
      globalip = vim.vm.customization.GlobalIPSettings()
      ident = vim.vm.customization.LinuxPrep(domain='domain.local', hostName=vim.vm.customization.FixedName(name=new_vm_name))
      customspec = vim.vm.customization.Specification(nicSettingMap=[adaptermap], globalIPSettings=globalip, identity=ident)
      resource_pool = vmutils.get_resource_pool(si, pool_resource)
      relocateSpec = vim.vm.RelocateSpec(pool=resource_pool)
      cloneSpec = vim.vm.CloneSpec(powerOn=True, template=False, location=relocateSpec, customization=None, config=vmconf)
      clone = template_vm.Clone(name=new_vm_name, folder=template_vm.parent, spec=cloneSpec)
      Disconnect(si)
      line_counter += 1

