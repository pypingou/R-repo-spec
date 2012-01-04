%global packname  DATforDCEMRI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.52
Release:          1%{?dist}
Summary:          Deconvolution Analysis Tool for Dynamic Contrast Enhanced MRI

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-xtable R-akima R-R.oo R-R.methodsS3 R-matlab R-lattice R-locfit R-graphics R-grDevices R-grid 

BuildRequires:    R-devel tex(latex) R-xtable R-akima R-R.oo R-R.methodsS3 R-matlab R-lattice R-locfit R-graphics R-grDevices R-grid 

%description
This package performs voxel-wise deconvolution analysis of DCE-MRI
contrast agent concentration versus time data and generates the Impulse
Response Function, which can be used to approximate commonly utilized
kinetic parameters such as K^trans and ve.  An interactive advanced voxel
diagnosis tool (AVDT) is also provided to facilitate easy navigation of
voxel-wise data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/DATforDCEMRI/html
%doc %{rlibdir}/DATforDCEMRI/DESCRIPTION
%doc %{rlibdir}/DATforDCEMRI/CITATION
%{rlibdir}/DATforDCEMRI/Meta
%{rlibdir}/DATforDCEMRI/demo
%{rlibdir}/DATforDCEMRI/data
%{rlibdir}/DATforDCEMRI/R
%{rlibdir}/DATforDCEMRI/NAMESPACE
%{rlibdir}/DATforDCEMRI/help
%{rlibdir}/DATforDCEMRI/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.52-1
- initial package for Fedora