%global packname  mapdata
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Extra Map Databases

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-maps 

BuildRequires:    R-devel tex(latex) R-maps 

%description
Supplement to maps package, providing the larger and/or higher-resolution

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
%doc %{rlibdir}/mapdata/html
%doc %{rlibdir}/mapdata/DESCRIPTION
%{rlibdir}/mapdata/INDEX
%{rlibdir}/mapdata/libs
%{rlibdir}/mapdata/mapdata
%{rlibdir}/mapdata/help
%{rlibdir}/mapdata/Meta
%{rlibdir}/mapdata/data
%{rlibdir}/mapdata/R
%{rlibdir}/mapdata/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.0-1
- initial package for Fedora