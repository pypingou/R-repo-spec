%global packname  shapefiles
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Read and Write ESRI Shapefiles

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-foreign 

BuildRequires:    R-devel tex(latex) R-foreign 

%description
Functions to read and write ESRI shapefiles

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
%doc %{rlibdir}/shapefiles/html
%doc %{rlibdir}/shapefiles/DESCRIPTION
%{rlibdir}/shapefiles/R
%{rlibdir}/shapefiles/Meta
%{rlibdir}/shapefiles/help
%{rlibdir}/shapefiles/INDEX
%{rlibdir}/shapefiles/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora