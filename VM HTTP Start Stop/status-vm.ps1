param (
    [string]$vmName
)
(Get-VM -Name $vmName).State
