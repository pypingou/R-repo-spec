%global packname  SpatialVx
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Spatial Forecast Verification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fields 


BuildRequires:    R-devel tex(latex) R-fields



%description
Functions to perform most of the spatial forecast verification methods
carried out in the Spatial Forecast Verification Inter-Comparison Project
(ICP), and a few others.  This first version only has the neighborhood
methods, but the next version will have many more.

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
%doc %{rlibdir}/SpatialVx/html
%doc %{rlibdir}/SpatialVx/DESCRIPTION
%{rlibdir}/SpatialVx/Meta
%{rlibdir}/SpatialVx/NAMESPACE
%{rlibdir}/SpatialVx/R
%{rlibdir}/SpatialVx/data
%{rlibdir}/SpatialVx/INDEX
%{rlibdir}/SpatialVx/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora