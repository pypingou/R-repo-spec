%global packname  SpatialExtremes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.1
Release:          1%{?dist}
Summary:          Modelling Spatial Extremes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package proposes several approaches for spatial extremes modelling.

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
%doc %{rlibdir}/SpatialExtremes/html
%doc %{rlibdir}/SpatialExtremes/doc
%doc %{rlibdir}/SpatialExtremes/NEWS
%doc %{rlibdir}/SpatialExtremes/DESCRIPTION
%{rlibdir}/SpatialExtremes/help
%{rlibdir}/SpatialExtremes/data
%{rlibdir}/SpatialExtremes/R
%{rlibdir}/SpatialExtremes/Meta
%{rlibdir}/SpatialExtremes/libs
RPM build errors:
%{rlibdir}/SpatialExtremes/INDEX
%{rlibdir}/SpatialExtremes/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.1-1
- initial package for Fedora