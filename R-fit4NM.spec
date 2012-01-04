%global packname  fit4NM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.3.3
Release:          1%{?dist}
Summary:          NONMEM platform

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gWidgets R-tcltk R-tkrplot R-RGtk2 R-gWidgetsRGtk2 R-cairoDevice 


BuildRequires:    R-devel tex(latex) R-gWidgets R-tcltk R-tkrplot R-RGtk2 R-gWidgetsRGtk2 R-cairoDevice



%description
This package is for NONMEM user

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.3.3-1
- initial package for Fedora