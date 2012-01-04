%global packname  rpubchem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          rpubchem - Interface to the PubChem Collection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML R-car R-RCurl 


BuildRequires:    R-devel tex(latex) R-XML R-car R-RCurl



%description
Access PubChem data (compounds, substance, assays). Structural information
is provided in the form of SMILES strings. This package only provides
access to a subset of the precalculated data stored by PubChem. Bio-assay
data can be accessed to obtain descriptions as well as the actual data. It
is also possible to search for assay ID's by keyword. Currently the main
limitation is that only 1000 molecules can be downloaded at a time from
the PubChem servers

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.3-1
- initial package for Fedora