%global packname  maps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.2
Release:          1%{?dist}
Summary:          Draw Geographical Maps

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Display of maps.  Projection code and larger maps are in separate packages
(mapproj and mapdata).

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
%doc %{rlibdir}/maps/html
%doc %{rlibdir}/maps/DESCRIPTION
%{rlibdir}/maps/INDEX
%{rlibdir}/maps/mapdata
%{rlibdir}/maps/NAMESPACE
%{rlibdir}/maps/Meta
%{rlibdir}/maps/R
%{rlibdir}/maps/libs
%{rlibdir}/maps/data
%{rlibdir}/maps/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.2-1
- initial package for Fedora